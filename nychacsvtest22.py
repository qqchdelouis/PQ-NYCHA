# -*- coding: utf-8 -*-
# Copyright 2016 Progress Queens, Inc. (CC BY 4.0)
# You are free to share and adapt, provided you provide attribution and
# make no additional restrictions to its use. For notices and other
# information, visit : http://creativecommons.org/licenses/by/4.0/
#
# LF Comment : NYCHA Test Module 22 Based on Jupyter Pandas tutorials. 
#
# noting fieldnames in CSV file
# fieldnames = ['FIRST_NAME', 'LAST_NAME', 'SR_CREATED', 'SR_ID', 'SR_NUM', 
# 'SR_TYPE', 'SR_SUB_TYPE', 'SR_STATUS', 'CONTACT_ID', 'UNIT_ID', 'WORK_ORDER_NUM', 
# 'LOCATION', 'LOCATION_ID', 'DESCRIPTION', 'SCHEDULE_DATE', 'RESP_SCHEDULER', 
# 'PRIORITY', 'STATUS']

# Important note : This module was designed to be in the same cwd as the CSV file.
# So, download both and correct the directory and Location of the CSV file.

from pandas import DataFrame, read_csv
import pandas as pd
import sys
import numpy as np

print('Stats for NYCHA service requests per CSV file with and without work order :')
print(' ')

# define location of CSV file to be searched.

import os
os.chdir('/Applications/nychatest')
Location = r'/Applications/nychatest/sr_withandwithout_workorder.csv'
df = pd.read_csv(Location)

# Section for Paint and Lead searches and counts

ceiling = 'Ceiling - Lead Paint'
leak = 'Leak From Above - Needs Lead Testing'
wall = 'Walls - Lead Paint'
need = 'Mildew Condition - Needs Painting'
paint = 'Mildew Condition - Paint After Repair'
peel = 'Paint - Peeling'

# Section exporting lead search 

masklead = df['DESCRIPTION'].isin([ceiling, leak, wall])
df = df[masklead]
df.to_excel('leadoutput.xlsx', index=False)
print('Lead search results exported to: leadoutput.xlsx')
print(' ')

# Section exporting paint search ; note requires re-reading Location

df = pd.read_csv(Location)
maskpaint = df['DESCRIPTION'].isin([need, paint, peel])
df = df[maskpaint]
df.to_excel('paintoutput.xlsx', index=False)
print('Lead search results exported to: paintoutput.xlsx')
print(' ')

# In case needed, apply date format to SR_CREATED

df = pd.read_csv(Location)
df['SR_CREATED'] = pd.to_datetime(df['SR_CREATED'])

# Here are the counts of each yearly total 

df_firstyear = df[(df.SR_CREATED >= '01/01/2009 00:00:00') & 
    (df.SR_CREATED <= '12/31/2009 23:59:59')]
firstyeartotal = len(df_firstyear['SR_CREATED'])
print('Year 2009 Total : ', firstyeartotal)
df_secondyear = df[(df.SR_CREATED >= '01/01/2010 00:00:00') & 
    (df.SR_CREATED <= '12/31/2010 23:59:59')]
secondyeartotal = len(df_secondyear['SR_CREATED'])
print('Year 2010 Total : ', secondyeartotal)
df_thirdyear = df[(df.SR_CREATED >= '01/01/2011 00:00:00') & 
    (df.SR_CREATED <= '12/31/2011 23:59:59')]
thirdyeartotal = len(df_thirdyear['SR_CREATED'])
print('Year 2011 Total : ', thirdyeartotal)
df_fourthyear = df[(df.SR_CREATED >= '01/01/2012 00:00:00') & 
    (df.SR_CREATED <= '12/31/2012 23:59:59')]
fourthyeartotal = len(df_fourthyear['SR_CREATED'])
print('Year 2012 Total : ', fourthyeartotal)
df_fifthyear = df[(df.SR_CREATED >= '01/01/2013 00:00:00') & 
    (df.SR_CREATED <= '12/31/2013 23:59:59')]
fifthyeartotal = len(df_fifthyear['SR_CREATED'])
print('Year 2013 Total : ', fifthyeartotal)
df_sixthyear = df[(df.SR_CREATED >= '01/01/2014 00:00:00') & 
    (df.SR_CREATED <= '12/31/2014 23:59:59')]
sixthyeartotal = len(df_sixthyear['SR_CREATED'])
print('Year 2014 Total : ', sixthyeartotal)
df_seventhyear = df[(df.SR_CREATED >= '01/01/2015 00:00:00') & 
    (df.SR_CREATED <= '12/31/2015 23:59:59')]
seventhyeartotal = len(df_seventhyear['SR_CREATED'])
print('Year 2015 Total : ', seventhyeartotal)
print(' ')

# Here are the counts for Lead and Paint service requests

df = pd.read_csv(Location)
print('Grand totals of lead-related service requests :')
print(' ')
print('Ceiling - Lead Paint : ', df['DESCRIPTION'].str.contains(ceiling).sum())
print('Leak From Above - Needs Lead Testing : ', df['DESCRIPTION'].str.contains(leak).sum())
print('Walls - Lead Paint : ', df['DESCRIPTION'].str.contains(wall).sum())
print(' ')
print('Grand totals of paint-related service requests :')
print(' ')
print('Mildew Condition - Needs Painting : ', df['DESCRIPTION'].str.contains(need).sum())
print('Mildew Condition - Paint After Repair : ', df['DESCRIPTION'].str.contains(paint).sum())
print('Paint - Peeling : ', df['DESCRIPTION'].str.contains(peel).sum())
print(' ')
print('Done !')
