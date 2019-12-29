import glob
import os
import re
from PIL import Image
#input_dir=input()
#file_list = os.listdir('/'+input_dir)
def main():
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

            if re.match(".png$",infile):
                im.save(file+"1.png" , "png")
            if re.match(".jpg$",infile):
                im.save(file+".jpg" , "jpg")
            if re.match(".jpeg$",infile):
                im.save(file+".jpeg" , "jpeg")

if __name__ == '__main__':
     input_dir=input()
     main()