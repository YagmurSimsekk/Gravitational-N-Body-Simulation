'''
The main method which gets called when the python program is executed
Initial data is simulated with the help of defined integrator
Output is saved as a data file
The data file is used as input for the Visualisation.
'''
from matplotlib import pyplot as plt

import argparse
import packages.constants 
import faulthandler
from packages.simulation import SystemSimulator
from packages.initial_data import DataInitializer
from packages.integrator import PositionVerlet, VelocityVerlet, VerletIntegrator
from packages.animate import AnimatedScatter
from packages.filehandler import NumpyFileHandler

def main():

    # variables
    #set_variables()

    print('Starting Operation')
    # initialize the data , or read from a data file
    # sample sample To be updated when the integration method is available
    initializer = DataInitializer()
    initial_data = initializer.nasaData()

    # initialize integrator object - currently as Verlet, can be updated to other integrator
    integrator = PositionVerlet(initial_data.masses, initial_data.positions,
                                 initial_data.velocities, initial_data.sizes, initial_data.colors)

    # simulate
    faulthandler.enable()

    d_sim = SystemSimulator(integrator=integrator)
    output = d_sim.simulate()

    # save the data to a data file
    #file_handler = NumpyFileHandler('data\_MW_disc_dataset.npy')
    #file_handler.write(output)

    # animate
    # call the animate function using the above saved data file and generate the output
    #output = file_handler.read()
    a = AnimatedScatter(ndata=output)
    plt.show()

    print('Operation completed.')


def set_variables():
    parser = argparse.ArgumentParser()
    # add arguments to the parser
    parser.add_argument("--steps", metavar='S', type=int,
                        help='number of steps for simulation', default=packages.constants.steps)
    parser.add_argument("--bodies", metavar='B', type=int,
                        help='number of bodies for simulation', default=packages.constants.bodies)

    # parse the arguments
    args = parser.parse_args()

    # get the arguments value
    packages.constants.steps = int(args.steps)
    packages.constants.timeline =range(0, packages.constants.steps)
    packages.constants.dt = packages.constants.timeline[1] - packages.onstants.timeline[0]
    packages.constants.bodies = int(args.bodies)

if __name__ == '__main__':
    main()
