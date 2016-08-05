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

print('Ascribing stats for NYCHA service requests per CSV file with and without work order.')
print('The stats for mold- and mildew-related service requests')
print('will be made, according to public housing development and borough.')
print(' ')

# Section for Mold and Mildew searches and counts

def molddef():
    walls = 'Walls - Mildew Mold'
    ceiling = 'Ceiling - Mildew Mold'
    global maskmold
    maskmold = df['DESCRIPTION'].isin([walls, ceiling])
    global dfmold
    dfmold = df[maskmold]
    

def mildewdef():
    mildew = 'Mildew - '
    mildewc = 'Mildew Condition - '
    mildewcm = 'Mildew Condition - Mildew'
    mildewcnc = 'Mildew Condition - Needs Cleaning'
    mildewcnp = 'Mildew Condition - Needs Painting'
    mildewcpar = 'Mildew Condition - Paint After Repair'
    mildewcv = 'Mildew Condition - Vent OOO'
    global maskmildew
    maskmildew = df['DESCRIPTION'].isin([mildew, mildewc, mildewcm,
        mildewcnc, mildewcnp, mildewcpar, mildewcv])
    global dfmildew
    dfmildew = df[maskmildew]
    
# define location of CSV file to be searched and define TDS field.

import os
os.chdir('/Applications/nychatest')
Location = r'/Applications/nychatest/sr_withandwithout_workorder.csv'
df = pd.read_csv(Location)
df['TDS_ID'] = df.LOCATION_ID.str[:3]

# Set up lookup table and Borough field.

tdsfile = r'/Applications/nychatest/NYCHATDSManual.xlsx'
tdslut = pd.ExcelFile(tdsfile)
tdslut = tdslut.parse("Sheet1")
tdslut['TDS'] = tdslut['TDS'].apply(lambda x: '{0:0>5}'.format(x))
tdslut['TDS_ID'] = tdslut.TDS.str[:3]
df['SITE_NAME'] = df.TDS_ID.map(tdslut.set_index('TDS_ID')['COMPLEX'])
df['BOROUGH'] = df.TDS_ID.map(tdslut.set_index('TDS_ID')['BOROUGH'])

molddef()
mildewdef()

# Section exporting mold search by site, borough

trssitemold = dfmold.groupby(['BOROUGH', 'SITE_NAME']).size()
pd.DataFrame(trssitemold).to_excel('TDSmoldsiteoutput.xlsx', index=True)
trsbormold = dfmold.groupby(['BOROUGH']).size()
pd.DataFrame(trsbormold).to_excel('TDSmoldboroutput.xlsx', index=True)

# Section exporting mildew search by site, borough

trssitemildew = dfmildew.groupby(['BOROUGH', 'SITE_NAME']).size()
pd.DataFrame(trssitemildew).to_excel('TDSmildewsiteoutput.xlsx', index=True)
trsbormildew = dfmildew.groupby(['BOROUGH']).size()
pd.DataFrame(trsbormildew).to_excel('TDSmildewboroutput.xlsx', index=True)

# Finish
print('Mold results have been printed.')
print('Mildew search by site has been exported to : TDSmoldsiteoutput.xlsx')
print('Mildew search by borough has been exported to : TDSmoldboroutput.xlsx')
print('')
print('Mildew results have been printed.')
print('Mildew search by site has been exported to : TDSmildewsiteoutput.xlsx')
print('Mildew search by borough has been exported to : TDSmildewboroutput.xlsx')
print('Done !')