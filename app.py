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
import grass.script as gs


def saveOutput(fileNameInGrass):
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
    with open('data/output/' + os.path.basename(ref_vector).split('.')[0] + 'stats.csv', 'a') as output_csv:
        # save header initially
        if os.stat('data/output/' + os.path.basename(ref_vector).split('.')[0] + 'stats.csv').st_size == 0:
            output_csv.writelines(
                'day,time(UTC),non_null_cells,null_cells,min,max,range,mean,mean_of_abs,stddev,variance,coeff_var,sum,sum_abs,first_quart,median,third_quart,perc_90')
        output_csv.write("\n")
        output_csv.writelines(str(day)+','+str(time)+','+lastLine)


# change directory because the file is usually imported to grass gis
os.chdir('/home/jyothisable/P.A.R.A/1.Projects/mtp/Softwares/VS code/Batch_Stats_Raster')
files = sorted(os.listdir('data/input_raster'))
ref_vector = 'data/input_vector_mask_m/fid_421.gpkg'
gs.run_command('v.in.ogr',
               input=ref_vector,
               output='ref_vector',
               overwrite=True)
for file in files:
    inputFileInfo = os.path.basename(file).split('_')
    date = inputFileInfo[2]
    day = date[:2]
    time = inputFileInfo[3]
    gs.run_command('r.in.gdal',
                   input='data/input_raster/'+file,
                   output='solar_ins',
                   flags='o',
                   overwrite=True)
    gs.run_command('g.region',
                   vector='ref_vector')
    saveOutput('solar_ins')
