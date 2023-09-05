from pycarver_utils import image_loader as il

import tkinter as tk
import tkinter.filedialog as fd
import os
import numpy
from PIL import Image
from PIL import ImageMath

class Carver(object):
    """
    Class to scale an image to a given size
    """
    
    def __init__(self, 
                 image:Image, *, 
                 size:float=None, 
                 target_dpi:float=300.0,
                 use_image_dpi:bool=False
                 ) -> None:
        """
        Initialize the Scaler object
        :param image: image to scale
        :param size: the size in inches of the longest dimension (inches)
        :param y_dim: y dimension to scale to (inches)
        :param target_dpi: target dpi to scale to (default 300.0)
        :param use_image_dpi: use the image dpi to scale
        """
        self.image = image
        self.size = size
        self.use_image_dpi = use_image_dpi
        self.target_dpi = \
            (
            target_dpi 
            if not use_image_dpi or 'dpi' not in image.info 
            else
            sum([v for v in image.info['dpi']]) / len(image.info['dpi'])
            )
        self.scaled_image = self._scale_image()
        self.quantized_image = self._quantize_image()
        self.carving_area = self._get_carving_area()
        pass
    
    def __str__(self) -> str:
        return f"""<Carver:
                Filename: {self.image.filename}
                Image: {self.image}
                Size: {self.size}
                Target DPI: {self.target_dpi}
                Use Image DPI: {self.use_image_dpi}
                Scaled Image: {self.scaled_image}
                Quantized Image: {self.quantized_image}
                Carving Area: {self.carving_area}
>"""
    
    def _inches_to_px(self, inches:float) -> float:
        """
        Convert inches to pixels
        :param inches: inches to convert
        :return: pixels
        """
        if inches is None:
            return None
        else:
            return round(inches * self.target_dpi)
    
    def _scale_image(self) -> Image:
        """
        Scale the image to the given dimensions or use dpi
        """
        if self.use_image_dpi:
            return self._scale_image_dpi()
        else:
            return self._scale_image_dimensions()
    
    def _scale_image_dpi(self) -> Image:
        """
        Scale the image to the given dimensions using dpi
        """
        if 'dpi' not in self.image.info:
            raise ValueError("Image does not have dpi information")
        
        dpi = self.image.info['dpi']
        x_dim = round(self.image.size[0] / dpi[0])
        y_dim = round(self.image.size[1] / dpi[1])
        self.scaled_image = self.image
        self.scaled_image.resize((x_dim, y_dim))
        return self.scaled_image

    def _quantize_image(self) -> Image:
        """
        Quantize the image to 2 bits (black and white)
        """
        return self.scaled_image.quantize(2)
    
    def _get_carving_area(self) -> float:
        """
        Get the area to carve
        """
        to_carve = len([px for px in self.quantized_image.getdata() if px == 1])
        return to_carve / (self.target_dpi**2)

    def _scale_image_dimensions(self) -> Image:
        """
        Scale the image to the given dimensions
        """
        if self.image.size[0] > self.image.size[1]:
            scale_factor = (1, self.image.size[1] / self.image.size[0])
        elif self.image.size[0] < self.image.size[1]:
            scale_factor = (self.image.size[0] / self.image.size[1], 1)
            
        x_dim = self._inches_to_px(self.size * scale_factor[0])
        y_dim = self._inches_to_px(self.size * scale_factor[1])
             
        self.scaled_image = self.image.resize((x_dim, y_dim))
        return self.scaled_image

class Classifier(Carver):
    """
    Class to determine time per inch for a given image
    """
    def __init__(self, image:Image, carving_time:float, *, dpi:float=300.0) -> None:
        """
        Initialize the Classifier object
        :param image: image to classify
        :param dpi: dpi to classify at
        """
        self.image = image
        self.dpi = dpi
        self.carving_time = carving_time
        pass
    
    def classify_image(self) -> float:
        """
        Determine carving time per inch for the image
        """
        
        return
    

class Estimator(Carver):
    """
    Class to carve an image
    """
    
    def __init__(self, image:Image, *, dpi:float=300.0) -> None:
        """
        Initialize the Carver object
        :param image: image to carve
        :param dpi: dpi to carve at
        """
        
        self.image = image
        self.dpi = dpi
        self.carved_image = self.carve_image()
        pass
    
    def carve_image(self) -> Image:
        """
        Carve the image
        """
        return self.image
    
if __name__ == "__main__":
    loader = il.ImageLoader()
    images = loader.load_images_from_dir(r".\samples")#f"{fd.askdirectory()}")
    for image in images:
        cv = Carver(images[image], size=3.0, target_dpi=300.0)
        print(cv)
        print(f"resized: {cv.image.size} -> {cv.scaled_image.size}")
        if not os.path.exists(f".\images\scaled_{image}"):
            cv.quantized_image.save(f".\images\quantized_{image}")
        else:
            os.remove(f".\images\scaled_{image}")
            cv.quantized_image.save(f".\images\quantized_{image}")