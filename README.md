# Gravitational N Body
Gravitational N-Body Simulation using Symplectic Integrator

## Description
This is a python project to simulate N-body systems under influence of Gravitation force between them.
The project has modules for simulation of 2-body, 3-body, Solar System and scientifically modelled system.

Nasa data is obtained from the Horizons website using their APIs https://ssd.jpl.nasa.gov/horizons/
Galaxy data is created with Galpy module https://docs.galpy.org/en/v1.8.1/index.html


## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection. To use and modify this project, we would recommend to so these steps:


### Clone the Repository

```
git clone https://git.imp.fu-berlin.de/cs2022/project-1/Gravitational-N-Body.git
git checkout main
git status
```



<!-- I would recommend to install a new environment and setup all dependencies. So, you can read the following instruction:
- Install virtual environment using:
```
pip install virtualenv
```
- Create a virtual environment  and activate it using:
```
virtualenv nbody
source nbody/bin/activate
```
- Install requirements from requirements.txt
```
pip install -r requirements.txt -->
<!-- ``` -->

### Clone from GitLab
Use this command line to add the project to your local system, either by url:
```commandline
git clone https://git.imp.fu-berlin.de/cs2022/project-1/Gravitational-N-Body.git
```
or by SSH Key:
```commandline
git clone git@git.imp.fu-berlin.de:cs2022/project-1/Gravitational-N-Body.git
```

Using SSH Key command requires creating an ssh key, which added to your GitLab account ([Stup SSH key](https://docs.gitlab.com/ee/ssh/)).
SSH key make interacion with repository easier bacause you do not need to wite your username and password each time.


### Setup Environment
After cloning the repository, you need to setup an environment to install all needed packages and libraries. The steps of setting an environment are as follows:
In this case, we call the environment "n-body"

-In Python

1. `pip install virtualenv`
2. `virtualenv n-body`
3. `source n-body/bin/activate`
4. `pip install -r requirements.txt`

-In conda:

1. `conda create -n n-body`
2. `conda activate n-body`
3. `pip install -r requirements.txt`


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

## References
https://git.imp.fu-berlin.de/cs2022/project-1/Gravitational-N-Body/-/wikis/Useful-Links

