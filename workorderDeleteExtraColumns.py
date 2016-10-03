# user/bin/env python3
# -*- coding: utf-8 -*-
# workorderDeleteExtraColumns.py - Supprimer les colonnes inutiles. 

from pandas import read_csv
import pandas as pd
import csv, os

os.chdir(r'/Applications/nychatest/FR2/Maximo/wo')

# NOTE --------------------------------------------------------------------
# NOTE :  Extra header rows will need to be removed from wo102 - wo602.
# NOTE --------------------------------------------------------------------

measureColumns1 = ['ESTMATCOST', 'ESTTOOLCOST', 'ACTTOOLCOST', 'OUTLABCOST', 
                   'OUTMATCOST', 'OUTTOOLCOST', 'CONTRACT', 'CALENDAR', 'DOWNTIME', 
                   'CREWID', 'WOLABLNK', 'ASSETLOCPRIORITY', 'CHARGESTORE', 'GLACCOUNT', 
                   'ESTSERVCOST', 'ACTSERVCOST', 'DISABLED', 'ESTATAPPRMATCOST', 
                   'ESTATAPPRTOOLCOST', 'ESTATAPPRSERVCOST', 'OWNERSYSID', 'WORKLOCATION', 
                   'EXTERNALRE', 'FINCNTRL', 'GENERATE', 'GENFORPOLINEID']
 
measureColumns2 = ['MEASUREMENTVALUE', 'OBSERVAT', 'POINTNUM', 'VENDOR', 'RISK', 
                  'ENVIRONMENT', 'BACKOUTPLAN', 'COMMODIT', 'WHOMISCHANGEFOR', 
                  'REASONFORCHANGE', 'VERIFICATION', 'ZZ504RESID', 'ZZED', 'ZZEXTRAFIELD2', 
                  'ZZLAST_IN', 'ZZPACO', 'ZZRESCHARGE', 'ZZSRDESC', 'ZZEPAREGNUM', 'ZZDOS', 
                  'ZZOR', 'ZZTIMEIN', 'ZZTIMEOUT', 'ZZXRFGUN', 'ZZXRFGUN2']
 
measureColumns3 = ['ZZASBSUBSTRATE', 'ZZASBCOMPONENT', 'ZZASBCOLOR', 'ZZASBREQTYPE', 
                   'ZZASBPC', 'ZZASBPCTYPE', 'ZZAS', 'ZZASBSAMPLESIZE', 
                   'ZZASBTESTRESULT', 'ZZASBDATE', 'ZZDUPENDD', 'ZZASBITEM', 'ZZISABATED', 
                   'ZZISTESTED', 'ZZVIABATE', 'ZZMOBILED', 'CINUM', 'FLOWACTION', 
                   'FLOWACTIONASSIST', 'FLOWCONTROLLED', 'LAUNCHENTRYNAME', 'SUSPENDFLOW', 
                   'TARGETDESC', 'WOISSWAP', 'CALCORGI', 'CALCCALE', 'CALCSHIF', 'PMCOMTYPE', 
                   'PMCOMSTATE', 'PMCOMBPELACTNAME', 'PMCOMBPELENABLED', 'PMCOMBPELINPROG']
 
measureColumns4 = ['REPFACSI', 'REPAIRFACILITY', 'GENFORPOREVISION', 'STOREROOMMTLSTATUS', 
                   'DIRISSUEMTLSTATUS', 'WORKPACKMTLSTATUS', 'IGNOREDIAVAIL', 'ESTOUTLABHRS', 
                   'ESTOUTLABCOST', 'ACTOUTLABHRS', 'ACTOUTLABCOST', 'ESTATAPPROUTLABHRS', 
                   'ESTATAPPROUTLABCOST', 'AVAILSTAT', 'NESTEDJPINPROCESS', 'PLUSCISMOBILE', 
                   'PLUSCJPREVNUM', 'PLUSCLOOP', 'PLUSCNEXT', 'PLUSCOVER', 'PLUSCPHYLOC', 
                   'SNECONSTR', 'FNLCONSTR', 'AMCREW', 'CREWWORK', 'REQASSTDWNTIME', 
                   'APPTREQUIRED', 'AOS', 'AMS', 'LOS', 'LMS'] 

# troubleColumns were not deleted.
# troubleColumns = ['COMMODIT', 'ZZASBDATE']

# There are 12 processed child files of the parent Work Order Maximo file.
wo101File = 'wo1commapass-1.txt'
wo102File = 'wo1commapass-2.txt'
wo201File = 'wo2commapass-1.txt'
wo202File = 'wo2commapass-2.txt'
wo301File = 'wo3commapass-1.txt'
wo302File = 'wo3commapass-2.txt'
wo401File = 'wo4commapass-1.txt'
wo402File = 'wo4commapass-2.txt'
wo501File = 'wo5commapass-1.txt'
wo502File = 'wo5commapass-2.txt'
wo601File = 'wo6commapass-1.txt'
wo602File = 'wo6commapass-2.txt'

# Process each commapass file.
print('Beginning to read files in Pandas.')
print('Reading 101.')
wo101df = pd.read_csv(wo101File, dtype=str)
print('Deleting extra columns for 101.')
for field in measureColumns1:
    del wo101df[field]
for field in measureColumns2:
    del wo101df[field]
for field in measureColumns3:
    del wo101df[field]
for field in measureColumns4:
    del wo101df[field]
print('Writing df to directory.')
wo101df.to_csv('wo101df.csv')
print('Deleting df.')
del wo101df

print('Reading 102.')
wo102df = pd.read_csv(wo102File, dtype=str)
print('Deleting extra columns for 102.')
for field in measureColumns1:
    del wo102df[field]
for field in measureColumns2:
    del wo102df[field]
for field in measureColumns3:
    del wo102df[field]
for field in measureColumns4:
    del wo102df[field]
print('Writing df to directory.')
wo102df.to_csv('wo102df.csv')
print('Deleting df.')
del wo102df

print('Reading 201.')
wo201df = pd.read_csv(wo201File, dtype=str)
print('Deleting extra columns for 201.')
for field in measureColumns1:
    del wo201df[field]
for field in measureColumns2:
    del wo201df[field]
for field in measureColumns3:
    del wo201df[field]
for field in measureColumns4:
    del wo201df[field]
print('Writing df to directory.')
wo201df.to_csv('wo201df.csv')
print('Deleting df.')
del wo201df

print('Reading 202.')
wo202df = pd.read_csv(wo202File, dtype=str)
print('Deleting extra columns for 202.')
for field in measureColumns1:
    del wo202df[field]
for field in measureColumns2:
    del wo202df[field]
for field in measureColumns3:
    del wo202df[field]
for field in measureColumns4:
    del wo202df[field]
print('Writing df to directory.')
wo202df.to_csv('wo202df.csv')
print('Deleting df.')
del wo202df

print('Reading 301.')
wo301df = pd.read_csv(wo301File, dtype=str)
print('Deleting extra columns for 301.')
for field in measureColumns1:
    del wo301df[field]
for field in measureColumns2:
    del wo301df[field]
for field in measureColumns3:
    del wo301df[field]
for field in measureColumns4:
    del wo301df[field]
print('Writing df to directory.')
wo301df.to_csv('wo301df.csv')
print('Deleting df.')
del wo301df

print('Reading 302.')
wo302df = pd.read_csv(wo302File, dtype=str)
print('Deleting extra columns for 302.')
for field in measureColumns1:
    del wo302df[field]
for field in measureColumns2:
    del wo302df[field]
for field in measureColumns3:
    del wo302df[field]
for field in measureColumns4:
    del wo302df[field]
print('Writing df to directory.')
wo302df.to_csv('wo302df.csv')
print('Deleting df.')
del wo302df

print('Reading 401.')
wo401df = pd.read_csv(wo401File, dtype=str)
print('Deleting extra columns for 401.')
for field in measureColumns1:
    del wo401df[field]
for field in measureColumns2:
    del wo401df[field]
for field in measureColumns3:
    del wo401df[field]
for field in measureColumns4:
    del wo401df[field]
print('Writing df to directory.')
wo401df.to_csv('wo401df.csv')
print('Deleting df.')
del wo401df

print('Reading 402.')
wo402df = pd.read_csv(wo402File, dtype=str)
print('Deleting extra columns for 402.')
for field in measureColumns1:
    del wo402df[field]
for field in measureColumns2:
    del wo402df[field]
for field in measureColumns3:
    del wo402df[field]
for field in measureColumns4:
    del wo402df[field]
print('Writing df to directory.')
wo402df.to_csv('wo402df.csv')
print('Deleting df.')
del wo402df

print('Reading 501.')
wo501df = pd.read_csv(wo501File, dtype=str)
print('Deleting extra columns for 501.')
for field in measureColumns1:
    del wo501df[field]
for field in measureColumns2:
    del wo501df[field]
for field in measureColumns3:
    del wo501df[field]
for field in measureColumns4:
    del wo501df[field]
print('Writing df to directory.')
wo501df.to_csv('wo501df.csv')
print('Deleting df.')
del wo501df

print('Reading 502.')
wo502df = pd.read_csv(wo502File, dtype=str)
print('Deleting extra columns for 502.')
for field in measureColumns1:
    del wo502df[field]
for field in measureColumns2:
    del wo502df[field]
for field in measureColumns3:
    del wo502df[field]
for field in measureColumns4:
    del wo502df[field]
print('Writing df to directory.')
wo502df.to_csv('wo502df.csv')
print('Deleting df.')
del wo502df

print('Reading 601.')
wo601df = pd.read_csv(wo601File, dtype=str)
print('Deleting extra columns for 601.')
for field in measureColumns1:
    del wo601df[field]
for field in measureColumns2:
    del wo601df[field]
for field in measureColumns3:
    del wo601df[field]
for field in measureColumns4:
    del wo601df[field]
print('Writing df to directory.')
wo601df.to_csv('wo601df.csv')
print('Deleting df.')
del wo601df

print('Reading 602.')
wo602df = pd.read_csv(wo602File, dtype=str)
print('Deleting extra columns for 602.')
for field in measureColumns1:
    del wo602df[field]
for field in measureColumns2:
    del wo602df[field]
for field in measureColumns3:
    del wo602df[field]
for field in measureColumns4:
    del wo602df[field]
print('Writing df to directory.')
wo602df.to_csv('wo602df.csv')
print('Deleting df.')
del wo602df
print('Done.')