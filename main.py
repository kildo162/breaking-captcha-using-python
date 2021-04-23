# -*- coding:utf-8 -*-
import logging
from PIL import Image
import cv2
from os import listdir
from os.path import join, isfile
import convert

# Create a custom logger
import download

logger = logging.getLogger(__name__)

RAW_PATH = "data/raw/"
SLICED_PATH = "data/sliced/"

chars_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars_dict = {c: chars_list.index(c) for c in chars_list}
list_chars = [f for f in listdir('data/chars') if isfile(join('data/chars', f)) and 'jpg' in f]


def process_directory(directory):
    file_list = []
    for file_name in listdir(directory):
        file_path = join(directory, file_name)
        if isfile(file_path) and 'jpg' in file_name:
            file_list.append(file_path)
    return file_list


def reduce_noise(file_path):
    print(file_path)
    img = cv2.imread(file_path)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 50, 50, 7, 21)
    cv2.imwrite(file_path, dst)
    img = Image.open(file_path).convert('L')
    img = img.point(lambda x: 0 if x < 128 else 255, '1')
    img.save(file_path)


def reduce_noise_dir(directory):
    list_file = process_directory(directory)
    for file_path in list_file:
        reduce_noise(file_path)


if __name__ == "__main__":
    # download.download_captcha_raw()
    # reduce_noise_dir(RAW_PATH)
    convert.convert_png_to_jpg_dir(RAW_PATH)
