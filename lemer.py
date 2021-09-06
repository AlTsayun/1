from typing import Iterator


class Lemer(Iterator):
    def __init__(self, a, m, r0):
        self.a = a
        self.m = m
        self.currentR = r0

    def __iter__(self):
        return self

    def __next__(self):
        self.currentR = (self.currentR * self.a) % self.m
        return float(self.currentR) / self.m

    def getFromInclusive(self):
        return 0.0

    def getToInclusive(self):
        return 1.0
