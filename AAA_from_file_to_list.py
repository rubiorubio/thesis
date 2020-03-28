#%%
import utm

all_points = []
all_points_path = []
all_paths = []
frequency = []
start_point =[]
all_points_LanLon=[]

with open('D:\\FILES\\code\\thesis4\\files\\Intelligent Ray Tracing(IRT)\\PropName_nueva\\Site  1 Antenna 1 Rays.str','r') as file:
    for line in file:    
        if line.find("POINT") == 0:
            all_points.append(line.split())
            print(line.split())
            if len(all_paths) > 0:
                all_points_path.append(all_paths.copy())
                all_paths = []
        elif line.find("PATH ") == 0:
            last_path = line.split()
            all_paths.append(last_path)
        elif line.find("ANTENNA")==0:
            start_point.append(line.split())
        elif line.find("FREQUENCY") == 0:
            frequency.append(line.split())
            print(line.split())
    all_points_path.append(all_paths.copy())

for p in all_points:
    if p[0] != "POINT":
        continue
    z = (float(p[1]), float(p[2]), 33,'T')
    #print (utm.to_latlon(*z))
    all_points_LanLon.append((utm.to_latlon(*z)))

path1_LanLon=[]

for pt in all_points_path:
    point_paths = []
    for p in pt:
        if p[0] != "PATH" or len(p)== 5:
            x= (float(p[1]),float(p[2]))
            point_paths.append(x)
        elif p[0] != "PATH" or len(p) == 11:
            z = (float(p[5]), float(p[6]), 33,'T')        
            point_paths.append((utm.to_latlon(*z)))
        elif p[0] != "PATH" or len(p) == 17:
            z = (float(p[5]), float(p[6]), 33,'T') 
            zz =  (utm.to_latlon(*z))
            z1 = (float(p[11]), float(p[12]), 33,'T')
            zz1 = (utm.to_latlon(*z1))
            joinedlist  = zz+zz1
            point_paths.append(joinedlist)
        else:
            z    = (float(p[5]), float(p[6]), 33,'T') 
            zz   = (utm.to_latlon(*z))
            z1   = (float(p[11]), float(p[12]), 33,'T')
            zz1  = (utm.to_latlon(*z1))
            zzz  = (float(p[17]), float(p[18]), 33,'T')
            zzz1 =  (utm.to_latlon(*zzz))   
            joinedlist = zz+zz1+zzz1
            point_paths.append(joinedlist)
    path1_LanLon.append(point_paths)


# #%%
# len(all_points_path),len(path1_LanLon)
# #%%
# # len(all_points_path[174][0])
# path1_LanLon[174]
# #%%
# path1_LanLon
# #%%
# all_points_path[1][0][5]
# #%%
# all_points_LanLon[1]
# #%%
# len(all_points_path[0])
# all_points_path[0]

# #%%
# len(all_points_path), len(all_points)

# #%%
# all_points_path[7439][0][1]
# #%%

# all_points[25922:25932]
# with open('coordinates plot.txt','w') as file:
# 	file.write(str(all_points[25922:25932]))
# #%%
# print(frequency)
# print(start_point[0][2])
# #%%
# def find_point(all_p, x, y, z):
#     for i, p in enumerate(all_p):
#         if float(p[1]) == x and float(p[2]) == y and float(p[3]) == z:
#             return i
# print(find_point(all_points,  317127.75, 5687960.75, 1.50))


# #%%
# l = [1,2,3]
# s = [4,5,6]
# joinedlist = l+s
# print(joinedlist)
#%%
all_points

#%%
import utm
z = (317013.00, 5687907.00, 33,'T')
utm.to_latlon(*z)

# %%
