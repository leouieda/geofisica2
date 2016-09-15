clean:
	# Erase the HDF5 caches of previous simulations
	@echo "Removing old simulation cache files..."
	@find . -name "*.h5" -exec rm -v {} \;
