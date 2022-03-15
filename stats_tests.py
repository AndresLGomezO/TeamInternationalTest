import unittest
from stats import DataCapture

class DataCaptureTest(unittest.TestCase):

    def test_add(self):
        result=[1,2,3]
        data_capture=DataCapture([])
        data_capture.add(1)
        data_capture.add(2)
        data_capture.add(3)
        self.assertEqual(data_capture.values, result)

class BuildStatsTest(unittest.TestCase):

    def setUp(self):
        self.data_capture=DataCapture([])
        self.data_capture.add(1)
        self.data_capture.add(2)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(5)
        self.data_capture.add(6)
        self.data_capture.add(7)
        self.data_capture.add(8)
        self.data_capture.add(9)
        self.data_capture.add(10)
        self.stats=self.data_capture.build_stats()

    def test_less(self):
        resulti=[1,2,3]
        resultq=3
        stats=self.stats
        resq, items=stats.less(4)
        self.assertEqual(resq, resultq)
        self.assertEqual(items, resulti)
    
    def test_greater(self):
        resulti=[5,6,7,8,9,10]
        resultq=6
        stats=self.stats
        resq, items=stats.greater(4)
        self.assertEqual(resq, resultq)
        self.assertEqual(items, resulti)
    
    def test_between(self):
        resulti=[2,3]
        resultq=2
        stats=self.stats
        resq, items=stats.between(1,4)
        self.assertEqual(resq, resultq)
        self.assertEqual(items, resulti)


if __name__ == '__main__':
    unittest.main()

