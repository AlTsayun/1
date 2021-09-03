import math
class SequenceMetrics:
    def __init__(self, sequence: list):
        self.sequence = sequence
        #мат ожидание
        self.expectedValue = None 
        #дисперсия
        self.variance = None
        #среднее квадратичное отклонение
        self.standardDeviation = None

    def getExpectedValue(self):
        if (self.expectedValue == None):
            self.expectedValue = float(sum(self.sequence)) / len(self.sequence)
        return self.expectedValue

    def getVariance(self):
        if (self.variance == None):
            expectedValue = self.getExpectedValue()
            self.variance = float(sum([i - expectedValue ** 2 for i in self.sequence])) / len(self.sequence)
        return self.variance


    def getStandardDeviation(self):
        if (self.standardDeviation == None):
            self.standardDeviation = math.sqrt(self.getVariance())
        return self.standardDeviation