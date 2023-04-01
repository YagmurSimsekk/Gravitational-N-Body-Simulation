import copy
import sys
import numpy as np
from math import pi
import packages

from packages.initial_data import DataInitializer
from packages.integrator import VerletIntegrator
from packages.simulation import SystemSimulator
import packages.constants as C

'''
This is a unit test to test simulation code. 
The test asserts if the simulator runs and calculate new positions and momenta of bodies for the number of timesteps entered in the C.py file.
'''
def test_simulator_from_constants():
    _data_initializer = DataInitializer()    
    outputs = []

    ## TIMESTEPS
    _ts = 3
    _num_of_bodies = 4

    ## RANDOM INITIAL DATA
    initial_data = _data_initializer.getNBodyData()

    ##INITIALIZE INTEGRATOR
    _integrator = VerletIntegrator(initial_data.masses, initial_data.positions, initial_data.velocities, initial_data.sizes, initial_data.colors)
        
    ## initialize and call simulate
    _simulator = SystemSimulator(_integrator)
    outputs= _simulator.simulate()

    ## Check if total number of outputs returned are equal to the simulation steps
    assert (len(outputs) == C.steps)
'''
This is a unit test to test setting steps and number of bodies on the run. 
The test includes setting up Constants values
The test asserts if the simulator runs with new values of steps specified in the test case.
'''

def test_simulator_with_setting_constants():
    _data_initializer = DataInitializer()    
    outputs = []

    ## TIMESTEPS -> set the constants value here
    C.steps = 3
    C.bodies = 3

    C.timeline = np.linspace(0, 6 * pi, C.steps)
    C.dt = C.timeline[1] - C.timeline[0]    

    ## RANDOM INITIAL DATA
    initial_data = _data_initializer.get3BodyData()

    ##INITIALIZE INTEGRATOR
    _integrator = VerletIntegrator(initial_data.masses, initial_data.positions, initial_data.velocities, initial_data.sizes, initial_data.colors)
        
    ## initialize and call simulate
    _simulator = SystemSimulator(_integrator)
    outputs= _simulator.simulate()

    ## Check if total number of outputs returned are equal to the simulation steps set in this method
    assert (len(outputs) == C.steps)
