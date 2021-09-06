import math
class UniformDistributionMetrics:
    def __init__(self, fromInclusive, toInclusive):
        
        self.fromInclusive = fromInclusive
        self.toInclusive = toInclusive

        #мат ожидание
        self.expectedValue = float(fromInclusive + toInclusive) / 2 
        #дисперсия
        self.variance = float(toInclusive - fromInclusive) ** 2 / 12 
        #среднее квадратичное отклонение
        self.standardDeviation =  float(toInclusive - fromInclusive) / (2 * math.sqrt(3))


    def getExpectedValue(self):
        return self.expectedValue

    def getVariance(self):
        return self.variance

    def getStandardDeviation(self):
        return self.standardDeviation

    def getProbabilityDensityFunction(self):
        return lambda x: 0 if (x < self.fromInclusive) or (x > self.toInclusive) else float(1) / (self.toInclusive - self.fromInclusive) 

    def getCumulativeDistributionFunction(self):
        return lambda x: 0 if (x < self.fromInclusive) else 1 if (x > self.toInclusive) else  float(x - self.fromInclusive) / (self.toInclusive - self.fromInclusive) 

    def getCircleRatio(self):
        return math.pi / 4

    def getName(self):
        return "uniform distribution"

    def getPeriodLength(self):
        return None
    
    def getAperiodLength(self):
        return None