#!/bin/bash

# Setup the repository for class:
# * Clean the repo of previous student changes
# * Pull in the latest changes from github
# * Activate the conda enviroment
# * Update our Fatiando a Terra development version
# * Start Jupyter

# Reset the repository by discarting all changes and pulling the latest commits
# from Github
git reset HEAD .
git checkout -- .
# Erase the HDF5 caches of previous simulations
find . -name "*.h5" -exec rm -v {} \;
git checkout master
git pull origin master

# Activate the environment
source activate geofisica2

# Update Fatiando
pip install --upgrade https://github.com/fatiando/fatiando/archive/wavefd.zip

# Start Jupyter
jupyter notebook
