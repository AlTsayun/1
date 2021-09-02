class Lemer:
    def __init__(self, a, m, r0):
        self.a = a
        self.m = m
        self.currentR = r0

    def getNext(self):
        self.currentR = self.currentR * self.a % self.m
        return float(self.currentR) / self.m