import copy
import packages
from packages.initial_data import DataInitializer
from packages.model import SimulationData
from packages.integrator import VerletIntegrator

def test_verlet_compute():
    _data_initializer = DataInitializer()
    outputs = [SimulationData]

    ## TIMESTEPS
    _ts = 3
    _num_of_bodies = 3

    ## RANDOM INITIAL DATA
    initial_data = _data_initializer.get3BodyData()

    ##INITIALIZE INTEGRATOR
    _integrator = VerletIntegrator(initial_data.masses, initial_data.positions, initial_data.velocities, initial_data.sizes, initial_data.colors)
        
    ## Loop over all timesteps
    for step in range(_ts):
        y =  _integrator.step(time_step= step)            
        outputs.append(copy.deepcopy(y))

    ## Check positions of all bodies at timestep 1 and 2, they should be different as calculated by the integrator
    assert (outputs[1].positions != outputs[2].positions).all() 
