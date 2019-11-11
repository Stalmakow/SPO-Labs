#!/usr/bin/python3
import folium as flm
import pandas as pd

data =pd.read_csv("data2.csv")



map = flm.Map(location=[59.970550 , 30.430893], zoom_start = 13)

x=data.iloc[:,2]
y=data.iloc[:,3]
vote1=data.iloc[:,4]
vote2=data.iloc[:,5]
vote3=data.iloc[:,6]
per1=data.iloc[:,8]
per2=data.iloc[:,9]
per3=data.iloc[:,10]


for x,y,vote1,vote2,vote3,per1,per2,per3 in zip(x,y,vote1,vote2,vote3,per1,per2,per3):
    flm.CircleMarker(location=[x,y],radius = 6, popup=str(vote1)+" ("+str(per1)+"%) For Amosov \n"+str(vote2)+" ("+str(per2)+"%) For Beglov \n"+str(vote3)+" ("+str(per3)+"%) For Tikhonova", icon=flm.Icon(color = 'gray')).add_to(map)


map.save("map1.html")
