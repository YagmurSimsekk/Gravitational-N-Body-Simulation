from matplotlib import animation, pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""

    def __init__(self, ndata):

        # intialize data
        self.data = ndata
        self.s = abs(self.data[0].sizes)/100
        self.c = self.data[0].colors
        self.ttl_en = self.data[0].total_energy


        # array for plotting orbits, saving old position points
        '''
        Reusing data object and above variables to find shape of old positions array => self.old_positions = np.array((#bodies, #dimensions, #timesteps))
        #bodies = self.data[0].positions.shape[0] , # dimensions = self.data[0].positions.shape[1] #total_steps =  len(ndata) 
        '''
        self.old_positions = np.zeros((self.data[0].positions.shape[0], self.data[0].positions.shape[1], len(ndata)))
        self.old_positions[:,:,0] = self.data[0].positions

        # Setup the figure and axes...
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')


        # Set up Plot Styles
        self.set_styles()

        # Then setup FuncAnimation.     
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=np.arange(0,len(ndata),500), interval=5,
                                           init_func=self.setup_plot, blit=False)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""

        self.scat = self.ax.scatter(self.data[0].positions[:, 0], self.data[0].positions[:, 1],
                                    self.data[0].positions[:, 2], s=self.s, c=self.c,depthshade=False,alpha=0.5)
        return self.scat,

    def update(self, i):
        """Update the scatter plot."""
        #remove old data
        self.scat.remove()

        #set new data
        c_data = self.data[i]
        self.old_positions[:,:,i] = self.data[i].positions #old positions
        
        #plot new points
        self.scat = self.ax.scatter(c_data.positions[:, 0], c_data.positions[:, 1], c_data.positions[:, 2], s=self.s, c=self.c, depthshade=False,alpha=0.5)
        #plot the total energy
        self.fig.suptitle(t = 'Total Energy of the System: %.2f' % c_data.total_energy, fontweight="bold", color = "black", fontsize=10,va = 'top')
        
        #plot trailing orbits
        xp = self.old_positions[:, 0, i]
        yp = self.old_positions[:, 1, i]
        zp = self.old_positions[:, 2, i]

        self.ax.scatter(xp, yp, zp, s=0.01, color = 'black')

        plt.pause(0.0001)
        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

    def set_styles(self):

        # figure styles
        self.fig.set_size_inches(10, 10)
        # self.ax.set_facecolor('black')
        # self.ax.w_xaxis.set_pane_color('black')
        # self.ax.w_yaxis.set_pane_color('black')
        # self.ax.w_zaxis.set_pane_color('black')

        #self.ax.grid(0)
        # self.ax.xaxis.label.set_color('white')
        # self.ax.yaxis.label.set_color('white')
        # self.ax.zaxis.label.set_color('white')
        # self.ax.tick_params(axis='x', colors='white')
        # self.ax.tick_params(axis='y', colors='white')
        # self.ax.tick_params(axis='z', colors='white')

        self.ax.set_xlabel('X', fontsize=15)
        self.ax.set_ylabel('Y', fontsize=15)
        self.ax.set_zlabel('Z', fontsize=15, rotation=0)

        # self.ax.set_xlim(-100, 100)
        # self.ax.set_ylim(-100, 120)
        # self.ax.set_zlim(-2, 3)

        # set the angle for the 3D grid view
        #self.ax.view_init(90, -90)
        
    def get_limits(self):
        limits = []
        for i in range(len(self.data)):
            for j in range(3):
                limits.append(max(self.data[i].positions[j-1]))
                limits.append(min(self.data[i].positions[j-1]))

        return [max(limits), min(limits)]
