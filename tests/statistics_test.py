from statistics_adt import StatisticsADT, Array2D
import unittest


class TestStatisticsADT(unittest.TestCase):
    '''Testing Statistics ADT class'''
    def test_class(self):
        stat = StatisticsADT("freight_ton.csv", 'freight')

        self.assertEqual(stat._key, "freight")
        self.assertIsInstance(stat, StatisticsADT)
        
        self.assertIsInstance(stat._contents, Array2D)
        self.assertIsInstance(stat._countries_sum, Array2D)

        stat1 = StatisticsADT("passenger_number.csv", 'passenger')
        stat1.overall_statistics()

        self.assertEqual(len(stat1.STATISTICS), 3)


if __name__ == "__main__":
    unittest.main()


