#%%
import numpy as np
import matplotlib.pyplot as plt

frequency = [1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825]

n1= 20115

file = (open("D:\\FILES\\code\\thesis4\\files\\complex_numb\\"+str(n1)+".txt"))
content = file.readlines()
#print(content)
list_for_complex = [] 
for line in content:
    current_place = line[:-1]
    list_for_complex.append(current_place)

modull = []
for i in list_for_complex:  #  from list of comolex numbers to modul
    m = complex(i)
    modulus = abs(m)
    modull.append(modulus)

tes = [] # delete each value from the lits to a sum of values of the list
for i in modull:
       tes.append(i/sum(modull))
frqmodul = dict(zip(frequency, tes))
x = list(frqmodul.keys())
y = np.cumsum(tes)

plt.figure(figsize=(6,4))

plt.suptitle('CDF')
plt.xlabel('Frequency (Mhz)')
plt.ylabel('Amplitude')
plt.grid()

plt.plot(x,y,color='green')
plt.savefig("D:\\FILES\\code\\thesis4\\files\\CDF\\"+str(n1)+".png")
	

#%%
