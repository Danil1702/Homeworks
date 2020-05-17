from flask import Flask, render_template, request, redirect, url_for
from map_generation import map_building
from Airlines.airlines_ADT import AirlinesADT


app = Flask(__name__)
list_of_visited = []


@app.route("/")
def index1():
    '''
    Launches homepage 
    '''
    return render_template("index1.html")


@app.route("/repeat")
def index3():
    '''
    Launches page used in unexpected situations
    '''
    return render_template("index3.html")    


@app.route("/airports", methods=['POST', 'GET'])
def airport_search():
    '''
    Lauches page with a choice form
    '''
    if request.method == "POST":
        cityname = request.form['user']
        locator = AirlinesADT(cityname)     
        try:       
            locator.get_nearby_airports()      
            
            if not locator._airports_nearby:
                raise ValueError
            
            list_of_visited.append(locator._airports_nearby)   
            airports = [airport._name for airport in locator._airports_nearby]            
            return render_template("index2.html", airports=airports)      
        except:
            return redirect(url_for('index3'))        


@app.route("/map", methods=['POST', 'GET'])
def map():
    '''
    Lauches map generation and redirects for webmap
    '''
    if request.method == "POST":
        chosen_airport = None
        airport_name = request.form['user']
        
        for airport in list_of_visited[-1]:
            if airport._name == airport_name:
                chosen_airport = airport
        
        try:    
            routes = AirlinesADT(icao=chosen_airport._icao)
            routes.get_routes_available()
        except:
            return redirect(url_for('index3')) 

        map_building(routes._routes_available, chosen_airport)
        return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True) 