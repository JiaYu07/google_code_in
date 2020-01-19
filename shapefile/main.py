import geopandas as gpd
import matplotlib.pyplot as plt
import os
import pathlib

basic= os.getcwd()
city=["taipei","seoul","kaoshuing","tokyo","beijing"]
element=["buildings","landuse","natural","places","points","railways","roads","waterways"]

def main():
    for i in city:
        fig, axes= plt.subplots(figsize=(150,150))
        axes.set_title(i)
        tmp=""
        for j in element:
            tmp=basic+"/cities/"+i+"/shape/"+j+".shp"
            msg=gpd.read_file(tmp)   
            msg.plot(ax=axes,cmap="gist_earth")
        plt.show()
        
if __name__ == "__main__":
    main()
