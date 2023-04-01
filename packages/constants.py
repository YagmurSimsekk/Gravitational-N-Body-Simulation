#Pyhsical constants
import numpy as np
from math import pi

au_d = 149597870700 #astronomical units [m]
au_m = 10**24 #astronomical mass [kg]
au_t = 86400 #astronomical time - 1 day [s]
G = -6.6743*(10**-11) #gravitational constants in SI units
#G = G*(au_d**-3)*(au_m**1)*(au_t**2) #gravitational constants in units for this system


m_sun = 1988500*(10**24) #mass of the sun
m_earth = 59724*(10**24) #mass of the earth
light_year = 94607 * (10**15) 

##Galaxy system for Galpy
parsec_distance = 1.08 * 10e19 #metre is equal to 1 parsec
solar_mass = 1.989 * 10e30 #kilogram is equal to one SM
Gyr_time = 3.15 * 10e7 #seconds is equal 1 gregorian year

#Hence after convertion our Gravitational constant is
#G = G * (parsec_distance ** -3) * (solar_mass ** 1) * (Gyr_time ** 2)

steps=10000
timeline = np.linspace(0,1000, steps)   # take linespace timeline for smaller dt's
#timeline = range(0, steps, 1)          # take range timeline for integer dt's
dt = timeline[1] - timeline[0]
bodies = 30

