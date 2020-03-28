#%%
import cmath 
import json
import math
import time

t = time.process_time()
point_num= 13867
save_data = 'D:\\FILES\\code\\thesis4\\files\\complex_numb\\'+ str(point_num) +'.txt'


def process_one(fname):
	f = json.load(open(fname))
	phases = []
	amplitudes = []

	for p in f: 
		phase = []
		amplitude = []   
		for pt in p["paths"]:
			amplitude.append(pt["Amplitude(dbm)"])
			phase.append(pt["Phase"])
		phases.append(phase)
		amplitudes.append(amplitude)

	ss = phases[point_num]
	aaa = amplitudes[point_num]
	aa = []
	
	def dbm_to_mw(dBm):
			
		return 10**((dBm)/10.)

	for i in aaa:
		
		aa.append(dbm_to_mw(i))
	sin_list = [math.sin(i) for i in ss] # find a sin of Phase for complex numbers
	cos_list = [math.cos(i) for i in ss] # find a sin of Phase for complex numbers
	imag_part = [x * y for x, y in zip(sin_list, aa)]# find imagin part in ось y
	real_part = [x * y for x, y in zip(cos_list, aa)]# find imagin part in ось y
	sum_reail_part = sum(real_part)
	sum_imag_part  = sum(imag_part)
	freq200hz = complex(sum_reail_part,sum_imag_part)
	with open(save_data, 'a') as file:
		file.write(str(freq200hz) + '\n')
	pass
def first():
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1805.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1806.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1807.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1808.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1809.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1810.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1811.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1812.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1813.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1814.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1815.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1816.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1817.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1818.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1819.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1820.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1821.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1822.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1823.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1824.json")
	process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1825.json")
	elapsed_time = time.process_time() - t
	print(elapsed_time)
first()
t = time.process_time()


#%%
