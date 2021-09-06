from circle_ratio_counter import CircleRatioCounter
import math
from typing import Iterator
class MetricsIterator(Iterator):
    def __init__(self, iter: Iterator, name):
        self.name = name
        self.iter = iter
        self.iterationsCount = 0
        #мат ожидание
        self.expectedValue = 0
        #дисперсия
        self.variance = 0

        self.circleRatioCounter = CircleRatioCounter()

    def __iter__(self):
        return self

    def __next__(self):
        nextItem = next(self.iter)
        count = self.iterationsCount + 1
        self.variance = (self.variance * (count - 2) / (count - 1)  + (nextItem - self.expectedValue) ** 2 / count ) if count != 1 else 0
        self.expectedValue = (self.expectedValue * (count - 1) + nextItem) / count
        self.iterationsCount = count
        self.circleRatioCounter.addElement(nextItem)
        return nextItem

    def getExpectedValue(self):
        return self.expectedValue

    def getVariance(self):
        return self.variance

    #среднее квадратичное отклонение
    def getStandardDeviation(self):
        return math.sqrt(self.variance)
    
    def getCircleRatio(self):
        return self.circleRatioCounter.getCircleRatio()

    def getName(self):
        return self.name
        