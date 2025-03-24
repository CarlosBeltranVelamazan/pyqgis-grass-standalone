from qgis.core import *
import processing

# Initialize QGIS
qgs = QgsApplication([], False)
qgs.initQgis()

# Load processing algorithms
from processing.core.Processing import Processing
Processing.initialize()
QgsApplication.processingRegistry().providerById('grass').loadAlgorithms()

# Check if GRASS provider is available
providers = [p.id() for p in QgsApplication.processingRegistry().providers()]
if 'grass' not in providers:
    raise RuntimeError("GRASS provider is not loaded.")

# List all available algorithms in the processing registry
algorithms = QgsApplication.processingRegistry().algorithms()
available_algorithms = [alg.id() for alg in algorithms]
print("Available algorithms:", available_algorithms)

# Load the DEM raster
raster_path = r'test/test_DEM.tif'
raster_layer = QgsRasterLayer(raster_path, 'Elevation DEM')
if not raster_layer.isValid():
    raise FileNotFoundError(f"Raster could not be loaded. Check the file path: {raster_path}")

print(f"Raster loaded successfully. CRS: {raster_layer.crs().authid()}")

# Define output paths for slope and aspect
slope_raster = r'test/slope.tif'
aspect_raster = r'test/aspect.tif'

# Compute slope and aspect using r.slope.aspect
processing.run('grass:r.slope.aspect', {
    'elevation': raster_path,
    'slope': slope_raster,
    'aspect': aspect_raster
})

print(f"Slope raster saved at: {slope_raster}")
print(f"Aspect raster saved at: {aspect_raster}")
print("Processing completed")

# Close QGIS session
qgs.exitQgis()
