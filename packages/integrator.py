from abc import abstractmethod
import numpy as np
from . import constants
from . import model
#class Integrator():
#    @abstractmethod
#    def calculateVelocity(self):
#        return
#
#    def step(self, dt: float):
#        '''This is an abstract method that solves the discreticed ODE. It does not have an implementation.
#        Every integrator we define needs to implement this method.'''
#    
#    def compute(self, N: int, r_data: SimulationData, time_step):
#        '''Method'''

class Integrator():

    def __init__(self, mass: np.array, init_pos: np.array, init_vel: np.array, size: np.array,colour : np.array):
        self.size = size
        self.mass = mass.astype(float)
        self.init_pos = init_pos
        self.init_vel = init_vel
        self.N = len(self.mass)
        self.G = constants.G
        self.dt = constants.dt
        self.colour= colour
            

    def calculateAcceleration_Total_Energy(self):
        #Defining a 3D array with positions and calculatins abs distances
        pos_A = np.full(shape=(self.N,self.N,3), fill_value = self.init_pos, dtype = float) #setting up a N x N x 3 array
        pos_B = np.transpose(pos_A, axes=(1,0,2)) #transposing the previous 3D array - returns a N x N x 3 array
        vector = np.array(pos_B - pos_A) #vectors from body to body
        abs_distance = np.sqrt(np.sum((vector**2),axis=2,dtype=float)) #absolute distances between bodies - returns a N x N array
        
        #Calculating actual accelerations
        acc = np.divide((self.G*vector),(abs_distance**3)[:,:,np.newaxis], dtype= float) #calculating 3D array with acc for each body in each direction
        acc[np.isnan(acc)] = 0.0
        acc[np.isinf(acc)] = 0.0 #assigning value 0 to where we have div by 0
        acc = np.multiply(acc, self.mass[np.newaxis, :, np.newaxis]) #multiplying by mass to get acc - returns a 
        acc = np.sum(acc, axis = 1) #summing up acc for each body in each direction - returns a N x 3 array
        acc = acc.astype(float)

        #Calculating total energy of the system
        total_energy = np.multiply(self.mass[np.newaxis,:],self.mass[:, np.newaxis])
        total_energy = np.divide(total_energy, abs_distance, out=np.zeros_like(total_energy), where=abs_distance!=0)
        total_energy = total_energy.astype(float)
        total_energy = self.G*np.sum(total_energy) + np.sum(np.multiply(abs(0.5*self.init_vel**2), self.mass[:,np.newaxis]))
        
        return acc, total_energy
            
    def calculateVelocity(self, init_vel: np.array, acc: np.array, dt:float):
        vel = np.add(init_vel, acc * dt) #returns a N x 3 array
        return vel

    def calculatePosition(self, init_pos: np.array, vel: np.array, dt:float):
        pos = np.add(init_pos, vel * dt) #returns a N x 3 array
        return pos
    
    def calculateCenterOfMass(self):
        center_of_mass = np.multiply(self.init_pos.T, self.mass).T
        center_of_mass = np.divide(np.sum(center_of_mass, axis = 0), np.sum(self.mass))
        return center_of_mass

class VerletIntegrator(Integrator):
    
    def step(self, time_step: int):
        
        acc, total_energy = Integrator.calculateAcceleration_Total_Energy(self)
        vel = Integrator.calculateVelocity(self, init_vel = self.init_vel, acc = acc, dt = self.dt)
        pos = Integrator.calculatePosition(self, init_pos = self.init_pos, vel = vel, dt = self.dt)
        self.init_vel = vel
        self.init_pos = pos

        center_of_mass = Integrator.calculateCenterOfMass(self)

        return model.SimulationData(time_step, pos, vel, self.mass, self.size,self.colour, total_energy, center_of_mass)

class VelocityVerlet(Integrator):
    
    def step(self, time_step: int):
        
        acc, total_energy = Integrator.calculateAcceleration_Total_Energy(self) #calculating a(n) for v(n+0.5)
        vel = Integrator.calculateVelocity(self, init_vel = self.init_vel, acc = acc, dt = self.dt/2) #calculating v(n+0.5)
        pos = Integrator.calculatePosition(self, init_pos = self.init_pos, vel = vel, dt = self.dt) #calculating p(n+1) with v(n+0.5)

        self.init_pos = pos    
        self.init_vel = vel

        center_of_mass = Integrator.calculateCenterOfMass(self)

        return model.SimulationData(time_step, pos, vel, self.mass, self.size,self.colour, total_energy, center_of_mass)
class PositionVerlet(Integrator):

    def step(self, time_step: int):

        pos = Integrator.calculatePosition(self, init_pos = self.init_pos, vel = self.init_vel, dt = self.dt/2)
        
        self.init_pos = pos

        acc, total_energy = Integrator.calculateAcceleration_Total_Energy(self)
        vel = Integrator.calculateVelocity(self, init_vel = self.init_vel, acc = acc, dt = self.dt)

        self.init_vel = vel

        center_of_mass = Integrator.calculateCenterOfMass(self)

        return model.SimulationData(time_step, pos, vel, self.mass, self.size,self.colour, total_energy, center_of_mass)


    #def step(self, body1: Celestial_Object, body2: Celestial_Object, dt: float):
        # For two body, we need to pass in two data objects?
        #self.calculatePosition(body1.pos, body1.v, dt)
        #self.calculateAcceleration(body2.mass, body2.pos, body1.pos, G)
        #self.calculateVelocity(body1.init_vel, dt)

        #body1.init_vel = self.updated_vel
        #body1.pos = self.updated_pos
        #return body1

    #def compute(self, N: int, r_data: SimulationData, time_step) -> SimulationData: 

        #_accelerations = np.zeros([N, N, 3])  # empty array for forces

        # loop through each pair of bodies
        #for i in range(N):  # index for body 1
            #body1_position = r_data.positions[i]
            #body1_velocity = r_data.velocities[i]
            #body1_mass = r_data.masses[i]
            #body1 = Celestial_Object(r_data.masses[i], r_data.positions[i][0], r_data.positions[i][1], r_data.positions[i]
                                     #[2], r_data.velocities[i][0], r_data.velocities[i][1], r_data.velocities[2])
    	    
                       
            #for j in range(N):  # index for body 2
                # calculate the force
                #if (i == j):
                    #continue
                #body2 = Celestial_Object(r_data.masses[j], r_data.positions[j][0], r_data.positions[j][1], r_data.positions[j]
                                         #[2], r_data.velocities[j][0], r_data.velocities[j][1], r_data.velocities[2])
                #body2_position = r_data.positions[j]
                #body2_velocity = r_data.velocities[j]
                #body2_mass = r_data.masses[j]

                # calculate the interaction for body 1 and body 2
                #_accelerations[i][j]= self.calculateAcceleration( body2_mass, body2_position, body1_position, G)
        
        #for i in range(N):
            #sum up the acceleration for body 1 with all others
            #body1_total_acc = np.sum(_accelerations[i], axis=0)

            #calculate the velocity
            #r_data.velocities[i] = self.calculateVelocity(r_data.velocities[i],body1_total_acc, time_step)
            
            #calculate new position of body 1
            #r_data.positions[i] = self.calculatePosition(r_data.positions[i],r_data.velocities[i], time_step)
        
        #r_data.time_step = time_step
        #print('Positions')
        #print(r_data.positions)
        #print('Velocitites')
        #print(r_data.velocities)
        #return SimulationData(time_step, r_data.positions, r_data.velocities, r_data.masses, r_data.sizes)
        
#lass LeapFrogIntegrator(Integrator):

    #def calculateVelocity(self):
    #    return

    #def step(self, dt: float):
    #    return dt
