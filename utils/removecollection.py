import glob
import os
import sys 
folder = sys.argv[1]


files = glob.glob(folder+ '*.dat*')
line = '<collection>'
for file in files:
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
        newlastline = '</collection>'
        data[-1]= newlastline
    with open(file, 'w') as fout:
        fout.writelines(data[1:])

