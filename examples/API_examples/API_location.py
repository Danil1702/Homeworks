import requests
import json

def API(lat, lon, radius, number):    
    url = f"https://aerodatabox.p.rapidapi.com/airports/search/location/{lat}/{lon}/km/{radius}/{number}"

    headers = {
        'x-rapidapi-host': "aerodatabox.p.rapidapi.com",
        'x-rapidapi-key': "2bb16f0062msh25be2f08b8ac2eap15e7f2jsn2bb2739b0907"
        }

    response = requests.request("GET", url, headers=headers)
    with open("location.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    API(50.00000, 30.00000, 100, 3)