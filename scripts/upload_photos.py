import os
from urllib.parse import urljoin
from PIL import Image
from os import listdir
from instabot import Bot


def format_images(source_folder='images', recipient_folder='formated_images'):
    files = listdir(source_folder)
    for file in files:
        image_path = os.path.join(source_folder, file)
        image = Image.open(image_path)
        image_trim_size = abs(image.height - image.width)/2

        if image.width < image.height:
            image_new_coordinates = (0, image_trim_size, image.width, image.height - image_trim_size)
        else:
            image_new_coordinates = (image_trim_size, 0, image.width - image_trim_size, image.height)

        cropped_image = image.crop(image_new_coordinates)
        cropped_image.thumbnail((1080, 1080))

        image_title = file.split('.')[0]
        new_image = image_title + '.jpg'
        new_image_path = os.path.join(recipient_folder, new_image)
        cropped_image.save(new_image_path)

def upload_images(login, password, source_folder='formated_images'):
    bot = Bot()
    bot.login(username=login, password=password, proxy=None)

    files = listdir(source_folder)
    for file in files:
        image_path = os.path.join(source_folder, file)
        bot.upload_photo(image_path, caption="Space is great!")