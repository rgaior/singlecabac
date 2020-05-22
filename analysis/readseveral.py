import numpy as np
import os
import sys
import matplotlib.pyplot as plt
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import reader
import datastruct
import glob
#import constant
#import utils

clocks = ['SCLK0','SCLK1','SCLK2','RG','PCLK0','PCLK1','PCLK2','PCLK3']
folder='/Users/gaior/DAMIC/code/singlecabac/data/text/test20200228/'
signals = ['SCLK0','SCLK1']
for signal in signals:
    files = glob.glob(folder + '*'+ signal+'*'+'*.dat')
    a_risedata = np.array([])
    a_falldata = np.array([])
    a_risesetdata = np.array([])
    a_fallsetdata = np.array([])
    if signal is in clocks:
        for file in files
        print file
        r = reader.Reader(file)
        meas = datastruct.measurement
        meas = r.getmeas()
        if 'fall' in file:
            # do the rise scan:
            a_fallsetdata = np.append(a_fallsetdata,meas.setvalues[0])
            a_fallsetdata1 = np.append(a_fallsetdata1,meas.setvalues[1])
#    print 'meas.setvalues ', meas.setvalues
    a_data = np.append(a_data, float(meas.measvalue[dataname]))
    a_data1 = np.append(a_data1, float(meas.measvalue[dataname1]))

size = len(a_data)
#plt.semilogy(a_setdata[:size/2],a_data[:size/2]*1e9,'o',label='Fall time')
#plt.semilogy(a_setdata1[size/2:],a_data1[size/2:]*1e9,'o',label='Rise time')
plt.plot(a_setdata[:size/2],a_data[:size/2]*1e9,'o',label='Fall time')
plt.plot(a_setdata1[size/2:],a_data1[size/2:]*1e9,'o',label='Rise time')
#print 
print a_data
# #input = np.arange(0,255,10)
# input = np.arange(0,1023,50)
# #plt.semilogy(input[:-1], a_data,'o')
# plt.plot(input[:-2], a_data,'o')
# #plt.xlabel('DAC [0-255]')
plt.xlabel('DAC value')
plt.ylabel('Rise/Fall time [ns]')
# plt.ylabel('OD0 [V]')
plt.legend()
plt.show()
#meas.show()
