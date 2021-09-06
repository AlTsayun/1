from gui.image_label import ImageLabel
import tkinter as tk
from tkinter import messagebox
from types import FunctionType

class LoadingWindow(tk.Toplevel):
    
    def __init__(self, cancelAction: FunctionType):
        super().__init__()
        import pathlib
        self.title("Loading...")
        self.cancelAction = cancelAction
        self.resizable(0, 0)
        img = ImageLabel(self)
        img.pack()


        btnExecute = tk.Button(self, text= "Cancel", command= self.btnCancelClicked)
        btnExecute.pack(side= "bottom")

        self.protocol("WM_DELETE_WINDOW", self.btnCancelClicked)
        img.load("./resources/loading.gif")
        
    def btnCancelClicked(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure that you want to cancel operation?')
        if answer:
            self.cancelAction()
            self.destroy()
