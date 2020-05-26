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
import scan
import datastruct
import glob



clocks = ['SCLK0','SCLK1','SCLK2','RG','PCLK0','PCLK1','PCLK2','PCLK3']
#folder='/Users/gaior/DAMIC/code/singlecabac/data/text/test20200228/'
folder = '/Users/gaior/DAMIC/data/singlecabac/20200519/4cabacvoltages/'
#signals = ['SCLK0','SCLK2']
#signals = ['PCLK0','PCLK1','PCLK2','PCLK3']
#signals = ['OD0_exp','OD1_exp','OG','RD','SPARE']
#signals = ['OD0_exp','OD1_exp','OG','RD','SPARE']
#signals = ['SPARE']
signals = ['PCLK0']
types = ['fall']
#types = ['bias']
typeofsignal = 'clock'
#typeofsignal = 'bias'
chips = [22,23,24,25,26,27]
#legends = ['Rise time', 'Fall time']

xdata = np.array([])
ydata = []
for chip in chips:
    for signal in signals:
        for type in types:    
            myscan = scan.Scan(signal, type, folder, chip, typeofsignal, 'test')
            myscan.getfiles()
            [a_x, a_y, a_rmsy] = myscan.extractcurve()
            #a_y = np.delete(a_y,10)
            #a_x = np.delete(a_x,10)
            xdata = a_x
            ydata.append(a_y)
#        print [a_x, a_y, a_rmsy]
            leg = type +' ' + signal.replace('_','') + ' chip = ' + str(chip)

            if typeofsignal == 'clock':
                plt.plot(a_x,a_y*1e9,'o',label=leg)
                
#                plt.semilogy(a_x,a_y*1e9,'o',label=leg)
            if typeofsignal == 'bias':
                plt.plot(a_x,a_y,'o',label=leg)
                #plt.plot(a_x,a_y,'o')
#                plt.plot(a_x,a_rmsy,'o',label=leg)
            
plt.xlabel('DAC unit')
if typeofsignal== 'clock':
    plt.ylabel('time [ns]')
if typeofsignal== 'bias':
    plt.ylabel('Output Voltage [V]')
plt.tight_layout()
plt.legend()
plt.figure()
if typeofsignal == 'bias':
    #plt.plot(xdata, ydata[1] - ydata[0],'o')
    plt.plot(xdata, ydata[0],'o')

    plt.ylabel('difference [V]')
if typeofsignal == 'clock':
    plt.semilogy(xdata, np.abs((ydata[1] - ydata[0])*1e9),'o')
#    plt.plot(xdata, ydata[0]*1e9,'o')
    plt.ylabel('difference [ns]')
plt.xlabel('DAC unit')
plt.show()
