import json
from .utils import sync_local_image, get_hash
from os import path

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
IMG_JSON_DIR = path.join(BASE_DIR, "images.json")
IMG_DIR = path.join(BASE_DIR, "assets", "images")

DANCE = False


def initializer():
    image_dict = {
        path.basename(file_path).split(".")[0]: file_path
        for file_path in sync_local_image(IMG_DIR)
    }
    with open(IMG_JSON_DIR, "w", encoding="UTF8") as json_file:
        json.dump(image_dict, json_file)

    context = {
        "secrets": json.loads(open("./secrets.json", encoding="UTF8").read()),
        "keywords": json.loads(open("./keywords.json", encoding="UTF8").read()),
        "images": json.loads(open("./images.json", encoding="UTF8").read()),
    }

    return context
