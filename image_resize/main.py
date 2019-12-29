import glob
import os
import re
from PIL import Image
#input_dir=input()
#file_list = os.listdir('/'+input_dir)
infile=""
file=''
im=''
def main():
    global infile, file, im
    files = []
    for ext in ('/*.jpeg', '/*.png', '/*.jpg'):
        files.extend(glob.glob(input_dir+ext))

    #print(files)
    for infile in files:
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            (x,y)=im.size
            #print(x,y)
            y_s=300
            x_s=x/(y_s/300)                
            if  (x_s>400):
                x_s=400            
            im= im.resize((x_s,y_s),Image.ANTIALIAS)
            saving()            

            physical_size=64*1024
            size_tmp=im.getsize()
            q=100
            while size_tmp > physical_size and q>0 :
                out = im.resize(im.size, Image.ANTIALIAS) 
                saving(q)
                size_tmp=im.getsize()
                print(size_tmp)
                q-=5               


def saving(q=100):
    global infile, file, im

    if re.match(".png$",infile):
        im.save(file+".png" , "png",quality=q)
    if re.match(".jpg$",infile):
        im.save(file+".jpg" , "jpg",quality=q)
    if re.match(".jpeg$",infile):
        im.save(file+".jpeg" , "jpeg",quality=q)

if __name__ == '__main__':
     input_dir=input()
     main()
