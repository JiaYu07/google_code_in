import geopandas as gpd
import matplotlib.pyplot as plt

basic="/home/crystal/桌面/google_code_in/shapefile/"
city=["taipei","seoul","kaoshuing","tokyo","beijing"]
element=["buildings","landuse","natural","places","points","railways","roads","waterways"]

for i in city:
    fig, axes= plt.subplots(figsize=(150,150))
    axes.set_title(i)
    tmp=""
    for j in element:
        tmp=basic+i+"/shape/"+j+".shp"
        msg=gpd.read_file(tmp)   
        msg.plot(ax=axes,cmap="gist_earth")
    plt.show()
