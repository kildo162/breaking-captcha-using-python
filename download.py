from datetime import datetime
from pathlib import Path
import os
import shutil
import time
import requests as requests
import glob


def download_captcha_raw():

    index = check_index_file()

    for x in range(int(index) + 1, 1000000):

        time_default = 1

        current_dir = os.getcwd()
        path = os.path.join(current_dir, 'data/raw')

        image_url = "http://tracuunnt.gdt.gov.vn/tcnnt/captcha.png?uid=a5884a69-91cb-4f01-ae09-a168396bf7b6"
        filename = "{}.png".format(x)

        r = requests.get(image_url, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True
            with open(os.path.join(path, filename), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                time_sleep = time_default
                r.close()
                logger('Downloaded image successfully: {}'.format(filename))
        else:
            logger('Can not download {}'.format(r.status_code))
            time_sleep = +time_default
            r.close()
        time.sleep(time_sleep)


def logger(value):
    print('{} - {}'.format(datetime.now().time(), value))


def check_index_file():
    list_of_files = glob.glob('data/raw/*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return Path(latest_file).stem


if __name__ == "__main__":
    # print(check_index_file())
    download_captcha_raw()
