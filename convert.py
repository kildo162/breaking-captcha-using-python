import glob
import os
from os import listdir
from os.path import join, isfile
from pathlib import Path

import cv2
from PIL import Image


def process_directory(directory):
    file_list = []
    for file_name in listdir(directory):
        file_path = join(directory, file_name)
        if isfile(file_path) and 'png' in file_name:
            file_list.append(file_path)
    return file_list


def convert_png_to_jpg_dir(directory):
    files = glob.glob(f"{directory}/*")

    for file in files:
        convert_png_to_jpg(file)


def convert_png_to_jpg(file_path):
    print(file_path)

    image = cv2.imread(file_path)
    file_name = Path(file_path).stem
    cv2.imshow('Display Image', image)
    cv2.waitKey(0)
    # transform image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # apply cv2.THRESH_TRUNC or cv2.THRESH_OTSU
    _, image_new = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
    cv2.imwrite(f"{'data/train/{}.png'.format(file_name)}", image_new)

    image = Image.open(f"data/train/{'{}.png'.format(file_name)}")
    image = image.convert("P")
    image2 = Image.new("P", image.size, 255)

    # set pixel black
    for x in range(image.size[1]):
        for y in range(image.size[0]):
            pixel = image.getpixel((y, x))
            if pixel < 115:
                image2.putpixel((y, x), 0)

    # save converted image
    image2.save(f"data/train/{os.path.basename(file_path)}")
    # glob.delete(f"{path_finish}/aplicado.png")

