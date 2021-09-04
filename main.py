import math
from event_counter import EventCounter
from buffered_action_iterator import BufferedActionIterator
from bucketized_counter_iterator import BucketizedCounterIterator
from lemer import Lemer
from periodic_metrics_iterator import PeriodicMetricsIterator
from uniform_distribution_metrics import UniformDistributionMetrics

#a = 16807, m = 2147483647
metrics = PeriodicMetricsIterator(Lemer(997,883,1))
bucketizedCounter = BucketizedCounterIterator(metrics, 20, 0, 1)
pointsInCircle = EventCounter()
bufActionIter = BufferedActionIterator(bucketizedCounter, 2, lambda buf: (
        pointsInCircle.emit() if ((buf[0] ** 2) + (buf[1] ** 2)) <= 1 else None
    ))


for x in bufActionIter:
    pass
    # print(x)
print("metrics:")
print(f"expected value:\t\t{metrics.getExpectedValue()}")
print(f"variance:\t\t{metrics.getVariance()}")
print(f"standard deviation:\t{metrics.getStandardDeviation()}")
print(f"period length:\t\t{metrics.getPeriodLen()}")
print(f"aperiod length:\t\t{metrics.getAperiodLen()}")
# todo: fix "circle" ratio
print(f"\"circle\" ratio:\t\t{float(pointsInCircle.getCount()) / len(metrics.getSequence())}")
print(f"pi / 4 ratio:\t\t{math.pi / 4}")

fromInclusive = 0
toInclusive = 1
metrics = UniformDistributionMetrics(fromInclusive, toInclusive)

print("uniform distribution metrics:")
print(f"expected value:\t\t{metrics.getExpectedValue()}")
print(f"variance:\t\t{metrics.getVariance()}")
print(f"standard deviation:\t{metrics.getStandardDeviation()}")

# func = metrics.getCumulativeDistributionFunction()
# print("CumulativeDistributionFunction:")
# for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
#     print(func(i))

# func = metrics.getProbabilityDensityFunction()
# print("ProbabilityDensityFunction:")
# for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
#     print(func(i))

