import json
import os

def get_file_name(filepath: str):
    return filepath.replace('\\', '/').split('/')[1].split('.')[0]

def load_photos_folder(directory):
    c = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            file = {
                "name": get_file_name(f),
                "file": f,
                "columns": 3,
                "rows": 3
            }
            c.append(file)
            print(get_file_name(f))
            pass
    with open('photos.json', 'w') as file:
        file.write(json.dumps(c))