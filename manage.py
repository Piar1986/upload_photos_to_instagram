import json
import os
import requests
from pathlib import Path
from urllib.parse import urljoin
from PIL import Image
from os import listdir
from dotenv import load_dotenv
from instabot import Bot
from scripts import fetch_hubble_collection
from scripts import fetch_spacex_last_launch


def format_images(source_folder='images', recipient_folder='formated_images'):
    files = listdir(source_folder)
    for file in files:
        image_path = os.path.join(source_folder, file)
        image = Image.open(image_path)
        image.thumbnail((1080, 1080))
        image_title = file.split('.')[0]
        new_image = image_title + '.jpg'
        new_image_path = os.path.join(recipient_folder, new_image)
        image.save(new_image_path)


if __name__ == '__main__':
    load_dotenv()
    instagram_login = os.getenv("INSTAGRAM_LOGIN")
    instagram_password = os.getenv("INSTAGRAM_PASSWORD")
    hubble_collection_title = 'stsci_gallery'

    Path('images').mkdir(parents=True, exist_ok=True)
    Path('formated_images').mkdir(parents=True, exist_ok=True)

    fetch_spacex_last_launch()
    fetch_hubble_collection(hubble_collection_title)
    format_images()
    
    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password, proxy=None)