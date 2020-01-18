import geopandas as gpd
import matplotlib.pyplot as plt
import os
#% plt inline
#os.getcwd()
#os.path.join(os.getcwd,"")
#get=open(r'taipei/roads.shp')
#桌面/google_code_in/shapefile/taipei/roads.shp
fp="/home/crystal/桌面/google_code_in/shapefile/"
taipei_roads = gpd.read_file(fp+"taipei/shape/roads.shp")
taipei_natural = gpd.read_file(fp+"taipei/shape/natural.shp")
taipei_buildings= gpd.read_file(fp+"taipei/shape/buildings.shp")
#print(gdf.head())
seoul_roads=gpd.read_file(fp+"seoul/shape/roads.shp")
seoul_natural=gpd.read_file(fp+"seoul/shape/natural.shp")
seoul_buildings=gpd.read_file(fp+"seoul/shape/buildings.shp")

kao_roads=gpd.read_file(fp+"kaoshuing/shape/roads.shp")
kao_natural=gpd.read_file(fp+"kaoshuing/shape/natural.shp")
kao_buildings=gpd.read_file(fp+"kaoshuing/shape/buildings.shp")

tokyo_roads=gpd.read_file(fp+"tokyo/shape/roads.shp")
tokyo_natural=gpd.read_file(fp+"tokyo/shape/natural.shp")
tokyo_buildings=gpd.read_file(fp+"tokyo/shape/buildings.shp")

beijing_roads=gpd.read_file(fp+"beijing/shape/roads.shp")
beijing_natural=gpd.read_file(fp+"beijing/shape/natural.shp")
beijing_buildings=gpd.read_file(fp+"beijing/shape/buildings.shp")

fig, axes1 = plt.subplots(figsize=(150,150))
taipei_roads.plot(ax=axes1, color='red')
taipei_natural.plot(ax=axes1, color='green')
taipei_buildings.plot(ax=axes1, color='blue')
axes1.set_title("taipei")
plt.show()

fig, axes2 = plt.subplots(figsize=(150,150))
seoul_roads.plot(ax=axes2, color='r')
seoul_natural.plot(ax=axes2, color='g')
seoul_buildings.plot(ax=axes2, color='b')
axes2.set_title("seoul")
plt.show()

fig, axes3 = plt.subplots(figsize=(150,150))
kao_roads.plot(ax=axes3, color='r')
kao_natural.plot(ax=axes3, color='g')
kao_buildings.plot(ax=axes3, color='b')
axes3.set_title("kao")
plt.show()

fig, axes4 = plt.subplots(figsize=(150,150))
tokyo_roads.plot(ax=axes4, color='blue')
tokyo_natural.plot(ax=axes4, color='green')
tokyo_buildings.plot(ax=axes4, color='red')
axes4.set_title("tokyo")
plt.show()

fig, axes5 = plt.subplots(figsize=(150,150))
beijing_roads.plot(ax=axes5, color='r')
beijing_natural.plot(ax=axes5, color='g')
beijing_buildings.plot(ax=axes5, color='b')
axes5.set_title("beijing")
plt.show()


#gdf.plot()
#plt.show()