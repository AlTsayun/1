from lemer import Lemer
from sequence_metrics import SequenceMetrics

lemer = Lemer(3,5,1)

sequence = [lemer.getNext() for i in range(0,5)]
print(sequence)
metrics = SequenceMetrics(sequence)
print(metrics.getExpectedValue())
print(metrics.getVariance())
print(metrics.getStandardDeviation())