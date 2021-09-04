from lemer import Lemer
from periodic_metrics_iterator import PeriodicMetricsIterator
from uniform_distribution_metrics import UniformDistributionMetrics

metrics = PeriodicMetricsIterator(Lemer(3,5,1))
for x in metrics:
    print(x)
print(metrics.getExpectedValue())
print(metrics.getVariance())
print(metrics.getStandardDeviation())
print(metrics.getPeriodLen())
print(metrics.getAperiodLen())

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

