#%%
import math
import json
from AAA_from_file_to_list import *
import math

def process_one(filename):
    with open(filename,'w') as f:
        #json.dump(all_points,f,indent = 1)
        #json.dump(all_points_path,f,indent = 1)
        points = []
        for i in range(len(all_points)):

            current_paths = all_points_path[i]
            current_pointLL = all_points_LanLon[i]
                        
            point = {
                "Frequency(mhz)" : frequency,
                "x": current_pointLL[0],
                "y": current_pointLL[1],
                                
            }
            point["paths"] = []
            for j in range(len(current_paths)):
                path = current_paths[j]
                point["paths"].append({
                    "Amplitude(dbm)": float(path[2])-77.21-20*math.log10(frequency),
                    "Phase" : 2*(math.pi)*(float(path[1]))*float(frequency/1000),
                })


            points.append(point)
            #print (current_point,current_paths)
            print(point)
        json.dump(points,f,indent = 1)
    pass

frequency = 1806
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1806.json")
#%%
frequency = 1807
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1807.json")
frequency = 1808
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1808.json")
frequency = 1809
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1809.json")
frequency = 1810
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1810.json")
frequency = 1811
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1811.json")
frequency = 1812
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1812.json")
frequency = 1813
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1813.json")
frequency = 1814
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1814.json")
frequency = 1815
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1815.json")
frequency = 1816
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1816.json")
frequency = 1817
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1817.json")
frequency = 1818
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1818.json")
frequency = 1819
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1819.json")
frequency = 1820
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1820.json")
frequency = 1821
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1821.json")
frequency = 1822
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1822.json")
frequency = 1823
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1823.json")
frequency = 1824
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1824.json")
frequency = 1825
process_one("D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1825.json")
#%%
