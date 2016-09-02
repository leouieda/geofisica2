#!/bin/bash

# Setup the repository for class:
# * Clean the repo of previous student changes
# * Pull in the latest changes from github
# * Activate the conda enviroment
# * Update our Fatiando a Terra development version
# * Start Jupyter

# Reset the repository by discarting all changes and pulling the latest commits
# from Github

echo "Discarding local changes to the repository...\n\n"
git reset HEAD .
git checkout -- .

# Erase the HDF5 caches of previous simulations
echo "\nRemoving old simulation cache files...\n\n"
find . -name "*.h5" -exec rm -v {} \;

echo "\nFetching latest changes from Github...\n\n"
git checkout master
git pull origin master

# Activate the environment
echo "\nActivating conda environment...\n\n"
source activate geofisica2

# Update Fatiando
echo "\nUpdating Fatiando a Terra...\n\n"
pip install --upgrade https://github.com/fatiando/fatiando/archive/wavefd.zip

# Start Jupyter
echo "\nStart the notebook server...\n\n"
jupyter notebook
