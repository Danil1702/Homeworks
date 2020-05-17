import json
from geopy.geocoders import Nominatim

from API import API_location, API_destination
from arrays import DynamicArray
from airport import Airport 


class AirlinesADT:
    '''
    Abstact class representing AirlinesADT
    Processes data collected from API's and saves the
    results of research using DynamicArray
    '''
    def __init__(self, cityname=None, icao=None):
        '''
        Initializing new AirlinesADT object with 
        cityname and icao parameters are None by default

        ___init___: str, str -> NoneType
        :param cityname: city for doing research
        :param icao: ICAO identifier of the airport chosen by user
        '''
        self._cityname = cityname
        self._icao = icao
        self._location = None
        self._destinations = None
        self._airports_nearby = DynamicArray()
        self._routes_available = DynamicArray()
 
    def get_nearby_airports(self):
        '''
        Defines the coordinates of the given city.
        Searches for nearby airports using API_location
        Saves result of the research in  dynamic array

        airports_nearby: array of Airport objects - airports
                         found using API_location
        '''
        geolocator = Nominatim(user_agent="airport finder")
        location = geolocator.geocode(self._cityname)
        self._location = API_location(location.latitude, 
                                      location.longitude, 50, 10)  
        
        for airport in self._location['items']:
            name = airport['name']
            icao = airport['icao'] 
            location = airport['location']
            self._airports_nearby.append(Airport(name, location, icao)) 
    
    def get_routes_available(self):      
        '''
        Searches for avaliable routes and average 
        number of daily flights  from the chosen airport
        (ICAO identifier)in these directions using API_destination
        If any of the parameters (name, location, average flights)
        is absent, the route is skipped

        routes_available: array of Airport objects - directions
                          available for travelling                        
        '''
        self._destinations = API_destination(self._icao)

        for route in self._destinations['routes']:
            try:
                location = route['destination']['location']
                name = route['destination']['name']
                average_flights = route['averageDailyFlights']
                self._routes_available.append(Airport(name, location, 
                                             average_fligths=average_flights)) 
            except KeyError:
                pass


if __name__ == "__main__":
    airlines = AirlinesADT("London")
    airlines.get_nearby_airports()

    for airport in airlines._airports_nearby:
        print(airport.get_description())

    print("-----------------------------------------------------------------")

    airlines._icao = "UKBB" 
    airlines.get_routes_available()

    for airport in airlines._routes_available:
        print(airport.get_description()) 