#!/usr/bin/env python3
# =============================================================================
# Created By  : Athul Jyothis
# Created Date: 11-09-2021 23:32:21
# =============================================================================
"""
The module has been build for batch finding statistics of raster and saving it to a csv file
"""
import os
from pathlib import Path
import csv
import grass.script as gs
from datetime import datetime as d
# change directory because the file is usually imported to grass gis
os.chdir('/home/jyothisable/P.A.R.A/1.Projects/mtp/Softwares/VS code/Batch_Stats_Raster')

def saveOutput(inputFileName,fileNameInGrass):
    '''
    input input file name and output file name
    save current output file as .tif in output folder and also append statistics of this file to a .csv file 
    '''
    # output results stats into CSV (can't append directly)
    gs.run_command('r.univar', map=fileNameInGrass,
                    output='data/cache/stats_cache.csv', 
                    separator='comma', 
                    overwrite=True, 
                    flags='te')
    # read the last lines from cache file
    with open('data/cache/stats_cache.csv', newline='') as cache_csv:
        lastLine = cache_csv.read().splitlines()[-1]
    # append it to permanent file
    with open('data/output/stats.csv', 'a') as output_csv:
        # save header initially
        if os.stat('data/output/stats.csv').st_size == 0:
            output_csv.writelines(
                'day,time(UTC),non_null_cells,null_cells,min,max,range,mean,mean_of_abs,stddev,variance,coeff_var,sum,sum_abs,first_quart,median,third_quart,perc_90')
        output_csv.write("\n")
        output_csv.writelines(str(day)+','+str(time)+','+lastLine)


files = Path('data/input_raster').glob('*.tif')
for file in files:
    inputFileInfo = os.path.basename(file).split('_')
    date = inputFileInfo[3]
    day = date[:2]
    time = inputFileInfo[4]
    gs.run_command('r.in.gdal', input=file,output='solar_ins', flags='o' ,overwrite=True)
    saveOutput(os.path.basename(file),'solar_ins')




