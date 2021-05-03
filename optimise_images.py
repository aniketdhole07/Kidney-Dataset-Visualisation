
import cv2
import os
def get_file():
    path = "/home/aniket/Desktop/Projects/nanostring/static/crp_imgs"
    paths=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.endswith(".png")):
                paths.append(os.path.join(root,file))
    print(paths)
    return paths
def resize(image,window_height = 500):
    aspect_ratio = float(image.shape[1])/float(image.shape[0])
    window_width = window_height/aspect_ratio
    image = cv2.resize(image, (int(window_height),int(window_width)))
    return image
paths=get_file()
for i in paths:
    img = cv2.imread(i)         #image location
    img_resized = resize(img,window_height = 500)
    head, tail = os.path.split(i)
    print(i)
    cv2.imwrite('crp_imgs/'+str(tail),img_resized)
for i in paths:
    tmp=i.replace(" ","")
    os.rename(i,tmp) 

