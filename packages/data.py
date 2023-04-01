from astroquery.jplhorizons import Horizons
import pandas as pd
import numpy as np
import random

'''
Function to extract information about sun, planets and their moons in Solar System
The function outputs data frame including the body name, mass, sizes, positions(x,y,z), velocities(x,y,z) and the color assigned to a body.
The units are all given in AU.
The data provided by using NASA Horizons API.

'''

#30 bodies
def nasadata_func():
    bodies = ['10', '199', '299', '399', '499', '599','699', '799', '899', '999', '301', '401', '402', '503', '504', '501', '502', '606', '605', '608', '604', '603','703', '704', '702', '701', '801', '808', '802', '901' ]

    # masses in [10^^24 kg]
    masses = [1988500,0.3302,4.8685,5.97219,0.64171,1898, 568, 86.8, 102, 0.0130, 0.07346, 1.08E-08, 2.0E-09, 14819000E-08, 10759000E-08, 8931900E-08, 4799800E-08, 134520000E-09, 2306518E-09, 1805635E-09, 1122.8E-09, 1062.2E-09, 340000E-08, 307600E-08,1169.4E-08, 1157.8E-08, 2139000E-08, 3900E-08, 2400E-08, 158.7E-05 ]

    #radius in [km]
    sizes = [695700.0 ,2440.0 , 6051.84,6371.01,3389.92, 69911, 58232, 25362, 24622, 1188.3, 1737.5, 11.1, 6.2, 2634.1, 2410.3, 1821.6, 1560.8, 2574.73, 763.8, 735.6, 561.7, 533.0, 788.9, 761.4, 584.7, 578.9, 1353.4, 210, 170, 606.0]
    
    col = random.sample(range(1,254), 29) 
    col.insert(0, 255)
    
    cols = ['name','x', 'y', 'z', 'vx', 'vy', 'vz']

    df = pd.DataFrame(columns = cols)

    for i in bodies:
        eros = Horizons(id= i, 
            epochs={'start': '2017-01-01',
                    'stop': '2017-01-02',
                    'step': '1d'})
        vecs = eros.vectors()
        vec = vecs[0]
        name = vec[0]
        row1 = pd.Series([name, vec['x'], vec['y'], vec['z'],vec['vx'],vec['vy'],vec['vz']], index= df.columns) #positions and velocities in [au] and [au/day]
        df = df.append(row1, ignore_index = True)
    
    df.insert(1, "mass", masses)
    df.insert(2, "size", sizes)
    df.insert(3, "color", col)

    return df

