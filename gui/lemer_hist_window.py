import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class LemerHistWindow(tk.Toplevel):
    def __init__(self, buckets: list, fromInclusive, toInclusive):
        super().__init__()

        bucketsCount = len(buckets)

        self.title("Lemer distribution histogram")
        fig = Figure()
        ax = fig.add_subplot()
        bucketsSum = sum(buckets)
        step = (toInclusive - fromInclusive) / bucketsCount
        bins = np.arange(fromInclusive, toInclusive + step / 2, step= step)
        ax.hist(bins[:-1], bins= bins, weights= [float(x) / bucketsSum for x in buckets])
        averageY = 1.0 / bucketsCount
        ax.hlines(averageY, fromInclusive, toInclusive, color= "green")
        ax.text(toInclusive, averageY, "1/m", ha='left', va='center')

        canvas = FigureCanvasTkAgg(fig, master= self)
        canvas.get_tk_widget().pack()
        canvas.draw()

