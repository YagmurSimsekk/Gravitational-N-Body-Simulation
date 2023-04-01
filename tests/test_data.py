import sys
import numpy as np
import packages.constants as C

from packages.initial_data import DataInitializer

def test_initial_data():
    _data_initializer = DataInitializer()
    
    ## RANDOM INITIAL DATA
    initial_data = _data_initializer.getNBodyData()

    ## Check positions of all bodies at timestep 1 and 2, they should be different as calculated by the integrator
    assert (len(initial_data.positions) == C.bodies) 

    
