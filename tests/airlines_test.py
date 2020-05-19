from airlines_ADT import AirlinesADT, DynamicArray
import unittest


class TestAirlinesADT(unittest.TestCase):
    '''Class for testing AirlinesADT'''
    def test_init(self):
        airlines = AirlinesADT(icao="UKBB")
        
        self.assertIsNone(airlines._cityname)
        self.assertLessEqual(airlines._icao, "UKBB")

    def test_nearby_airports(self):
        airlines = AirlinesADT(cityname="Sumy")
        airlines.get_nearby_airports()

        airport_list = []
        for airport in airlines._airports_nearby:
            airport_list.append(airport.get_description())

        self.assertEqual(airport_list,\
                    [('Sumy', 'UKHS', {'lat': 50.8583, 'lon': 34.7625}, 0)])
        self.assertIsInstance(airlines._airports_nearby, DynamicArray)

    def test_routes_available(self):
        airlines = AirlinesADT(icao="UKBB")   
        airlines.get_routes_available()         

        airport_list = []
        for airport in airlines._routes_available:
            airport_list.append(airport.get_description())

        self.assertEqual(airport_list[0],\
                        ('Istanbul, Istanbul', '',\
                        {'lat': 41.2752762, 'lon': 28.7519436}, 5.43))
        self.assertIsInstance(airlines._routes_available, DynamicArray)    


if __name__ == "__main__":
    unittest.main()        


