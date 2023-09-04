import cv2
from PIL import Image
import os

class ImageLoader(object):
    """
    Class to load an image from a directory
    """
    
    def __init__(self) -> None:
        self.image_extensions = [".jpg", ".png", ".jpeg"]
        self.images = {}
        pass
    
    def _load_image(self, image_path: str) -> Image:
        """
        Load an image from a path
        :param image_path: path to image
        :return: image as a Pillow Image
        """
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            raise FileNotFoundError(f"Image path {image_path} not found")
        
    def _load_images(self, image_paths: list) -> list:
        """
        Load multiple images from a list of paths
        :param image_paths: list of paths to images
        :return: list of images as numpy arrays
        """
        images = \
                {
                    os.path.basename(image_path): self._load_image(image_path)
                    for image_path in image_paths
                }
        self.images.update(images)
        return images
    
    def load_images_from_dir(self, image_dir: str) -> list:
        """
        Load all images from a directory
        :param image_dir: path to directory
        :return: list of images as numpy arrays
        """
        image_paths = \
                [
                    os.path.join(image_dir, image_path) 
                    for image_path in os.listdir(image_dir)
                    if os.path.splitext(image_path)[1] in self.image_extensions
                ]
        return self._load_images(image_paths)
    
    def load_recursive(self, image_dir: str) -> list:
        """
        Load all images from a directory and all subdirectories
        :param image_dir: path to directory
        :return: list of images as numpy arrays
        """
        image_paths = \
                [
                    os.path.join(root, file)
                    for root, dirs, files in os.walk(image_dir)
                    for file in files
                    if os.path.splitext(file)[1] in self.image_extensions
                ]
        return self._load_images(image_paths)