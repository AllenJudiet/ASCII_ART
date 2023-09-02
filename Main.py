import PIL.Image
import os
from convertion import*
width=300
path=r"IMAGEPATH"
img=PIL.Image.open(path)



text=convertimg(img,width)
f=open("img.txt","w")
print(text)
f.write(text)
f.close()
os.startfile(f.name)
print("<DONE>")
