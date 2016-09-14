# user/bin/env python3
# -*- coding: utf-8 -*-
# filterExcessCommasCSV.py - Weed out lines of TXT or CSV files 
# that have excess commas. 
# 
# Copyright 2016 Progress Queens, Inc. (CC BY 4.0)
# You are free to share and adapt, provided you provide attribution and
# make no additional restrictions to its use. For notices and other
# information, visit : http://creativecommons.org/licenses/by/4.0/

from pandas import read_csv
import pandas as pd
import csv, fileinput, os, sys

os.chdir(r'/Applications/nychatest/FR2/delimitErrors')

# Separate good rows that have X fields (number of commas) into pass file, 
# and then dump bad rows into not pass file.
def searchCommas():
    noOfCommas = 12                              # max number of columns
    with open(fileName) as infile, open(outPassFile, 'w') as passFile, open(
    outNotPassFile, 'w') as notPassFile:
        fileReadlines = infile.readlines()
        for i in range(len(fileReadlines)):
            # We have to subtract one comma here, bc csv does not count the last comma.
            if fileReadlines[i].count(",") == noOfCommas - 1:
                passwriter = csv.writer(passFile)
                passwriter.writerow([fileReadlines[i]])
            else:
                notPasswriter = csv.writer(notPassFile)
                notPasswriter.writerow([fileReadlines[i]])

# Wrapping fileReadlines[i] around brackets in writerow adds double quotes at 
# the beginning and at the end of each line. We need to remove those double quotes.
def cleanupQuotes():
    with fileinput.FileInput(outPassFile, inplace=True, backup='.bak') as file:
        for line in file:
            # Need to skip over blank lines.
            cleanLine = line.replace('\"', '')
            if cleanLine.strip() == '':
                continue
            print(cleanLine, end='')
    with fileinput.FileInput(outNotPassFile, inplace=True, backup='.bak') as file:
        for line in file:
            # Need to skip over blank lines.
            cleanLine = line.replace('\"', '')
            if cleanLine.strip() == '':
                continue
            print(cleanLine, end='')       

fileName = sys.argv[1]
outPassFile = 'commaPassTest.txt'
outNotPassFile = 'commaNotPassText.txt'

if __name__ == '__main__':
    searchCommas()
    cleanupQuotes()
    print('Done.')
