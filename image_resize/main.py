import glob
import os
import re
from PIL import Image

def main():
    files = []
    for ext in ('/*.jpeg', '/*.png', '/*.jpg'):
        files.extend(glob.glob('/home/crystal/**/'+input_dir+ext,recursive=True))        
    
    for infile in files:
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        form=(im.format).lower()
        filename = infile.split("/")
        fname=filename[-1].split('.')[0]
       #print(fname)
        x_s=0
        y_s=0
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            (x,y)=im.size            
           #print(x,y)
            if (x<400 and y<400) :
                x_s=x
                y_s=y
            elif y>x or y==x:  
                ratio=float(x)/y
                y_s=400
                x_s=int(y_s*ratio)                
            elif x< y:
                ratio=float(y)/x
                x_s=400
                y_s=int(x_s*ratio)  

            physical_size=64*1024
            size_tmp=os.path.getsize(infile)
            q=95

            while size_tmp > physical_size and q>5 :                
                size_tmp=os.path.getsize(infile)
                im.save(fname,form,quality=q)
                #print(size_tmp)
                q-=3  

            im= im.resize((x_s,y_s),Image.ANTIALIAS)      
            im.save(infile,quality=q)    

if __name__ == '__main__':
     input_dir=input()
     main()
