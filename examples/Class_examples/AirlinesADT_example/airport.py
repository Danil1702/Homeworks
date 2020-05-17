class Airport:
    '''Abstacat base class representing an airport'''
    def __init__(self, name, location, icao="", average_fligths=0):
        '''
        Initializing new airport

        __init__:str, dict, str, float -> NoneType
        :param name: official name of the airport
        :param location: dictionary containing coordinates of the airport
        :param icao: name in the ICAO database(if it is absent - None)
        :param average_flights: average number of incoming flights 
                                from the chosen airport
        '''
        self._name = name
        self._icao = icao
        self._location = location
        self._average_fligths = average_fligths
    
    def get_description(self):
        '''
        Return basic description of an airport

        get_description: -> tuple
        :return: tuple of airport parameters
        '''
        return (self._name, self._icao, self._location, self._average_fligths)
