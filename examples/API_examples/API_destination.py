import requests
import json

def API(icao):    
    url = f"https://aerodatabox.p.rapidapi.com/airports/icao/{icao}/stats/routes/daily"

    headers = {
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
        'x-rapidapi-key': "2bb16f0062msh25be2f08b8ac2eap15e7f2jsn2bb2739b0907"
        }

    response = requests.request("GET", url, headers=headers)
    with open("destination.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    API("UKBB")        


