import math
from typing import Iterator


class BucketizedCounterIterator(Iterator):
    def __init__(self, iter: Iterator, bucketsCount: int,  fromInclusive, toInclusive):
        self.iter = iter
        self.buckets = [0] * bucketsCount
        self.fromInclusive = fromInclusive
        self.toInclusive = toInclusive

    def __iter__(self):
        return self

    def __next__(self):
        nextItem = next(self.iter)
        self.buckets[math.floor(nextItem / ((self.toInclusive - self.fromInclusive) / len(self.buckets)))] += 1
        return nextItem

    def getBuckets(self):
        return self.buckets

    def getFromInclusive(self):
        return self.fromInclusive

    def getToInclusive(self):
        return self.toInclusive

    