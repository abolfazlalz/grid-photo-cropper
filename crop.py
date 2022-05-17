import json
import os
import cv2
from cv2 import Mat

def resize(img: Mat, scale: int):
    print(scale)
    if scale == 1:
        return img
 
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / scale)
    height = int(img.shape[0] * scale_percent / scale)
    dim = (width, height)
    
    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    

def crop_file(filepath: str, columns: int, rows: int, scale: int):
    img = cv2.imread(filepath)
    name = filepath.replace('\\', '/').split('/')[1].split('.')[0]
    print(name)

    h, w, c = img.shape

    # Each avatar sizes
    eac = int(w / columns)
    ear = int(h / rows)

    for i in range(3):
        for j in range(3):
            x = i * eac
            y = j * ear
            
            crop_image = img[y:y+ear, x:x+eac]
            folder_path = 'output/%s/' % (name)
            
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path, exist_ok=True)
            filename = '%s/file%s.jpg' % (folder_path, i + j)
            f = filename.replace('\\', '/')
            cv2.imwrite(f, resize(crop_image, scale))

def crop():
    with open('photos.json', 'r') as file:
            photos = json.loads(file.read())
    for photo in photos:
        crop_file(photo['file'], int(photo['columns']), int(photo['rows']), int(photo['scale']))
