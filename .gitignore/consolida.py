
import pandas as pd
import numpy as np
import xlrd
import os, glob, shutil


# Count files
i = 0
for file in glob.glob('./*.*'):
 i = i+1
 #print (f+str(i), "= pd.read_excel ('" + file + "')")
 u = int(i)


# Create all files excels
i = 0
while i<u:
	i = i + 1
	x,y = 'f', "=pd.read_excel ('"
	vars()[x + str(i)] = y + file + "')"
		#DEBUG 
		#print('Variables',vars())	


# Create data frames
i = 0
while i<u:
	z,y = "df"," = pd.DataFrame(f"
	i = i + 1
	vars() [z+str(i)] = y+str(i) +')'
	#vars()[z+str(i)] = y+str(i)+str(')')
		#DEBUG
		#print('Variables',vars())	
		#print (z+str(i)+y+str(i) +')')
i = 0	


# Filenames
excel_names = glob.glob('./*.*')


# read them in
excels = [pd.ExcelFile(file) for name in excel_names]


# turn them into dataframes
frames = [a.parse(a.sheet_names[0], header=None,index_col=None) for a in excels]


# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]


# concatenate them
combined = pd.concat(frames)
combined.to_excel('C:/Users/vteixeira/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/var/tmp/teixeira/XLS_Concatenate/Consolidado.xlsx',sheet_name='Sheet1')