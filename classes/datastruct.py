import numpy as np


class measurement:
    date = ''
    typeofsignal= ''
    nameofsignal = ''
    useTS = False
    setvalues = np.array([])
    clockdata = []
    cabacdata = {}
    repetition = 0
    measvalue = {}
    cabacnumber=0
    TSpath = ''
    def __init__(self):
        date = ''
        typeofsignal= ''
        nameofsignal = ''
        useTS = False
        clockdata = []
        cabacdata = {}
        repetition = 0
        measvalue = {}
        cabacnumber=0
        TSpath = ''
        #voltages = []

    def show(self):
        print ('CABAC number = ' , self.cabacnumber)
        print ('typeofsignal = ' ,self.typeofsignal)
        print ('nameofsignal = ', self.nameofsignal)
        print ('setvalues = ' , self.setvalues)
        print ('useTS = ' , self.useTS)
        print ('T S Path  = ', self.TSpath)
        print ('CABAC param = ', self.cabacdata)
        print ('clock data = ' , self.clockdata)
        print ('meas values = ', self.measvalue)


        
class metadata:
    date = ''
    cabacnumber=0
    TSpath = ''
    def __init__(self):
        date = ''
        cabacnumber=0
        TSpath = ''
    def show():
        print ('date = ' , self.date)
        print ('cabacnumber = ', self.cabacnumber)
        print ('TSpath = ', self.TSpath)


