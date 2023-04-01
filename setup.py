from setuptools import setup, find_packages
import setuptools



setup(name='Nbody',
      version='1.0.0',
      description='Simulation N-Body at FU Berlin University',
      author='NBody Group',
      author_email='f.tavakkoli@fu-berlin.de',
      url='https://www.python.org/sigs/distutils-sig/',
      packages = find_packages( where="packages",include=['packages'], exclude=['data', 'tests']),
    # packages = setuptools.find_packages(include=['packages',]),
      package_dir = {'': 'packages'},
      py_modules = ['animate', 'integrator',"constants","data", "filehandler", "initial_data", "integrator", "simulation"],
      include_package_data=True,
     )





# setup(...,
#       packages=['packages'],
#       package_dir={'packages': 'packages'},
#       package_data={'data': ['data']},
#       )

# data_files=[('data', ['data/'])],

