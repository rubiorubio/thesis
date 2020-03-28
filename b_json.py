#%%
import math
import json
from AAA_from_file_to_list import *
import math


filename = 'D:\\FILES\\code\\thesis4\\files\json\\2.5\\all_points1805.json'
with open(filename,'w') as f:
    #json.dump(all_points,f,indent = 1)
    #json.dump(all_points_path,f,indent = 1)
    points = []
    freq = float(frequency[0][1])
    for i in range(len(all_points)):
        
        current_point = all_points[i]
        current_paths = all_points_path[i]
        current_pointLL = all_points_LanLon[i]
        current_paths1 = path1_LanLon[i]
        
        point = {
            "Frequency(mhz)" : float(frequency[0][1]),
            "x": current_pointLL[0],
            "y": current_pointLL[1],
            "z": float(current_point[3]),
            #"Distance": math.sqrt((float(current_point[1])-float(start_point[0][1]))**2+(float(current_point[2])-float(start_point[0][2]))**2+(float(current_point[3])-float(start_point[0][3]))**2),
            #'azimuth': math.degrees(math.atan2(((float(start_point[0][1]))-(float(current_point[1]))),(((float(start_point[0][2])-(float(current_point[2])))))))
        }
        point["paths"] = []
        for j in range(len(current_paths)):
            path1 = current_paths1[j]
            path = current_paths[j]
            point["paths"].append({
                "Delay(ns)": float(path[1]),
                "FieldStrength": float(path[2]),
                #"Amplitude(dbm)": float(path[2])-77.21-20*math.log10(freq),
                #"Phase" : 2*(math.pi)*(float(path[1]))*(float(frequency[0][1]))/1000,
            })

            if len(path) < 6:
                continue


            point["paths"][-1]["x"] = path1[0]
            point["paths"][-1]["y"] = path1[1]
            point["paths"][-1]["z"] = float(path[7])
            #point["paths"][-1]["azimuth"]= math.degrees(math.atan2(((float(path[5]))-(float(current_point[1]))),(((float(path[6])-(float(current_point[2])))))))
            #point["paths"][-1]["distance"]=math.sqrt((float(path[5])-float(start_point[0][1]))**2+(float(path[6])-float(start_point[0][2]))**2+(float(path[7])-float(start_point[0][3]))**2)
            #point["paths"][-1]["distance to point"]=(math.sqrt((float(path[5])-float(start_point[0][1]))**2+(float(path[6])-float(start_point[0][2]))**2+(float(path[7])-float(start_point[0][3]))**2))+(math.sqrt((float(current_point[1])-float(path[5]))**2+(float(current_point[2])-float(path[6]))**2+(float(current_point[3])-float(path[7]))**2))


                     
            if len(path) < 12:
                continue

            point["paths"][-1]["x1"] = path1[2]
            point["paths"][-1]["y1"] = path1[3]
            
            point["paths"][-1]["z1"] = float(path[13])
            #point["paths"][-1]["azimuth1"]= math.degrees(math.atan2(((float(path[11]))-(float(current_point[1]))),(((float(path[12])-(float(current_point[2])))))))
            #point["paths"][-1]["distance1"]= (math.sqrt((float(path[5])-float(start_point[0][1]))**2+(float(path[6])-float(start_point[0][2]))**2+(float(path[7])-float(start_point[0][3]))**2))+(math.sqrt((float(path[11])-float(path[5]))**2+(float(path[12])-float(path[6]))**2+(float(path[13])-float(path[7]))**2))
           # point["paths"][-1]["distance to point"] = (math.sqrt((float(path[5])-float(start_point[0][1]))**2+(float(path[6])-float(start_point[0][2]))**2+(float(path[7])-float(start_point[0][3]))**2))+(math.sqrt((float(path[11])-float(path[5]))**2+(float(path[12])-float(path[6]))**2+(float(path[13])-float(path[7]))**2))+(math.sqrt((float(current_point[1])-float(path[11]))**2+(float(current_point[2])-float(path[12]))**2+(float(current_point[3])-float(path[13]))**2))



            if len(path) < 18:
                continue
            point["paths"][-1]["x2"]        = path1[4]
            point["paths"][-1]["y2"]        = path1[5]
            point["paths"][-1]["z2"]        = float(path [19])
            #point["paths"][-1]["distance2"] =(math.sqrt((float(path[5])-float(start_point[0][1]))**2+(float(path[6])-float(start_point[0][2]))**2+(float(path[7])-float(start_point[0][3]))**2))+(math.sqrt((float(path[11])-float(path[5]))**2+(float(path[12])-float(path[6]))**2+(float(path[13])-float(path[7]))**2))+(math.sqrt((float(path[17])-float(path[11]))**2+(float(path[18])-float(path[12]))**2+(float(path[19])-float(path[13]))**2))
            #point["paths"][-1]["azimuth2"]  = math.degrees(math.atan2(((float(path[17]))-(float(current_point[1]))),(((float(path[18])-(float(current_point[2])))))))
            #point["paths"][-1]["full distance"] = (math.sqrt((float(path[5])-float(start_point[0][1]))**2+(float(path[6])-float(start_point[0][2]))**2+(float(path[7])-float(start_point[0][3]))**2))+(math.sqrt((float(path[11])-float(path[5]))**2+(float(path[12])-float(path[6]))**2+(float(path[13])-float(path[7]))**2))+(math.sqrt((float(path[17])-float(path[11]))**2+(float(path[18])-float(path[12]))**2+(float(path[19])-float(path[13]))**2))+(math.sqrt((float(current_point[1])-float(path[17]))**2+(float(current_point[2])-float(path[18]))**2+(float(current_point[3])-float(path[19]))**2))
            


        points.append(point)
        #print (current_point,current_paths)
        print(point)
    json.dump(points,f,indent = 1)

#%%