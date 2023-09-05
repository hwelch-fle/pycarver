# pycarver
Python tool for estimating woodcarving time for handcarved leather

## Usage
Place a black and white image in the samples folder, then load that image using the `ImageLoader` class

```python
from pycarver_utils.image_loader import ImageLoader

loader = ImageLoader()
images = loader.load_images_from_dir(".\samples")

for image in images:
  cv = Carver(images[image], size=3.0, target_dpi=300.0)
  print(cv)

>>> <Carver:
                Filename: .\samples\Mezcalaria.png
                Image: <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2019x2017 at 0x214AE75D310>
                Size: 3.0
                Target DPI: 300.0
                Use Image DPI: False
                Scaled Image: <PIL.Image.Image image mode=RGBA size=900x899 at 0x214AE75EE50>
                Quantized Image: <PIL.Image.Image image mode=P size=900x899 at 0x214CF731750>
                Carving Area: 2.415477777777778
>
```
Where the Carving Area is the total square inches of material that need to be carved to reproduce the image

## TODO
Implement the `Estimator` and `Classifier` objects to allow for existing projects to be imput to the program to better estimate time.
  -As of now the only data the program can determine is the area of the carved image

Implement a function in the `Carver` object to allow for estimation of paint areas by color.
  - Extend this into the `Estimator` and `Classifier` objects to allow for the user to estimate carving time, painting time, and paint cost
