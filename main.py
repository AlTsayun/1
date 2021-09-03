from lemer import Lemer
from sequence_metrics import SequenceMetrics
from uniform_distribution_metrics import UniformDistributionMetrics

lemer = Lemer(3,5,3)

sequence = [lemer.getNext() for i in range(0,50)]
print(sequence)
metrics = SequenceMetrics(sequence)
print(metrics.getExpectedValue())
print(metrics.getVariance())
print(metrics.getStandardDeviation())

fromInclusive = 0
toInclusive = 1
metrics = UniformDistributionMetrics(fromInclusive, toInclusive)

print(metrics.getExpectedValue())
print(metrics.getVariance())
print(metrics.getStandardDeviation())

func = metrics.getCumulativeDistributionFunction()
print("CumulativeDistributionFunction:")
for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    print(func(i))

func = metrics.getProbabilityDensityFunction()
print("ProbabilityDensityFunction:")
for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    print(func(i))

