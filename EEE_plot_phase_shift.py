#%%
def process_one(fname):
	file = (open(fname))
	content = file.readlines()
	#print(content)
	list_for_complex = [] 
	for line in content:
		current_place = line[:-1]
		list_for_complex.append(current_place)

	from math import log10

	modull = []
	frequency = [1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825]

	for i in list_for_complex:  #  from list of comolex numbers to modul
		m = complex(i)
		modulus = abs(m)
		modull.append(modulus)
		
	print(modull)
	modul = []
	def mw_to_dbm(mW):
			return 10.*log10(mW)
	for i in modull:
		modul.append(mw_to_dbm(i))
	# print(modul)

	import matplotlib.pyplot as plot
	from matplotlib import pyplot
	from matplotlib import pyplot as plt

	plt.figure(figsize=(6,4))

	plt.suptitle('Spectrum')
	plt.xlabel('Frequency (Mhz)')
	plt.ylabel('Amplitude (dbm)')
	plt.plot(frequency,modul,color='green')
	plt.grid()
	for a,b in zip(frequency,modul): 
		
		pyplot.text(a, b, str(a),rotation=-60,color='red')
		pyplot.text(a+0.3, b, float(format(b,'.3f')),rotation=-70,)

	plt.savefig('D:\\FILES\\code\\thesis4\\files\\plot\\'+str(n1)+'.png')

	pass

n1= 20115
# n2= 15904
# n3= 16645
# n4= 17469
process_one("D:\\FILES\\code\\thesis4\\files\\complex_numb\\"+str(n1)+".txt")
# process_one("D:\\FILES\\code\\thesis4\\files\\complex_numb\\"+str(n2)+".txt")
# process_one("D:\\FILES\\code\\thesis4\\files\\complex_numb\\"+str(n3)+".txt")
# process_one("D:\\FILES\\code\\thesis4\\files\\complex_numb\\"+str(n4)+".txt")


#%%
