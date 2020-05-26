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
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder",type=str, nargs='?',default='', help="folder with the chip folder")
parser.add_argument("chips", type=int, nargs='*',default=[22], help="chips to compare")
parser.add_argument("--signal",type=str, nargs='*',default=['all'], help='name of the signal to compare')
args = parser.parse_args()
chips = args.chips
folder = args.folder
signals = args.signal

clocks = ['SCLK0','SCLK1','SCLK2','RG','PCLK0','PCLK1','PCLK2','PCLK3']
biases = ['OD0_exp','OD1_exp','OG','RD','SPARE']
if signals == ['all']:
    signals = clocks + biases
if folder == '':
    folder = '/Users/gaior/DAMIC/data/singlecabac/20200519/4cabacvoltages/'


print('chips to be compared: ', chips)
print('signal to be ploted: ',signals)

for signal in signals:
    
    if signal in biases:
        types = ['bias']
        typeofsignal = 'bias'
    elif signal in clocks:
        types = ['rise','fall']
        typeofsignal = 'clock'
    for type in types:  
        xdata = np.array([])
        ydata = []
        plt.figure()
        for chip in chips:
            myscan = scan.Scan(signal, type, folder, chip, typeofsignal, 'test')
            myscan.getfiles()
            [a_x, a_y, a_rmsy] = myscan.extractcurve()
            xdata = a_x
            ydata.append(a_y)
            leg = type +' ' + signal.replace('_','') + ' chip = ' + str(chip)
            if typeofsignal == 'clock':
                plt.semilogy(a_x,a_y*1e9,'o',label=leg)
            if typeofsignal == 'bias':
                plt.plot(a_x,a_y,'o',label=leg)
            
        plt.xlabel('DAC unit')
        if typeofsignal== 'clock':
            plt.ylabel('time [ns]')
        if typeofsignal== 'bias':
            plt.ylabel('Output Voltage [V]')
        plt.tight_layout()
        plt.legend()
plt.show()

