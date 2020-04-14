import os
import requests
from urllib.parse import urljoin


def get_file_extension(url):
    file_extension = url.split('.')[-1]
    return file_extension


def download_image(url, filename, folder='images'):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    filepath = os.path.join(folder, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_hubble_image(image_id):
    url_template = 'https://hubblesite.org/api/v3/image/{}'
    base_url = 'https://media.stsci.edu/'
    url = url_template.format(image_id)
    response = requests.get(url)
    response.raise_for_status()
    images_src = response.json()['image_files'][-1]['file_url']
    file_url = urljoin(base_url, images_src)
    file_extension = get_file_extension(file_url)
    filename = f'hubble{image_id}.{file_extension}'
    download_image(file_url, filename)


def fetch_hubble_collection(collection_title):
    url_template = 'http://hubblesite.org/api/v3/images/{}'
    url = url_template.format(collection_title)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    collection = response.json()
    for image in collection:
        image_id = image['id']
        fetch_hubble_image(image_id)