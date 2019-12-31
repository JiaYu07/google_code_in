import glob
import os, sys
import re
from PIL import Image

input_dir=""
def main():
    files = []
    
    for ext in ('/*.jpeg', '/*.png', '/*.jpg'):
        files.extend(glob.glob('**/'+input_dir+ext,recursive=True))   

    ttt=(glob.glob('**/'+input_dir,recursive=True))     
    k=ttt[-1]+"/changed"
    if not os.path.exists(k):
        os.makedirs(k, exist_ok=True)
    
    for infile in files:
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        form=(im.format).lower()
        filename = infile.split("/")
        fname=filename[-1].split('.')[0]
        #print(infile)

        x_s=0
        y_s=0
        (x,y)=im.size     
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            p=k+"/"+fname+'.'+form       
            print("p:",p)     
            if (x<400 and y<400) :
                x_s=x
                y_s=y
            elif y>x or y==x:  
                ratio=float(x)/y
                y_s=400
                x_s=int(y_s*ratio)                
            elif x> y:
                ratio=float(y)/x
                x_s=400
                y_s=int(x_s*ratio)              
     
            physical_size=64*1024
            size_tmp=os.path.getsize(infile)
            q=95
            
            while size_tmp > physical_size and q>5 :                
                size_tmp=os.path.getsize(infile)
                im.save(p,form,quality=q)
                #print(size_tmp)
                q-=3  

            im= im.resize((x_s,y_s),Image.ANTIALIAS) 
            im.save(p,form)    


if __name__ == '__main__':
     input_dir=input()
     main()