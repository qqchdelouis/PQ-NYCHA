# -*- coding: utf-8 -*-
# Copyright 2016 Progress Queens, Inc. (CC BY 4.0)
# You are free to share and adapt, provided you provide attribution and
# make no additional restrictions to its use. For notices and other
# information, visit : http://creativecommons.org/licenses/by/4.0/
#
# LF Comment : NYCHA Module 24 Based on  Module 22. 
#
# noting fieldnames in CSV file
# fieldnames = ['FIRST_NAME', 'LAST_NAME', 'SR_CREATED', 'SR_ID', 'SR_NUM', 
# 'SR_TYPE', 'SR_SUB_TYPE', 'SR_STATUS', 'CONTACT_ID', 'UNIT_ID', 'WORK_ORDER_NUM', 
# 'LOCATION', 'LOCATION_ID', 'DESCRIPTION', 'SCHEDULE_DATE', 'RESP_SCHEDULER', 
# 'PRIORITY', 'STATUS']

# Important note : This module was designed to be in the same cwd as each of
# the CSV file and the TDS Lookup Table.
# So, download the files and correct the directory and Locations of the files.

from pandas import DataFrame, read_csv
import pandas as pd
import sys
import numpy as np

print('Ascribing stats for NYCHA service requests per CSV file with and without work order.')
print('The stats for lead- and mold/mildew-related service requests')
print('will be made, according to public housing development and borough.')
print(' ')

# define location of CSV file to be searched and of lookup table.

import requests
import os
os.chdir('/Applications/nychatest')
# Location = requests.get('https://drive.google.com/folderview?id=0B9G3z0zSlDX1Wkxmc3VCcG9XTjg&usp=drive_web')
Location = r'/Applications/nychatest/sr_withandwithout_workorder.csv'
df = pd.read_csv(Location)
df['TDS_ID'] = df.LOCATION_ID.str[:3]

# Section for Lead and Paint searches and counts

ceiling = 'Ceiling - Lead Paint'
leak = 'Leak From Above - Needs Lead Testing'
wall = 'Walls - Lead Paint'
# need = 'Mildew Condition - Needs Painting'
# paint = 'Mildew Condition - Paint After Repair'
# peel = 'Paint - Peeling'
masklead = df['DESCRIPTION'].isin([ceiling, leak, wall])
df = df[masklead]

# Set up lookup table and filter by location

# tdsfile = requests.get('https://drive.google.com/file/d/0B9EgtfYGBBK9bnMwdmhRWGw5dzQ/view?usp=sharing')
tdsfile = r'/Applications/nychatest/NYCHATDSManual.xlsx'
tdslut = pd.ExcelFile(tdsfile)
tdslut = tdslut.parse("Sheet1")
tdslut['TDS'] = tdslut['TDS'].apply(lambda x: '{0:0>5}'.format(x))
tdslut['TDS_ID'] = tdslut.TDS.str[:3]
df['SITE_NAME'] = df.TDS_ID.map(tdslut.set_index('TDS_ID')['COMPLEX'])
df['BOROUGH'] = df.TDS_ID.map(tdslut.set_index('TDS_ID')['BOROUGH'])

# Section exporting lead search by site

trssite = df.groupby(['BOROUGH', 'SITE_NAME']).size()
pd.DataFrame(trssite).to_excel('TDSleadsiteoutput.xlsx', index=True)

# Section exporting lead search by borough

trsbor = df.groupby(['BOROUGH']).size()
pd.DataFrame(trsbor).to_excel('TDSleadboroutput.xlsx', index=True)

# Finish

print('Lead search by site has been exported to : TDSleadsiteoutput.xlsx')
print('Lead search by borough has been exported to : TDSleadboroutput.xlsx')
print('Done !')