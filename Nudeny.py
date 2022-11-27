import requests
import os
from PIL import Image
from urllib.request import urlopen
from urllib.parse import urlparse
import validators


class Detect:

    def __init__(self):
        self.URL = "http://127.0.0.1:8000/"

    def save_to_path(self, prediction, save_path, detection_type="bbox"):
        url = prediction['url']
        url_path = urlparse(url).path
        filename = url_path.split('/')[2]
        image = Image.open(requests.get(url, stream=True).raw)

        if os.path.exists(save_path):
            os.chdir(save_path)
            image.save(filename)
        else:
            raise Exception("Save path does not exist.")

    def detectExposed(self, paths=[], urls=[], save_path=None):
        files = []
        for path in paths:
            if not os.path.exists(path):
                raise Exception("Path provided does not exists.")
            files.append(('files', open(path, 'rb')))
        
        for url in urls:
            if not validators.url(url):
                raise Exception("URL provided is not valid.")
            image = urlopen(url).read()
            files.append(('files', image))

        response = requests.post(
            url=self.URL+"draw_bounding_box/", files=files).json()

        predictions = response['predictions']
        
        if not save_path == None:
            for prediction in predictions:
                self.save_to_path(prediction, save_path, detection_type="bbox")

        return response

    def censorExposed(self, paths=[], urls=[], save_path=None):
        files = []
        for path in paths:
            if not os.path.exists(path):
                raise Exception("Path provided does not exists.")
            files.append(('files', open(path, 'rb')))
        
        for url in urls:
            if not validators.url(url):
                raise Exception("URL provided is not valid.")
            image = urlopen(url).read()
            files.append(('files', image))

        response = requests.post(
            url=self.URL+"censor/", files=files).json()

        predictions = response['predictions']

        if not save_path == None:
            for prediction in predictions:
                self.save_to_path(prediction, save_path, detection_type="censor")

        return response
