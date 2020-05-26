################################
## Scan class ##
################################

import math
import numpy as np
#import constant
import xml.etree.ElementTree as ET
import os
import sys
cwd = os.getcwd()
classpath = cwd + '/../classes/'
utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
sys.path.append(classpath)
import glob
from datastruct import *
import reader

class Scan:
    """takes an input file and sets up the various class needed for the analysis """
    def __init__(self, signalname, type, folder, chipnumber, typeofsignal, comment):
        self.signalname = signalname
        self.measurement = []
        self.scantype = type
        self.folder = folder 
        self.chipnumber = chipnumber
        self.comment = comment
        self.files = []
        self.typeofsignal = typeofsignal
    def getfiles(self):
        files = glob.glob(self.folder + '/'+ str(self.chipnumber) + '/' + self.signalname + '/*' + self.scantype + '*.dat')
#        print self.folder + '/'+ str(self.chipnumber) + '/' + self.signalname + '/*' + self.scantype + '*.dat'
        self.files = files


    def extractcurve(self):
        a_setparam = np.array([])
        a_measparam = np.array([])
        a_measparam1 = np.array([])
        for file in self.files:
#            print (file)
            r = reader.Reader(file)
            meas = r.getmeas()
            if self.typeofsignal == 'clock': 
                setfall = float(meas.setvalues[1])
                setrise = float(meas.setvalues[0])
                measrise = float(meas.measvalue['Rise'])
                measfall = float(meas.measvalue['Fall'])
#                print ('measrise = ' , measrise, ' measfall = ' , measfall)
                if self.scantype == 'fall':
                    a_setparam = np.append(a_setparam, setfall)
                    a_measparam = np.append(a_measparam, measfall)
                if self.scantype == 'rise':
                    a_setparam = np.append(a_setparam, setrise)
                    a_measparam = np.append(a_measparam, measrise)
            if self.typeofsignal == 'bias': 
                setval = float(meas.setvalues[0])
                measmean = float(meas.measvalue['Mean'])
                measrms = float(meas.measvalue['RMS'])
                a_setparam = np.append(a_setparam, setval)
                a_measparam = np.append(a_measparam, measmean)
                a_measparam1 = np.append(a_measparam1, measrms)
        return [a_setparam, a_measparam, a_measparam1]





                
    
