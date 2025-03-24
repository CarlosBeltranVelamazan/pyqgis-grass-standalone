# PyQGIS with GRASS GIS Standalone Script Executer

An easy way to install and use pyQGIS with GRASS GIS without the QGIS GUI.
Standalone PyQGIS application that is able to run a custom script, in this case `Proximity.py` without the need of a GUI. Also we don't need to set all kinds of environment variables using a batch file: just launch the VS Code project, and off you go. This was created for Windows.

# Installation

First get `OSGeo4W LTR` by running `install/qgis_deploy_install_upgrade_ltr.ps1` from PowerShell console with administrative rights. Ensure to fetch QGIS LTR. This script will automatically download and install `OSGeo4W`. You can obviously do this manually as well. Just ensure you get QGIS LTR and the _full_ installation. Also ensure to install everything in `C:/OSGeo4W`. If not, change the paths in `.env` and `.settings.json`, see below.

## Access Rights

If the script is failing because of accessrights, you need to temporarily bypass the ExecutionPolicy

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

# Verify `.env`

Open up `.env` in the root folder and verify that following settings match your installation:

```
OSGEO4W_ROOT=C:/OSGeo4W
QGIS_CONFIG=qgis-ltr
PYTHON_VERSION=Python312
GISBASE=${OSGEO4W_ROOT}/apps/grass/grass84
```

# Verify `settings.json`

Open up `.vscode/settings.json` and verify that the path in `python.defaultInterpreterPath` exists. If it doesn't, update it to match your configuration. You probably need to update `PYTHON_VERSION` in `.env` as well.

# Run example

To test if everything is correctly set up, you can run main.py either from a virtual environment or using the Run and Debug feature with launch.json. main.py includes a built-in verification to ensure that GRASS GIS is properly installed. It also runs a set of QGIS and GRASS tools to test whether the algorithms are functioning as expected. This test uses a TIF file from the test folder as input and generates several output files.

# Credits

Credits to MarByteBeep, https://github.com/MarByteBeep/pyqgis-standalone. This code is an updated version that resolves several path-related issues and modifies the scope of main.py to work with GRASS GIS. Creidts to isogeo: https://github.com/isogeo/isogeo-plugin-qgis/blob/master/.vscode/settings.json. The original work was based on this repository.

# Wishful thinking

It would be great if the QGIS team at one point in the future, would integrate all this in their API/SDK to make this whole process seamless :)
