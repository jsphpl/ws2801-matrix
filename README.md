#WS2801_Matrix

## Requirements

The following python packages need to be installed:
```
PIL / Pillow
numpy
spidev
```

## Usage

### Create an instance of the WS2801_Matrix class

You must pass the indexes of the leds as a 2-dimensional array as the first parameter to the constructor.

```python
import matrix
indexes = [  # a 2 by 2 display, yours will likely be larger…
	[1, 2],
	[0, 3]
]
matrix = matrix.WS2801_Matrix(indexes)
```

### Set the color of a single pixel by its x- and y-coordinates

```python
matrix.setPixel(12, 21, [255, 255, 255])  # set the pixel at x=12, y=21 to white
```

### Display an image file on the matrix

```python
path = 'example.png'
matrix.writeImageFile(path)
```

### Display a sequence of images

The images must be located in the same folder. Call `writeImageFolder(path, delay)` to loop through all images in `path`, showing each for `delay` seconds.

```python
path = 'animations/nyancat/'
matrix.writeImageFolder(path, 1)
```
