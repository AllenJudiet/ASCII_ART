

Ascii=[" ","@","#","S","%","?","*","+",";",":",",","."]

def resize(image,nw):
    w,h=image.size
    ratio=h/w
    nh=int(nw*ratio)
    n_img=image.resize((nw,nh))
    return n_img

def grey(image):
     G_img=image.convert("L")
     return G_img

def convertimg(image,nw):
    new_img=grey(resize(image,nw))
    pixs=new_img.getdata()
    chars="".join([Ascii[pix//25] for pix in pixs])
    pixcount=len(chars)
    op="\n".join(chars[i:i+nw]for i in range(0,pixcount,nw))

    return op


