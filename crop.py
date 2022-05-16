import json
import os
import cv2

def crop_file(filepath: str, columns: int, rows: int):
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

            id = i + j

            crop_image = img[y:y+ear, x:x+eac]
            folder_path = 'output/%s/' % (name)
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path, exist_ok=True)
            filename = '%s/file%s.jpg' % (folder_path, id)
            f = filename.replace('\\', '/')
            cv2.imwrite(f, crop_image)

def crop():
    with open('photos.json', 'r') as file:
            photos = json.loads(file.read())
    for photo in photos:
        crop_file(photo['file'], int(photo['columns']), int(photo['rows']))
