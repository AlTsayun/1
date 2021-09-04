from types import FunctionType

class EventCounter:
    def __init__(self):
        self.count = 0

    def emit(self):
        self.count += 1

    def getCount(self):
        return self.count