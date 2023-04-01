# Gravitational N Body
Gravitational N-Body Simulation using Symplectic Integrator

## Description
This is a python project to simulate N-body systems under influence of Gravitation force between them.
The project has modules for simulation of 2-body, 3-body, Solar System and scientifically modelled system.

Nasa data is obtained from the Horizons website using their APIs https://ssd.jpl.nasa.gov/horizons/
Galaxy data is created with Galpy module https://docs.galpy.org/en/v1.8.1/index.html


## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection. 

- Install requirements from requirements.txt
```
pip install -r requirements.txt 
```
<!-- ``` -->


### Install Project Using setup.py

The strucure of the project shown in following:
```
/path/to/Gravitational-N-Body/project/
├── package/                        Source dir.
│   └── modules.py                  Example module.
│   ├── __init__.py                 This makes the directory a package.
│   └── example_module.py       
├── main.py
├── test/                         
├── README.md                       README with info of the project.
└── setup.py                        Configuration details of the python package.
```

To install the project as a module, you can run this command line in the directory in which setup.py arise:

```commandline
pip install setup.py
```

## Test and Deploy

The built-in continuous integration in GitLab is configured for the project. Every merge request or commit will trigger the pipeline for running the unit test cases. https://git.imp.fu-berlin.de/cs2022/project-1/Gravitational-N-Body/-/pipelines 

Locally the test cases can be run by navigating to the cloned project folder and installing the dependencies using pip-install

```
cd GRAVITATIONAL-N-BODY
pip install -r requirements.txt
pytest 
```

