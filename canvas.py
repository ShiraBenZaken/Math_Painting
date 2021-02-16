import numpy as np
from PIL import Image
from filestack import Client


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user color
        self.data[:] = self.color

    def make(self, imagepath):
        # Convert array to image
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
        cli = Client('AwLL2HELRRODyqYu8aWBxz')
        filelink = cli.upload(filepath=imagepath)
        print(filelink.url)  
