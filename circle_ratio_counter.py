class CircleRatioCounter():
    def __init__(self):
        self.buffer = [None] * 2
        self.inCircleCounter = 0
        self.counter = 0
    
    def addElement(self, e):
        self.counter += 1
        self.buffer[self.counter % len(self.buffer) - 1] = e
        if self.counter % len(self.buffer) == 0:
            self.addPoint(self.buffer[0], self.buffer[1])
            
    def addPoint(self, x, y):
        if ((x ** 2) + (y ** 2)) < 1:
            self.inCircleCounter += 1
    
    def getCircleRatio(self):
        return self.inCircleCounter * 2 / self.counter