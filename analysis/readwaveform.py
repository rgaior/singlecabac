import matplotlib.pyplot as plt
import numpy as np
import sys
files = sys.argv[1:]

for file in files:
    data = np.loadtxt(file,delimiter=',',skiprows=5,unpack=True)
#    print data[0], '  ', data[1] 
    plt.plot(data[0]*1e6,data[1])

plt.xlabel('time [us]')
plt.ylabel('Voltage [V]')
plt.show()
