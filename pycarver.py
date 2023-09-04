#from pycarver_utils import pycarver_ui as ui
from pycarver_utils import image_loader as il

import tkinter as tk
import tkinter.filedialog as fd
import os
from PIL import Image

class Carver(object):
    """
    Class to scale an image to a given size
    """
    
    def __init__(self, 
                 image:Image, *, 
                 x_dim:float=None, 
                 y_dim:float=None,
                 target_dpi:float=300.0,
                 use_image_dpi:bool=False
                 ) -> None:
        """
        Initialize the Scaler object
        :param image: image to scale
        :param x_dim: x dimension to scale to (inches)
        :param y_dim: y dimension to scale to (inches)
        :param target_dpi: target dpi to scale to (default 300.0)
        :param use_image_dpi: use the image dpi to scale
        """
        self.image = image
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.use_image_dpi = use_image_dpi
        self.target_dpi = target_dpi
        
        self.scaled_image = None
        self._scale_image()
        pass
    
    def _inches_to_px(self, inches:float) -> float:
        """
        Convert inches to pixels
        :param inches: inches to convert
        :return: pixels
        """
        if inches is None:
            return None
        else:
            return inches * self.target_dpi
    
    def _scale_image(self) -> Image:
        """
        Scale the image to the given dimensions or use dpi
        """
        if self.use_image_dpi:
            self._scale_image_dpi()
            return None
        else:
            self._scale_image_dimensions()
            return None
    
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
             
    def _scale_image_dimensions(self) -> Image:
        """
        Scale the image to the given dimensions
        """
        x_px = round(self._inches_to_px(self.x_dim))
        y_px = round(self._inches_to_px(self.y_dim))
        self.scaled_image = self.image
        self.scaled_image.resize((x_px, y_px))
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
    images = loader.load_images_from_dir(f"{fd.askdirectory()}")
    for image in images:
        cv = Carver(images[image], x_dim=3.0, y_dim=3.0)
        print(f"resized: {cv.image.size} -> {cv.scaled_image.size}")
        cv.scaled_image.save(f".\images\scaled_{image}")