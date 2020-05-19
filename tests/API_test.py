from API import API_destination, API_location
import unittest


class APITest(unittest.TestCase):
    '''Class for testing API functions'''
    def destination_test(self):
        routes = API_destination("UKHS")

        self.assertIsInstance(routes, dict)
        self.assertEqual(len(routes['routes']), 0)

    def location_test(self):
        airports = API_location(50.9216, 34.80029, 50, 10)

        self.assertIsInstance(airports, dict)
        self.assertEqual(len(airports), 0)    


if __name__ == "__main__":
    unittest.main()   