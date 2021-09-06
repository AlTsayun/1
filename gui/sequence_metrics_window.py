import tkinter as tk
from tkinter import Frame, messagebox
from tkinter.constants import END, RIDGE
from types import FunctionType

class PeriodicMetricsWindow(tk.Toplevel):
    def __init__(self, metrics):
        super().__init__()
        name = metrics.getName()

        self.title(f"{name} metrics")
        lblDescription = tk.Label(self, text= f"Parameters of {name} sequence are following:")
        lblDescription.pack(side= "top")

        frmMetrics = Frame(self)
        frmMetrics.pack(fill= "x", expand= True)

        frmMetricsLabels = Frame(frmMetrics)
        frmMetricsLabels.pack(side= "left")

        frmMetricsValues = Frame(frmMetrics)
        frmMetricsValues.pack(side= "top", fill= "both")

        lblExpectedValue = tk.Label(frmMetricsLabels, text= "Expected value:")
        lblExpectedValue.pack()
        
        lblVariance = tk.Label(frmMetricsLabels, text= "Variance:")
        lblVariance.pack()

        lblStandardDeviation = tk.Label(frmMetricsLabels, text= "Standard deviation:")
        lblStandardDeviation.pack()

        lblPeriodLength = tk.Label(frmMetricsLabels, text= "Period length:")
        lblPeriodLength.pack()

        lblAperiodLength = tk.Label(frmMetricsLabels, text= "Aperiod length:")
        lblAperiodLength.pack()

        lblCircleRatio = tk.Label(frmMetricsLabels, text= "\"Circle\" ratio:")
        lblCircleRatio.pack()

        lblExpectedValueValue = tk.Label(frmMetricsValues, text= metrics.getExpectedValue())
        lblExpectedValueValue.pack(side= "top", fill= "x", expand= True)

        lblVarianceValue = tk.Label(frmMetricsValues, text= metrics.getVariance())
        lblVarianceValue.pack(side= "top", fill= "x", expand= True)

        lblStandardDeviationValue = tk.Label(frmMetricsValues, text= metrics.getStandardDeviation())
        lblStandardDeviationValue.pack(side= "top", fill= "x", expand= True)

        lblPeriodLengthValue = tk.Label(frmMetricsValues, text= metrics.getPeriodLength())
        lblPeriodLengthValue.pack(side= "top", fill= "x", expand= True)

        lblAperiodLengthValue = tk.Label(frmMetricsValues, text= metrics.getAperiodLength())
        lblAperiodLengthValue.pack(side= "top", fill= "x", expand= True)

        lblCircleRatioValue = tk.Label(frmMetricsValues, text= metrics.getCircleRatio())
        lblCircleRatioValue.pack(side= "top", fill= "x", expand= True)