import os

from time import sleep
from abc import ABC

import requests
from bs4 import BeautifulSoup

from utils import config, constants as consts


class ScraperInit(ABC):

    # List of all the proxies from the file
    proxy_list = []

    # List of proxies that were used
    used_proxy = []

    def __init__(self):

        # From config file
        self.proxy = config.USE_PROXY

    @staticmethod
    def run(self):
        """The main logic of the app."""
        pass

    @staticmethod
    def save_image(image_url, image_filename):
        # Download image

        print("image_url", image_url)
        image_path = consts.IMG_DIR.joinpath(image_filename).resolve()
        for _ in range(3):
            try:
                if not os.path.exists(image_path):
                    r = requests.get(image_url, stream=True)
                    if r.status_code == 200:
                        with open(image_path, 'wb') as f:
                            for chunk in r:
                                f.write(chunk)
                    print("image saved: ", image_path)
                else:
                    print("image exists: ", image_path)

                break

            except Exception as _ex:
                try:
                    os.remove(image_path)
                except:
                    pass

                print("[ERROR] While 'Download image' > ", _ex)
                print("\n\nSleep 3 sec and retry")
                sleep(3)
                # raise _ex
                continue

    @staticmethod
    def get_soup(url):
        """Load page and return bs4 soup or None if page was not loaded

        :param url: str URL for loading.
        :return: BeautifulSoup object or None.
        """
        print('Loading page: {}'.format(url))
        for _ in range(3):
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'lxml')
                return soup

            except Exception as _ex:
                print("[ERROR] While 'Page loading' > ", _ex)
                print("\n\nSleep 3 sec and retry")
                sleep(3)
                continue
