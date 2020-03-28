#%%
import time

t = time.process_time()
#do some stuff

import folium
from folium import IFrame
import os
import base64
import json
import pandas as pd

pointsCX = []
pointsCY = []

sizeX=[10,12,14,16,18]
sizeY=[10,12,14,16,18]
with open('D:\\FILES\\code\\thesis4\\files\\json\\1.5\\all_points1805.json') as f:
    data = json.load(f)
    for r in data[:6]:
        #print(r['y'])
        pointsCX.append(r['x'])
        pointsCY.append(r['y'])


names = []
for i in range(len(pointsCY)):
    names.append("%s , %s"% (pointsCX[i],pointsCY[i]))

#-------------------------------------------------------------------------------------------------------------------------------------------
#%%
import folium
import base64
from folium import IFrame
import time

t = time.process_time()

x = 51.31342
y = 12.374792
m = folium.Map(location=[51.313335, 12.374654],tiles='Stamen Toner',zoom_start =17)

icon_url = 'https://image.flaticon.com/icons/svg/252/252106.svg'
html = '<img src="data:image/pdf;base64,{}">'.format
icon_urlT='https://image.flaticon.com/icons/svg/34/34408.svg'

def Transmitter_marker():
    icon = folium.features.CustomIcon(icon_urlT,icon_size=( 45))  # Creating a custom Icon
    # picture1 = base64.b64encode(open('D:\\FILES\\code\\Thesis_3attempt\\results\\Graphs\\51.31270683574608 , 12.373759465210595.png','rb').read()).decode()
    # iframe1 = IFrame(html(picture1), width=600+20, height=400+20)
    # popup1 = folium.Popup(iframe1, max_width=650)
    folium.Marker(location=[x, y],icon=icon,tooltip='Transmitter').add_to(m)  #adding it to the map
#------------------------------------m------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f0_marker2p():
    icon = folium.features.CustomIcon(icon_url,icon_size=( 20))  # Creating a custom Icon
    picture1 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\11407.png','rb').read()).decode()
    iframe1 = IFrame(html(picture1), width=400+20, height=300+20)
    popup1 = folium.Popup(iframe1, max_width=650)
    tooltip=len(data[11407]['paths']),data[11407]['Distance'],
    folium.Marker(location=[data[11407]['x'] , data[11407]['y']],icon=icon,popup=popup1,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\11513.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[11513]['paths']),data[11513]['Distance'],
    folium.Marker(location=[data[11513]['x'] , data[11513]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture3 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\11681.png','rb').read()).decode()
    iframe3 = IFrame(html(picture3), width=400+20, height=300+20)
    popup3 = folium.Popup(iframe3, max_width=850)
    tooltip=len(data[11681]['paths']),data[11681]['Distance'],
    folium.Marker(location=[data[11681]['x'] , data[11681]['y']],icon=icon,popup=popup3,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture31 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\11748.png','rb').read()).decode()
    iframe31 = IFrame(html(picture31), width=400+20, height=300+20)
    popup31 = folium.Popup(iframe31, max_width=850)
    tooltip=len(data[11748]['paths']),data[11748]['Distance'],
    folium.Marker(location=[data[11748]['x'] , data[11748]['y']],icon=icon,popup=popup31,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture4 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\11805.png','rb').read()).decode()
    iframe4 = IFrame(html(picture4), width=400+20, height=300+20)
    popup4 = folium.Popup(iframe4, max_width=850)
    tooltip=len(data[11805]['paths']),data[11805]['Distance'],
    folium.Marker(location=[data[11805]['x'] , data[11805]['y']],icon=icon,popup=popup4,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=( 20))  # Creating a custom Icon
    picture1 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\11926.png','rb').read()).decode()
    iframe1 = IFrame(html(picture1), width=400+20, height=300+20)
    popup1 = folium.Popup(iframe1, max_width=650)
    tooltip=len(data[11926]['paths']),data[11926]['Distance'],
    folium.Marker(location=[data[11926]['x'] , data[11926]['y']],icon=icon,popup=popup1,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\12258.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[12258]['paths']),data[12258]['Distance'],
    folium.Marker(location=[data[12258]['x'] , data[12258]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\12632.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[12632]['paths']),data[12632]['Distance'],
    folium.Marker(location=[data[12632]['x'] , data[12632]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\12912.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[12912]['paths']),data[12912]['Distance'],
    folium.Marker(location=[data[12912]['x'] , data[12912]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map
  
    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\13231.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[13231]['paths']),data[13231]['Distance'],
    folium.Marker(location=[data[13231]['x'] , data[13231]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\13549.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[13549]['paths']),data[13549]['Distance'],
    folium.Marker(location=[data[13549]['x'] , data[13549]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture3 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\13867.png','rb').read()).decode()
    iframe3 = IFrame(html(picture3), width=400+20, height=300+20)
    popup3 = folium.Popup(iframe3, max_width=850)
    tooltip=len(data[13867]['paths']),data[13867]['Distance'],
    folium.Marker(location=[data[13867]['x'] , data[13867]['y']],icon=icon,popup=popup3,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture31 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\14027.png','rb').read()).decode()
    iframe31 = IFrame(html(picture31), width=400+20, height=300+20)
    popup31 = folium.Popup(iframe31, max_width=850)
    tooltip=len(data[14027]['paths']),data[14027]['Distance'],
    folium.Marker(location=[data[14027]['x'] , data[14027]['y']],icon=icon,popup=popup31,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture4 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\14188.png','rb').read()).decode()
    iframe4 = IFrame(html(picture4), width=400+20, height=300+20)
    popup4 = folium.Popup(iframe4, max_width=850)
    tooltip=len(data[14188]['paths']),data[14188]['Distance'],
    folium.Marker(location=[data[14188]['x'] , data[14188]['y']],icon=icon,popup=popup4,tooltip=tooltip).add_to(m)
#------------------------------------m------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f12900_marker20p():
    icon = folium.features.CustomIcon(icon_url,icon_size=( 20))  # Creating a custom Icon
    picture1 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\14349.png','rb').read()).decode()
    iframe1 = IFrame(html(picture1), width=400+20, height=300+20)
    popup1 = folium.Popup(iframe1, max_width=650)
    tooltip=len(data[14349]['paths']),data[14349]['Distance'],
    folium.Marker(location=[data[14349]['x'] , data[14349]['y']],icon=icon,popup=popup1,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\14511.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[14511]['paths']),data[14511]['Distance'],
    folium.Marker(location=[data[14511]['x'] , data[14511]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture3 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\14843.png','rb').read()).decode()
    iframe3 = IFrame(html(picture3), width=400+20, height=300+20)
    popup3 = folium.Popup(iframe3, max_width=850)
    tooltip=len(data[14843]['paths']),data[14843]['Distance'],
    folium.Marker(location=[data[14843]['x'] , data[14843]['y']],icon=icon,popup=popup3,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture31 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\15185.png','rb').read()).decode()
    iframe31 = IFrame(html(picture31), width=400+20, height=300+20)
    popup31 = folium.Popup(iframe31, max_width=850)
    tooltip=len(data[15185]['paths']),data[15185]['Distance'],
    folium.Marker(location=[data[15185]['x'] , data[15185]['y']],icon=icon,popup=popup31,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture4 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\15724.png','rb').read()).decode()
    iframe4 = IFrame(html(picture4),  width=400+20, height=300+20)
    popup4 = folium.Popup(iframe4, max_width=850)
    tooltip=len(data[15724]['paths']),data[15724]['Distance'],
    folium.Marker(location=[data[15724]['x'] , data[15724]['y']],icon=icon,popup=popup4,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=( 20))  # Creating a custom Icon
    picture1 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\15904.png','rb').read()).decode()
    iframe1 = IFrame(html(picture1), width=400+20, height=300+20)
    popup1 = folium.Popup(iframe1, max_width=650)
    tooltip=len(data[15904]['paths']),data[15904]['Distance'],
    folium.Marker(location=[data[15904]['x'] , data[15904]['y']],icon=icon,popup=popup1,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture2 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\16645.png','rb').read()).decode()
    iframe2 = IFrame(html(picture2), width=400+20, height=300+20)
    popup2 = folium.Popup(iframe2, max_width=850)
    tooltip=len(data[16645]['paths']),data[16645]['Distance'],
    folium.Marker(location=[data[16645]['x'] , data[16645]['y']],icon=icon,popup=popup2,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture3 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\17469.png','rb').read()).decode()
    iframe3 = IFrame(html(picture3), width=400+20, height=300+20)
    popup3 = folium.Popup(iframe3, max_width=850)
    tooltip=len(data[17469]['paths']),data[17469]['Distance'],
    folium.Marker(location=[data[17469]['x'] , data[17469]['y']],icon=icon,popup=popup3,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture31 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\18295.png','rb').read()).decode()
    iframe31 = IFrame(html(picture31), width=400+20, height=300+20)
    popup31 = folium.Popup(iframe31, max_width=850)
    tooltip=len(data[18295]['paths']),data[18295]['Distance'],
    folium.Marker(location=[data[18295]['x'] , data[18295]['y']],icon=icon,popup=popup31,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture4 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\18505.png','rb').read()).decode()
    iframe4 = IFrame(html(picture4),  width=400+20, height=300+20)
    popup4 = folium.Popup(iframe4, max_width=850)
    tooltip=len(data[18505]['paths']),data[18505]['Distance'],
    folium.Marker(location=[data[18505]['x'] , data[18505]['y']],icon=icon,popup=popup4,tooltip=tooltip).add_to(m)    
    
    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture31 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\19535.png','rb').read()).decode()
    iframe31 = IFrame(html(picture31), width=400+20, height=300+20)
    popup31 = folium.Popup(iframe31, max_width=850)
    tooltip=len(data[19535]['paths']),data[19535]['Distance'],
    folium.Marker(location=[data[19535]['x'] , data[19535]['y']],icon=icon,popup=popup31,tooltip=tooltip).add_to(m)  #adding it to the map

    icon = folium.features.CustomIcon(icon_url,icon_size=(20))  # Creating a custom Icon
    picture4 = base64.b64encode(open('D:\\FILES\\code\\thesis4\\files\\plot\\20115.png','rb').read()).decode()
    iframe4 = IFrame(html(picture4), width=400+20, height=300+20)
    popup4 = folium.Popup(iframe4, max_width=850)
    tooltip=len(data[20115]['paths']),data[20115]['Distance'],
    folium.Marker(location=[data[20115]['x'] , data[20115]['y']],icon=icon,popup=popup4,tooltip=tooltip).add_to(m)    

#------------------------------------m------------------------------------------------------------------------------------------------------------------------------------------------------------------

def paths_point(point_id):
	 
	points = []

	for p in data[point_id]['paths']:
		if not "x" in p:
			continue
		points.append([x,y])
		points.append([p["x"],p["y"]])
		if "x1" in p:
			points.append([p["x1"],p["y1"]])
		points.append([data[point_id]["x"],data[point_id]["y"]])


	folium.Marker(location=[data[point_id]['x'] , data[point_id]['y']],
		tooltip=data[point_id]['Distance']).add_to(m)  #adding it to the map
	folium.PolyLine(
		points,

		tooltip=(len(data[point_id]['paths']),data[point_id]['Distance']),

		color ='green'
	).add_to(m)


Transmitter_marker()
f0_marker2p()
f12900_marker20p()
paths_point(11407)

folium.Marker([data[11407]['x'] , data[11407]['y']], tooltip = data[11407]['Distance']).add_to(m)
folium.Marker([data[11512]['x'] , data[11512]['y']], tooltip = data[11512]['Distance']).add_to(m)
folium.Marker([data[0]['x'] , data[0]['y']], tooltip = data[0]['Distance']).add_to(m)

m.save('D:\\FILES\\code\\thesis4\\result\\Points.html')

elapsed_time = time.process_time() - t
print(elapsed_time)
#%%
m


# %%
print("ddddd")

# %%
