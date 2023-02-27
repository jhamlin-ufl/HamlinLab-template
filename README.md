# HamlinLab Jupyter Lab Template

## Purpose
Quick start for setting up a Jupyterlab project.

## Quickstart

1. If this is the first time you are getting up and running,
first you must [setup git ssh keys](#setting-up-git-ssh-keys) and [install poetry](#install-poetry).
2. Create a new repository from this template.  See github's instuctions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
3. Clone your new repository via:
    ```
    git clone git@github.com:yourGitUsername/yourNewRepositoryName.git
    ```
4. Cd into your new repository:
    ```
    cd yourNewRepositoryName
    ```
5. Create the environment for your new repository using poetry:
    ```
    poetry install
    ```
6. If you are going to use [VS Code](https://code.visualstudio.com/) to work
with the Jupyterlab notebooks, you should launch vs code from the terminal
(after you cd into the project directory) as follows:
    ```
    poetry run code
    ```

## Getting up and running (on linux)

To get up and running on a linux machine, you may have to first do the following:

1. Setup git ssh keys
2. Install poetry

### Setting up git ssh keys

1. You want to be able to use git without having to enter your password every
time.  There are numerous sources on how to do this.  See, e.g.:
[Github's own instuctions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
Note that in the instuction above, when you run the `ssh-keygen` command,
you should leave the username and password blank.

2.  It may help to setup a git configuration in your home directory (`~/.gitconfig`).
The contents can be as follows (enter your correct user name and email).
    ```
    # This is Git's per-user configuration file.
    [user]
    name = yourGitUsername
    email = yourGitEmailAddress
    # Attempt to fix some additional problems
    [url "git@github.com-yourGitUserName:"]
        insteadOf = https://github.com/
    ```

### Install poetry

Poetry is a package manager (somewhat similar to conda).
Full installation instuctions are available [here](https://python-poetry.org/docs/).
On linux you can:

1. Install via:
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
2. After running this command, you probably need to log out and back in.
3. In is helpful to keep your virtual environments inside your project directories,
instead of keeping them all in on global environments folder.  To set poetry to store
environments in the project direcotry, do the following:
    ```
    poetry config virtualenvs.in-project true
    ```
