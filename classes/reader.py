################################
## reader class ##
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
from datastruct import *


class Reader:
    """takes an input file and sets up the various class needed for the analysis """
    def __init__(self, filename):
        self.filename = filename
        self.root = ET.Element
        self.meas = measurement
    def open(self):
        tree = ET.parse(self.filename)
        return tree
    def getmeas(self):      
        tree = self.open()
        root = tree.getroot()
        meas = measurement()
        setval = np.array([])
        for child in root:
            if child.find('Name').text == 'Measurement setting IN':                
                for subchild in child:
                    try:
                        name = subchild.find('Name').text
#                        print 'name = ' , name 
                        # get the type of signal
                        if  name == 'ClockorBias':
                            CorB = int(subchild.find('Val').text)
                            if CorB == 0:
                                meas.typeofsignal = 'bias'
                            elif CorB == 1:
                                meas.typeofsignal = 'clock'
                        # get the name of signal
                        if  name == 'Signal name':
                            meas.nameofsignal = subchild.find('Val').text
                        # get the set values
                        if  name == 'Set Values':
                            for val in subchild.findall('DBL'):
                                value = val.find('Val').text
                                setval = np.append(setval,float(value))
                            meas.setvalues = setval 
                        if  name == 'Repetition':
                            meas.repetition = int(subchild.find('Val').text)
#                        if  name == 'UseTS':
#                            meas.UseTS = subchild.find('Val')
                        if  name == 'TS path':
                            meas.TSpath = subchild.find('Val').text
#                            print ' s;adkfnl;k ', subchild.find('Val').text
                        if name == 'CABACnumber':
                            meas.cabacnumber = int(subchild.find('Val'),text)
                    except:
                        continue
            if child.find('Name').text == 'CABACinput':
                a = child.findall('U8')
                b = child.findall('DBL')
                c = child.findall('Boolean')
                d = a+b+c
                for el in d:
                    nameofsig = el.find('Name').text  
                    valofsig = el.find('Val').text  
                    meas.cabacdata[nameofsig] = valofsig

            if child.find('Name').text == 'ClockData':
                a = child.findall('U32')
                for el in a:
                    if el.find('Val').text !=None:
                        meas.clockdata.append(int(el.find('Val').text))
            if child.find('Name').text == 'MeasData':
                 a = child.findall('DBL')
#                 print a
#                 for el in a:
#                     print 'sss ' , int(el.find('Val').text)
#                     meas.measdata.append(int(el.find('Val').text))
                 for subchild in child:
                    try:
                        name = subchild.find('Name').text
                        if name == 'Array':
#                            print 'name = ' , name
                            for subsubchild in subchild:
                                try:
                                    name = subsubchild.find('Name').text
                                    a = subsubchild.findall('DBL')
                                    b = subsubchild.findall('String')
#                                    print a.find('Val').text
#                                    for ela,elb in zip(a,b):
                                    for ela,elb in zip(a,b):
                                        val =  ela.find('Val').text
                                        description = elb.find('Val').text
                                        meas.measvalue[description] = val
#                                        print 'val = ',  val , 'desc = ' , description
#                                        print 'val = ',  val 
#                                        print int(el.find('Val').text)
#                                    print a
                                except:
                                    continue
                    except:
                        continue
#        meas.show()
        return meas
            

        


