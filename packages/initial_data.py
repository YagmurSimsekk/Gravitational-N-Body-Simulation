import numpy as np
from . import data
from . import model
from . import constants

from galpy.potential import  MWPotential2014, KeplerPotential
from galpy.util import conversion
from numpy.random import default_rng


class DataInitializer:

    def __init__(self) -> None:
        pass
    
    '''
    Method to generate a Gaussian distribution of points.    
    '''
    def gauss_3d(self, loc, x_s, y_s, z_s, N):
            rng = default_rng()
            x = rng.normal(loc=loc, scale=x_s, size=(N, 1))
            y = rng.normal(loc=loc , scale=y_s, size=(N, 1))
            z = rng.normal(loc=z_s, scale= z_s, size=(N, 1))  #Note mean for z-dim is kept same as the scale
            
            # initialize vector for orthogal velocities of the stars u(x,y,z) is orthogonal to u(y,-x,z)
            return np.dstack((x, y, z)).squeeze(1), np.dstack((y,-x, z)).squeeze(1)
    
    '''
    getNBodyData - Method to generate random data for N bodies
    simuates a stable system
    initial velocities are taken orthogonally with respect to positions

    Constants file data to be used as follows :
        !!  G = -6.6743*(10**-11) #gravitational constatnts in SI units
        !!  steps=10000
        !!  timeline = np.linspace(0,1000, steps)
        !!  bodies = 20
    '''
    def getNBodyData(self):
        N = constants.bodies
        
        r_positions, r_velocities = self.gauss_3d(1,10,10,10, N)        #get positions and velocities following a Gaussian distribution
        r_velocities = r_velocities * 1e-2        
        r_sizes = np.random.uniform(5000, 8000, size=[N])
        r_masses =np.ones(N) *1e7 #* np.ones((N)) 
        r_velocities -= np.mean(r_masses[:,None] * r_velocities,0) / np.mean(r_masses)
        r_timestamp = 0  # for initial timestep.
        c = np.random.uniform(1, 5, N).T

        center_of_mass = np.divide(np.sum(np.multiply(r_positions.T, r_masses).T, axis=0), np.sum(r_masses))

        return model.SimulationData(time_step=r_timestamp, positions=r_positions, velocities=r_velocities, masses=r_masses, sizes=r_sizes, colors=c, total_energy=0.0, center_of_mass=center_of_mass)    
    '''
    nasaData :
    Method to fetch 30 different bodies by using NASA Horizons API
    to simulate the parts of Solar System
    Constants file data to be used as follows :
        !!  G = -6.6743*(10**-11) #gravitational constatnts in SI units
        !!  steps=10000
        !!  timeline = np.linspace(0,1000, steps)
        !!  bodies = 30
    '''

    def nasaData(self):

        df = data.nasadata_func()
        r_positions = df[["x", "y", "z"]].to_numpy()
        r_velocities = df[["vx", "vy", "vz"]].to_numpy()
        r_masses = df["mass"].to_numpy()
        r_timestamp = 0
        r_sizes = df["size"].to_numpy()
        c = df["color"].to_numpy()

        center_of_mass = np.divide(
            np.sum(np.multiply(r_positions.T, r_masses).T, axis=0), np.sum(r_masses))

        return model.SimulationData(time_step=r_timestamp, positions=r_positions, velocities=r_velocities, masses=r_masses, sizes=r_sizes, colors=c, total_energy=0.0, center_of_mass=center_of_mass)
    '''
    getOrthogonalData :
    Method to fetch 2-body initial data
    to simulate a 2-body stable orthogonal system
    Constants file data to be used as follows :
        !!  G = -6.6743*(10**-11) #gravitational constatnts in SI units
        !!  steps=10000
        !!  timeline = np.linspace(0,1000, steps)
        !!  bodies = 2
    '''
    def getOrthogonalData(self):

        r_positions = np.array([[2, 2, 0], [1, 1, 0]])        
        r_velocities = np.array([[0, -1e-2, -1e-2], [0, 1e-2, 1e-2]])
        r_sizes = np.array([1, 1]) * 1e4
        r_masses = np.array([1, 1]) * 1e7
        r_timestamp = 0
        c = np.array([1, 255])

        center_of_mass = np.divide(
            np.sum(np.multiply(r_positions.T, r_masses).T, axis=0), np.sum(r_masses))

        return model.SimulationData(time_step=r_timestamp, positions=r_positions, velocities=r_velocities, masses=r_masses, sizes=r_sizes, colors=c, total_energy=0.0, center_of_mass=center_of_mass)
    '''
    get3BodyData :
    Method to fetch 3-body initial data
    to simulate a 3-body stable system
    Constants file data to be used as follows :
        !!  G = -6.6743*(10**-11) #gravitational constatnts in SI units
        !!  steps=10000
        !!  timeline = np.linspace(0,1000, steps)
        !!  bodies = 3
    '''
    def get3BodyData(self):

        r_positions = np.array([[2, 2, 0], [0, 2, 2], [2, 0, 2]])
        r_velocities = np.array([[-1e-2, 1e-2, 0], [ 0, -1e-2, 1e-2], [ 1e-2, 0, -1e-2]])
        r_sizes = np.array([1, 1, 1]) * 1e4
        r_masses = np.array([1, 1, 1]) * 1e7
        r_timestamp = 0
        c = np.array([1, 255, 105])

        center_of_mass = np.divide(
            np.sum(np.multiply(r_positions.T, r_masses).T, axis=0), np.sum(r_masses))

        return model.SimulationData(time_step=r_timestamp, positions=r_positions, velocities=r_velocities, masses=r_masses, sizes=r_sizes, colors=c, total_energy=0.0, center_of_mass=center_of_mass)

    '''
    Method to model initial scientific data
    The function uses Galphy and MiyamotoNagaiPotential to predict initial velocities of the bodies
    The initial positions are governed by a Gaussian distribution
    Constants file data to be used as follows :
        !!  #G = G * (parsec_distance ** -3) * (solar_mass ** 1) * (Gyr_time ** 2) G in GALPY Natural Units
        !!  steps=10000
        !!  dt = timeline[1] - timeline[0]
        !!  bodies = 200

    '''
    def getModelData(self):
        N = constants.bodies
      
        # initial Galaxy with random positions of stars in a disc shape i.e. z-dim =0
        _positions, _orth_vel = self.gauss_3d(0, 10, 10, 0, N) #positions are in the order of 1kpc(kiloparsec)

        # unit vector to compute velocities at later stage
        _unit_vel = np.asarray([v / np.sqrt(np.sum(v**2)) for v in _orth_vel]) 

        _distances = np.linalg.norm(_positions - [0, 0, 0], axis=-1) #
        _mass = np.ones(N) #* 10e2 #SM scaled to mass of 1 star
       
        # initial Galphy Potential function which helps us to create initial velocity vectors
        #with black hole
        MWPotential2014wBH = MWPotential2014 + \
            KeplerPotential(amp=5*10**6./conversion.mass_in_msol(220., 8.))
        mp = MWPotential2014wBH[1]

        #calculate velocities
        _velocities = np.zeros((N, 3))
        # get the initial velocities from initial MWPotential2014
        for i in range(N):
            # potential for each item at t=0
            #_p = conversion.potential_physical_input(mp._evaluate)(_distances[i], 0)
            _p = mp._evaluate(_distances[i], 0)
            _velocities[i] = (_unit_vel[i] )* _p/_distances[i] * 1 #time=1day

        _sizes = 5000 * np.ones(N) 
        _c = np.random.randint(1,255,size=N) # np.ones(N).T

        center_of_mass = (_positions * _mass[:, None]).mean(axis=0)

        # initial a starting model data
        return model.SimulationData(time_step=0, positions=_positions, velocities=_velocities, masses=_mass, sizes=_sizes, colors=_c, total_energy=0.0, center_of_mass=center_of_mass)

    