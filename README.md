# HamlinLab Jupyter Lab Template

## Purpose
Quick start for setting up a Jupyterlab project.

## Quick start
To get things running the first time:
1. Follow [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) in order to create a new github repository from the template. 
2. Go to your terminal and clone the new repository (use your username and the correct repository name):

        git clone git@github.com:your_user_name/new_repository_name.git
        
3. Change directory into the newly created directory:

        cd new_repository_name

4. Install the environment.  Replace new_repository_name with the name of the repository you just chose.  Installation may take several minutes and require GB or more of space):

        conda env create -n new_repository_name-env -f environment.yml

5. Activate the new environment:

        conda activate new_repository_name-env

6. Install the example packages in developer mode:

        pip install -e ./

7. Start up jupyter-lab:

        jupyter-lab &

8. You can open the `notebooks/01_quick_start.ipynb` notebook to get started.

## How to use

### Directory structure
The folder uses the following directory structure:
```
├── data
│   ├── external <- data from other sources such as publications by other authors
│   ├── processed <- data that has been processed in any way after collecting
│   └── raw <- completely raw unprocessed data
├── environment.yml <- which packages to install when making the environment
├── hamlin_lab <- place you modules in here
│   ├── example.py <- an example module
│   └── __init.py__ <- ignore me unless you know what you are doing.
├── notebooks
│   └── 01_quick_start.ipynb <- notebooks go here, named with numerical prefixes
├── publication_ready <- publication ready figures and tables go here.
├── README.md <- This readme file.
└── setup.py <- some instructions related to setting up the modules
```
I've left out some files and directories that you can ignore.
