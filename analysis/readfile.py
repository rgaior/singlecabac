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
#import constant
#import utils


folder='/Users/gaior/DAMIC/code/singlecabac/data/text/test20200224/'
fclock = '20200224_110214_PCLK0_Slope.dat'
fbias = '20191218_173643_OG_Noise.dat'
file = folder + fclock

reader = reader.Reader(file)
meas = datastruct.measurement
meas = reader.getmeas()
meas.show()
