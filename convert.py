import cv2
import logging
from pathlib import Path
from os import listdir
from os.path import join, isfile

logger = logging.getLogger(__name__)


def process_directory(directory):
    file_list = []
    for file_name in listdir(directory):
        file_path = join(directory, file_name)
        if isfile(file_path) and 'png' in file_name:
            file_list.append(file_path)
    return file_list


def convert_png_to_jpg_dir(directory):
    list_file = process_directory(directory)
    for file_path in list_file:
        convert_png_to_jpg(file_path)


def convert_png_to_jpg(file_path):
    logger.info(file_path)
    image = cv2.imread(file_path)
    file_name = Path(file_path).stem
    cv2.imwrite('{}.jpg'.format(file_name), image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

