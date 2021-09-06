from gui.lemer_hist_window import LemerHistWindow
from metrics_iterator import MetricsIterator
from gui.sequence_metrics_window import PeriodicMetricsWindow
from typing import Iterator
from gui.loading_window import LoadingWindow
from gui.lemer_input_window import LemerInputWindow

from threading import Thread

from event_counter import EventCounter
from buffered_action_iterator import BufferedActionIterator
from bucketized_counter_iterator import BucketizedCounterIterator
from lemer import Lemer
from periodic_metrics_iterator import PeriodicMetricsIterator
from uniform_distribution_metrics import UniformDistributionMetrics

def calculateLemerMetrics(a, m, r0, bucketsCount):
    print("calculate")
    #a = 16807, m = 2147483647
    #a = 105491, m = 1999999, r0 = 20441
    #a = 2803, m = 4999, r0 = 1097

    lemer = Lemer(a, m, r0)

    def iterate(lemer: Iterator):

        isCancelled = False

        def cancel():
            nonlocal isCancelled
            isCancelled = True

        loadingWindow = LoadingWindow(cancelAction= cancel)

        fromInclusive = lemer.getFromInclusive()
        toInclusive = lemer.getToInclusive()
        metrics = PeriodicMetricsIterator(lemer, "Lemer distribution")
        bucketizedCounter = BucketizedCounterIterator(metrics, bucketsCount, fromInclusive, toInclusive)

        for _ in bucketizedCounter:
            if isCancelled:
                return
        
        loadingWindow.destroy()

        PeriodicMetricsWindow(metrics)
        PeriodicMetricsWindow(UniformDistributionMetrics(fromInclusive, toInclusive))
        LemerHistWindow(bucketizedCounter.getBuckets(), fromInclusive, toInclusive)

        # def plotLemerHist(buckets, fromInclusive, toInclusive):
            
        #     bucketsCount = len(buckets)
        #     fig, ax = plt.subplots()
        #     plt.title("Lemer distribution histogram")
        #     bucketsSum = sum(buckets)
        #     step = (toInclusive - fromInclusive) / bucketsCount
        #     bins = np.arange(fromInclusive, toInclusive + step / 2, step= step)
        #     ax.hist(bins[:-1], bins= bins, weights= [float(x) / bucketsSum for x in buckets])
        #     averageY = 1.0 / bucketsCount
        #     ax.hlines(averageY, fromInclusive, toInclusive, color= "green")
        #     ax.text(0, averageY, "1/m", ha='right', va='center')
        #     plt.show()

        # p = Process(target= plotLemerHist, args= (bucketizedCounter.getBuckets(), fromInclusive, toInclusive))
        # p.start()


    executingThread = Thread(target= iterate, args= (lemer,))
    executingThread.start()

inputWindow = LemerInputWindow(lambda a, m, r0: calculateLemerMetrics(a, m, r0, 20) )
inputWindow.mainloop()