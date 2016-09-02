#!/bin/bash

# Setup the repository for class:
# * Clean the repo of previous student changes
# * Pull in the latest changes from github
# * Activate the conda enviroment
# * Update our Fatiando a Terra development version
# * Start Jupyter

# Reset the repository by discarting all changes and pulling the latest commits
# from Github

echo "Discarding local changes to the repository..."
git reset HEAD .
git checkout -- .

# Erase the HDF5 caches of previous simulations
echo "Removing old simulation cache files..."
find . -name "*.h5" -exec rm -v {} \;

echo "Fetching latest changes from Github..."
git checkout master
git pull origin master

# Activate the environment
echo "Activating conda environment..."
source activate geofisica2

# Update Fatiando
echo "Updating Fatiando a Terra..."
pip install --upgrade https://github.com/fatiando/fatiando/archive/wavefd.zip

# Start Jupyter
echo "Start the notebook server..."
jupyter notebook
