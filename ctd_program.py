import numpy as np
import matplotlib.pyplot as plt
data=np.genfromtxt('/Users/nataliekellogg/Desktop/Computer_class/module_practice_data/2017-01-0118.ctd',comments='#',skip_header=569, usecols=range(0,8))
#define columns
pressure=data[:,0]
tempC=data[:,2]
#open figure
fig=plt.figure()
plt.axis([0,30,2000,0])
plt.plot(tempC,pressure,'-',c='royalblue',ms=1,lw=2)
plt.title('Temperature vs. Pressure, 2015')
ax=fig.add_subplot(111)
ax.set_xlabel('Temperature (DegC)')
ax.set_ylabel('Pressure (dbars)')
#
plt.show()