#!/usr/bin/env conda run -n MTP python3
# =============================================================================
# Created By  : Athul Jyothis
# Created Date: 11-09-2021 23:32:21
# =============================================================================
"""
The module has been build for croping given raster file in input_raster folder using a given raster/vector file as reference
"""

import os
from pathlib import Path
import csv
import grass.script as gs
from datetime import datetime as d
# change directory because the file is usually imported to grass gis
os.chdir(os.path.dirname(__file__))

clipRef = 'data/reference/clipRef.gpkg'
gs.run_command('v.import', input=clipRef ,output='clipRef', overwrite=True)
# limit computational region
gs.run_command('r.mask' ,vect='clipRef')

files = Path('data/input_raster').glob('*.tif')
for file in files:
    inputFileInfo = os.path.basename(file).split('_')
    print(inputFileInfo)
    date = inputFileInfo[1]
    time = inputFileInfo[2]
    # gs.run_command('r.in.gdal', input=file,output='input_raster', overwrite=True)
    # gs.run_command('r.mapcalc' ,ex='clipped_raster = input_raster')


