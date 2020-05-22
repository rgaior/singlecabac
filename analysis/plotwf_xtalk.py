import matplotlib.pyplot as plt
import numpy as np
import sys
import glob
files = sys.argv[1:]
#print filebase
#files = glob.glob(filebase)
activefile = 'C1'
clockchannel = {'C1':"PCLK0",'C2':"PCLK1",'C3':"PCLK2",'C4':"PCLK3"}
for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=5,unpack=True)
    filename = file[file.rfind('/')+1:]
    channel = filename[:2]
    print 'channel = ' , channel
    plt.plot(data[0]*1e6,data[1],alpha =0.5,label=clockchannel[channel])
#    print data[0], '  ', data[1]    

plt.xlabel('time [us]')
plt.ylabel('Voltage [V]')
plt.legend()
plt.show()
