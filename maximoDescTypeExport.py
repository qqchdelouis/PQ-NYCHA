# user/bin/env python3
# -*- coding: utf-8 -*-
# maximoDescTypeExport.py - Rechercher et écrire les types de description. 
# Ce module est basé sur maximoDescTypeFinder.py qui n'a pas fonctionné.

from pandas import read_csv
import pandas as pd
import os

os.chdir(r'/Applications/nychatest/FR2/Maximo/wo')


# There are three (3) processed child files of the parent Work Order Maximo file.
woFileA      = 'woFrameA.csv'
woFileB      = 'woFrameB.csv'
woFileC      = 'woFrameC.csv'

searchLead   = ['Lead', 'lead']
searchAsbes  = ['Asbestos', 'asbestos']
searchMold   = ['Mold', 'mold']
searchMildew = ['Mildew', 'mildew']

# Process each commapass file.
print('Beginning to read files in Pandas.')

# Process dataframe A.
print('Reading Frame A, searching for masks.')
dfA          = pd.read_csv(woFileA, dtype=str)
maskALead    = dfA['DESCRIPTION'].isin(searchLead)
maskAAsbes   = dfA['DESCRIPTION'].isin(searchAsbes)
maskAMold    = dfA['DESCRIPTION'].isin(searchMold)
MaskAMildew  = dfA['DESCRIPTION'].isin(searchMildew)
print('Forming mask frames.')
maskALead    = dfA[maskALead]
maskAAsbes   = dfA[maskAAsbes]
maskAMold    = dfA[maskAMold]
MaskAMildew  = dfA[MaskAMildew]
print('Deleting frame A to save on RAM.')
del dfA

# Process dataframe B.
print('Reading Frame B, searching for masks.')
dfB          = pd.read_csv(woFileB, dtype=str)
maskBLead    = dfB['DESCRIPTION'].isin(searchLead)
maskBAsbes   = dfB['DESCRIPTION'].isin(searchAsbes)
maskBMold    = dfB['DESCRIPTION'].isin(searchMold)
MaskBMildew  = dfB['DESCRIPTION'].isin(searchMildew)
print('Forming mask frames.')
maskBLead    = dfB[maskBLead]
maskBAsbes   = dfB[maskBAsbes]
maskBMold    = dfB[maskBMold]
MaskBMildew  = dfB[MaskBMildew]
print('Deleting frame B to save on RAM.')
del dfB

# Process dataframe C and prepare exports.
print('Reading Frame C, searching for masks.')
dfC          = pd.read_csv(woFileC, dtype=str)
maskCLead    = dfC['DESCRIPTION'].isin(searchLead)
maskCAsbes   = dfC['DESCRIPTION'].isin(searchAsbes)
maskCMold    = dfC['DESCRIPTION'].isin(searchMold)
MaskCMildew  = dfC['DESCRIPTION'].isin(searchMildew)
print('Forming mask frames, concating mask frames, and exporting frames to Excel files.')
maskCLead    = dfC[maskCLead]
framesLead   = [maskALead, maskBLead, maskCLead]
dfLead       = pd.concat(framesLead)
pd.DataFrame(dfLead).to_excel('dfLeadMaximo.xlsx', index=True)
maskCAsbes   = dfC[maskCAsbes]
framesAsbes  = [maskAAsbes, maskBAsbes, maskCAsbes]
dfAsbes      = pd.concat(framesAsbes)
pd.DataFrame(dfAsbes).to_excel('dfAsbesMaximo.xlsx', index=True)
maskCMold    = dfC[maskCMold]
framesMold   = [maskAMold, maskBMold, maskCMold]
dfMold       = pd.concat(framesMold)
pd.DataFrame(dfMold).to_excel('dfMoldMaximo.xlsx', index=True)
MaskCMildew  = dfC[MaskCMildew]
framesMildew = [MaskAMildew, MaskBMildew, MaskCMildew]
dfMildew     = pd.concat(framesMildew)
pd.DataFrame(dfMildew).to_excel('dfMildewMaximo.xlsx', index=True)
print('Deleting frame C to save on RAM.')
del dfC

print('Done.')