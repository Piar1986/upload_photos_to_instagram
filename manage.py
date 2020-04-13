from pathlib import Path
from scripts import fetch_hubble_collection
from scripts import fetch_spacex_last_launch
from scripts import format_images, upload_images


if __name__ == '__main__':

    hubble_collection_title = 'stsci_gallery'

    Path('images').mkdir(parents=True, exist_ok=True)
    Path('formated_images').mkdir(parents=True, exist_ok=True)

    fetch_spacex_last_launch()
    fetch_hubble_collection(hubble_collection_title)
    format_images()
    upload_images()