#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import numpy as np
from PIL import Image
from LedStrip_WS2801 import LedStrip_WS2801, LedStrip_WS2801_FileBased

class WS2801_Matrix:
    def __init__(self, indexes):
        self.indexes = np.array(indexes)
        num_leds = self.indexes.shape[0] * self.indexes.shape[1]
        self.strip = LedStrip_WS2801(num_leds)

    @property
    def height(self):
        return self.indexes.shape[0]

    @property
    def width(self):
        return self.indexes.shape[1]

    """
    Get the led's index from its xy coords
    """
    def getIndex(self, x, y):
        return self.indexes[y][x]

    """
    Set a pixel to a specific color by its coordinates
    """
    def setPixel(self, x, y, color, update = True):
        index = self.getIndex(x, y)
        # print "x=%i, y=%i, index=%i, color=%s" % (x, y, index, color)
        self.strip.setPixel(index, color)
        if update:
            self.strip.update()

    """
    Set all pixels to a specific color.
    """
    def setAll(self, color):
        self.strip.setAll(color)
        self.strip.update()

    """
    Replace all pixels with new values
    """
    def writeArray(self, array):
        for x, y in self.iterPixels():
            self.setPixel(x, y, array[y][x], False)
        self.strip.update()

    """
    An iterator over all pixels as (x, y) tuple.
    """
    def iterPixels(self):
        for x in xrange(0, self.width):
            for y in xrange(0, self.height):
                yield (x, y)

    """
    Write an image from file to the matrix. Image
    dimensions must match the matrix dimensions.
    """
    def writeImageFile(self, path):
        image = Image.open(path)
        image_array = np.array(image, dtype=int)
        if image_array.shape[0:2] != self.indexes.shape[0:2]:
            raise DimensionsMismatch()
        else:
            self.writeArray(image_array)

    """
    Write a sequence of images from to the matrix. Images
    located at the given path are shown in the order of
    their filenames. Image & matrix dimensions must match.
    """
    def writeImageFolder(self, path, delay):
        while True:
            for file in sorted(os.listdir(path)):
                try:
                    file_path = os.path.join(path, file)
                    self.writeImageFile(file_path)
                except Exception as e:
                    if isinstance(e, DimensionsMismatch):
                        print("The dimensions of '%s' don't match" % file_path)
                    else:
                        print("'%s' doesn't seem to be a valid image file" % file_path)
                else:
                    time.sleep(delay)


class DimensionsMismatch(Exception):
    pass

