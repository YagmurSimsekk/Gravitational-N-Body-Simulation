from . import constants
from . import integrator
from . import model
'''
Class to simulate data using integrator and timesteps
'''


class SystemSimulator():
    def __init__(self, integrator: integrator.Integrator):
        self.integrator = integrator        

    def simulate(self) -> list[model.SimulationData]:             
        outputs  = []
        for t in constants.timeline:
            y =  self.integrator.step(t)
            outputs.append(y)

        return outputs

