import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from . import image_loader as il

class FileSelectWindow(tk.Tk):
    def __init__(self) -> None:
        # Load the image processor
        self.image_handler = il.ImageLoader()
        
        # Create the tkinter window
        self.tk_root = tk.Tk()
        self.tk_root.title("PyCarver")
        self.tk_root.geometry("800x600")
        self.tk_root.resizable(True, True)
        
        # Create the buttons
        self.buttons = {}
        self._build_buttons()
        self._place_buttons()
        
        # Create the variables
        self.filename = None
        self.directory = None
        self.recursive = False
        self.tk_root.mainloop()
        pass
    
    def _build_buttons(self) -> None:
        
        self.buttons['FileSelect'] = ttk.Button(
                self.tk_root,
                text="Select File",
                command=self._select_file
                )
        
        self.buttons['DirectorySelect'] = ttk.Button(
                self.tk_root,
                text="Select Directory",
                command=self._select_dir
                )
        
        self.buttons['LoadRecursive'] = ttk.Button(
                self.tk_root,
                text="Load Recursive",
                command=self._load_recursive
                )
        
        self.buttons['LoadSingleImage'] = ttk.Button(
                self.tk_root,
                text="Load Image",
                command=self._load_image
                )
        
        self.buttons['LoadDirectory'] = ttk.Button(
                self.tk_root,
                text="Load Images from Directory",
                command=self._load_images_from_dir
                )
        
        return None
    
    def _place_buttons(self) -> None:
        for button in self.buttons:
            self.buttons[button].pack()
    
    def _select_file(self) -> None:
        self.filename = fd.askopenfilename()
        return self.filename
    
    def _select_dir(self) -> None:
        self.directory = fd.askdirectory()
        return self.directory
    
    def _load_recursive(self) -> None:
        return self.image_handler.load_recursive(self.directory)
    
    def _load_image(self) -> None:
        return self.image_handler._load_images([self.filename])
    
    def _load_images_from_dir(self) -> None:
        return self.image_handler.load_images_from_dir(self.directory)
