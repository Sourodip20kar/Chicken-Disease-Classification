import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safeload(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


# to create list of directories
@ensure_annotations
def create_directories(path_to_dict: list, verbose = True):   # 
    for path in path_to_dict:
        os.makedirs(path, exists_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data,f, indent=4)

#logger.info(f"json file saved at: {path}")

def decodeImage(imgstrign, filename):
    imgdata = base64.b64decode(imgstrign)
    f.write(imgdata)
    f.close()

def encodeImage(cropped_image_path):
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())