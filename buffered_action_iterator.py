from typing import Iterator
from types import FunctionType


class BufferedActionIterator(Iterator):
    def __init__(self, iter: Iterator, bufferSize: int, action: FunctionType):
        self.iter = iter
        self.action = action
        self.buffer = [None] * bufferSize
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        next = self.iter.__next__()
        self.counter += 1
        self.buffer[self.counter] = next
        if self.counter == len(self.buffer) - 1:
            self.action(self.buffer)
            self.counter = -1
        return next