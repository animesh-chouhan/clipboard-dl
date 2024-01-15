import os
import time
import wget
import pyperclip
from urllib.parse import urlparse

sleep_time = 5
ignore_errors = True


def download():
    flag = True
    try:
        url = pyperclip.paste()
        filename = urlparse(url).path.split("/")[-1]
        if not os.path.isfile(filename):
            wget.download(url)
            print(filename)
    except ValueError as e:
        if e.args and "unknown url type:" in e.args[0]:
            print("Invalid url")
            flag = False
        else:
            if ignore_errors:
                print(f"ValueError: {e}")
                flag = False
            else:
                raise e
    except Exception as e:
        if ignore_errors:
            print(f"Exception: {e}")
            flag = False
        else:
            raise e
    return flag


while True:
    try:
        downloaded = False
        if download():
            downloaded = True
            sleep_time = 2
        else:
            sleep_time = 5
        time.sleep(sleep_time)
    except KeyboardInterrupt:
        if not downloaded:
            download()
        break
