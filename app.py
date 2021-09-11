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


files = Path('data/input_raster').glob('*.tif')
for file in files:
    gs.run_command('r.in.gdal', input=file,
                    output='DEM', overwrite=True)
        


