import statistics

from StatisticalOperations.mean import Mean
from StatisticalOperations.median import Median

class StatsTest:

    def test_Statistics_Mean(self):
        aList = [4, 5, 6, 7]
        return statistics.mean(aList)

    def test_Statistics_Median(self):
        aList = [4,5,6,7]
        return statistics.median(aList)
