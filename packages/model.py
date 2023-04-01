
import numpy as np

'''Sample Model for Celestial obj Data
TODO - to be replaced with the data models later.
'''

class Celestial_Object:
    def __init__(self, mass, x, y, z, init_vel, colour, rad):
        # Assingning the fixed values gathered from NASA Horizons
        self.mass = mass
        self.init_vel = init_vel
        self.colour = colour
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

        self.pos = np.array([x,y,z])

'''Sample Model for Simulation Data
TODO - to be replaced with the data models later.
'''

class SimulationData():
    def __init__(self, time_step: int, positions: np.array, velocities: np.array, masses: np.array, sizes: np.array, colors : np.array, total_energy: float, center_of_mass: np.array):
        self.time_step = time_step
        self.positions = positions
        self.velocities = velocities
        self.masses = masses
        self.sizes = sizes
        self.colors = colors
        self.total_energy = total_energy
        self.center_of_mass = center_of_mass
