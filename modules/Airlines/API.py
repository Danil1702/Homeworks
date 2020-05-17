import requests
import json


def API_location(lat, lon, radius, number):    
    '''
    API for searching for airports which are
    around certain location(defined by coordinates) 

    API_location: float, float, int, int -> dict
    :param lat: latitude of certain location
    :param lon: longitude of certain location
    :param radius: maximum radius of search
    :param number: take no more than number airports
    :return: dictionary of airports found in th area 
             around location
    '''
    url = f"https://aerodatabox.p.rapidapi.com/airports/search/location/{lat}/{lon}/km/{radius}/{number}"

    headers = {
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
        'x-rapidapi-key': "2bb16f0062msh25be2f08b8ac2eap15e7f2jsn2bb2739b0907"
        }

    response = requests.request("GET", url, headers=headers)
    return response.json()


def API_destination(icao):    
    '''
    API for recieving the information about 
    the available routes from certain airport
    (defined by the given ICAO identifier)
    and the average number of daily flights
    in each direction

    API_destination: str -> dict
    :param icao: airport identifier in ICAO
    :return: dictionary of available routes 
    '''
    url = f"https://aerodatabox.p.rapidapi.com/airports/icao/{icao}/stats/routes/daily"

    headers = {
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
        'x-rapidapi-key': "2bb16f0062msh25be2f08b8ac2eap15e7f2jsn2bb2739b0907"
        }

    response = requests.request("GET", url, headers=headers)
    return response.json()