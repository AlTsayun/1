import tkinter as tk
from tkinter import Frame, messagebox
from tkinter.constants import END, RIDGE
from types import FunctionType

class LemerInputWindow(tk.Tk):
    def __init__(self, action: FunctionType):
        super().__init__()
        self.action = action
        validateRegistered =self.register(self.validatePositiveIntOrEmpty)

        self.title("Lemer generator setup")
        lblDescription = tk.Label(self, text= "Enter A, M and R0 parameters for Lemer generator.")
        lblDescription.pack(side= "top")

        frmInput = Frame(self)
        frmInput.pack(fill= "x", expand= True)

        frmInputLabels = Frame(frmInput)
        frmInputLabels.pack(side= "left")

        frmInputEntries = Frame(frmInput)
        frmInputEntries.pack(side= "top", fill= "both")

        lblA = tk.Label(frmInputLabels, text= "A:")
        lblA.pack()

        lblM = tk.Label(frmInputLabels, text= "M:")
        lblM.pack()
        
        lblR0 = tk.Label(frmInputLabels, text= "R0:")
        lblR0.pack()
        

        #a = 105491, m = 1999999, r0 = 20441

        self.entA = tk.Entry(frmInputEntries, validate= "all", validatecommand= (validateRegistered, "%P"))
        self.entA.insert(END, "105491")
        self.entA.pack(side= "top", fill= "x", expand= True)
        self.entA.focus()

        self.entM = tk.Entry(frmInputEntries, validate= "all", validatecommand= (validateRegistered, "%P"))
        self.entM.insert(END, "1999999")
        self.entM.pack(side= "top", fill= "x", expand= True)

        self.entR0 = tk.Entry(frmInputEntries, validate= "all", validatecommand= (validateRegistered, "%P"))
        self.entR0.insert(END, "20441")
        self.entR0.pack(side= "top", fill= "x", expand= True)

        btnExecute = tk.Button(self, text= "Execute", command= self.btnExecuteClicked)
        btnExecute.pack(side= "bottom")


    def btnExecuteClicked(self):
        if not self.validateA():
            self.showIncorrectInput()
            return
        if not self.validateM():
            self.showIncorrectInput()
            return
        if not self.validateR0():
            self.showIncorrectInput()
            return
        self.action(a= int(self.entA.get()), m= int(self.entM.get()), r0= int(self.entR0.get()))
        pass

    def validateA(self):
        return self.validatePositiveInt(self.entA.get())

    def validateM(self):
        return self.validatePositiveInt(self.entM.get())

    def validateR0(self):
        return self.validatePositiveInt(self.entR0.get())

    def validatePositiveIntOrEmpty(self, inputVal):
        return (not inputVal) or self.validatePositiveInt(inputVal)

    def validatePositiveInt(self, inputVal):
        try:
            return int(inputVal) > 0
        except ValueError:
            return False
    
    def showIncorrectInput(self):
        messagebox.showwarning("Incorrect input", "A, M and R0 must be positive integer values.")

