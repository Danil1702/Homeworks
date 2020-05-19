from airport import Airport
import unittest


class TestAirport(unittest.TestCase):
    '''class for testing Airport class'''
    def test_init(self):
        airport = Airport("Boryspil", {'lat': 50.8583, 'lon': 34.7625})

        self.assertEqual(airport._icao, "")
        self.assertEqual(airport._average_fligths, 0.0)
        self.assertIsInstance(airport, Airport)

    def test_get_description(self):
        airport = Airport("Boryspil", {'lat': 50.8583, 'lon': 34.7625})

        self.assertEqual(len(airport.get_description()), 4)


if __name__ == "__main__":
    unittest.main()