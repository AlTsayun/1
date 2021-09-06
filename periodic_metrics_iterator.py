from typing import Iterator
from metrics_iterator import MetricsIterator

class PeriodicMetricsIterator(MetricsIterator):

    def __init__(self, iter: Iterator, name):
        super().__init__(iter, name)
        self.aperiodLen = None
        self.periodLen = None
        self.sequence = list()

    def __iter__(self):
        return self

    def __next__(self):
        nextItem = super().__next__()
        try:
            occurencePos = self.sequence.index(nextItem)

            self.aperiodLen = occurencePos
            self.periodLen = len(self.sequence) - occurencePos
            raise StopIteration
        except ValueError:
            self.sequence.append(nextItem)
            return nextItem

    def getPeriodLength(self):
        return self.periodLen

    def getAperiodLength(self):
        return self.aperiodLen

    def getSequence(self):
        return self.sequence