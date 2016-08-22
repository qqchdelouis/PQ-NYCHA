# user/bin/env python3
# -*- coding: utf-8 -*-
# text2csvNYCHApandas.py - Import text from a .txt file and export to CSV. 

from pandas import read_csv
import pandas as pd
import csv, os

os.chdir(r'/Applications/nychatest/FR2/Asbestos')

def csvConvert():
	with open('ZZASBESTOS.txt') as infile, open(
		'ZZASBESTOS.csv', 'w', newline='') as outfile:
		writer = csv.writer(outfile)
		for row in csv.reader(infile):
			writer.writerow(row)
	outfile.close()

# Import .txt file and convert to .csv (for files under 1 GB).
csvConvert()

# Begin section here for analysis of .csv file for asbestos.
Location = r'/Applications/nychatest/FR2/Asbestos/ZZASBESTOS.csv'
df = pd.read_csv(Location, delimiter=' *, *', engine='python')
df = df[df.ZZASBITEM != '---------------------------------------']

# Calculate total positive asbestos results.
asbesMask = df[df['ZZASBTESTRESULT'] == 'POSITIVE']

# Calculate entries subtotal by borough.
allBoroughDistr = df['SITEID'].value_counts()

# Calculate sum of all entries on dataframe.
allBoroughTotal = allBoroughDistr.sum()

# Calculate positive asbestos results by borough.
asbesBoroughDistr = asbesMask['SITEID'].value_counts()

# Calculate sum of all positive asbestos results.
asbesBoroughTotal = asbesBoroughDistr.sum()

# Calculate rate of positive test results.
asbesPozRate = len(asbesMask['ZZASBESTOSID']) / len(df['ZZASBESTOSID'])

# Begin reporting results.
print('The total number of asbestos tests conducted by borough is :')
print(allBoroughDistr)
print('')
print('The total number of asbestos tests conducted is :')
print(allBoroughTotal)
print('')
print('The reporting of asbestos is distributed across the boroughs as follows :')
print(asbesBoroughDistr)
print('')
print('The total number of positive asbestos tests is :')
print(asbesBoroughTotal)
print('')
print('Overall, asbestos tests were reported as positive at this rate,')
print('compared with total asbestos records :')
print(str(round(asbesPozRate * 100, 2)) + '%')
print('')
print('Done.')