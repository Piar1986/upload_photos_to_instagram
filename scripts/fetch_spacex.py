import json
import os
import requests


def download_image(url, filename, folder='images'):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    filepath = os.path.join(folder, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)
        

def fetch_spacex_last_launch():
    latest_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(latest_launch_url)
    response.raise_for_status()
    images_url = response.json()['links']['flickr_images']
    for image_number, url in enumerate(images_url):
        filename = 'spacex' + str(image_number) + '.jpg'
        download_image(url, filename)