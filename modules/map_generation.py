import folium


def map_building(destination_list, airport):
    '''
    Function for building a web map with four layers
    1. Markers - airports(darkblue - chosen airport, from green
    to red - destinations)
    2. Distribution of passenger airtransport
    3. Distribution of freight airtransport
    4. Overall distribution of airtransport

    map_building: list, Airport -> file
    :param destination_list: list of Airports -
                             available routes from airport
    :param airport: airport chosen for research                         
    '''
    map = folium.Map(
        location=[airport._location['lat'], airport._location['lon']],
        zoom_start=4
        )

    folium.Marker(
        location=[airport._location['lat'], airport._location['lon']], 
        popup= airport._name, 
        icon=folium.Icon(color= "darkblue")
        ).add_to(map)
    
    def set_color(airport):
        '''
        Helper function for defining the color
        of the marker according to number of average 
        daily incoming flights

        set_color: Airport -> str
        '''
        if airport._average_fligths <= 0.5:
            return "green"
        elif airport._average_fligths <= 1:
            return "orange" 
        else:
            return "red"      
    
    fg_airports = folium.FeatureGroup(name="Destinations", control= False)
  
    for airport in destination_list:   
        fg_airports.add_child(folium.Marker(
        location= [airport._location['lat'], airport._location['lon']],
        popup= f"{airport._name}Average Daily Flights:{airport._average_fligths}",
        icon=folium.Icon(color= set_color(airport))))
    

    fg_psn = folium.FeatureGroup(name="Passenger", overlay=False)
    fg_psn.add_child(
        folium.GeoJson(
            data=open('Statistics/Files/data.json', 'r', encoding='utf-8-sig').read(),
            style_function=lambda x:{
                'fillColor':'green'
                if x['properties']['passengers'] < 5*(10**7)
                else 'orange' if 5*(10**7) <= x['properties']['passengers'] < 10**9
                else 'red'
                }
            )
        )
        
    fg_fr = folium.FeatureGroup(name="Freight", overlay=False)
    fg_fr.add_child(
        folium.GeoJson(
            data=open('Statistics/Files/data.json', 'r',encoding='utf-8-sig').read(),
            style_function=lambda x:{
                'fillColor':'green'
                if x['properties']['freight'] < 1500
                else 'orange' if 1500 <= x['properties']['freight'] < 150000
                else 'red'
                }
            )
        ) 
        
    fg_ov = folium.FeatureGroup(name="Overall")
    fg_ov.add_child(
        folium.GeoJson(
            data=open('Statistics/Files/data.json', 'r', encoding='utf-8-sig').read(),
            style_function=lambda x:{
                'fillColor':'green'
                if x['properties']['overall'] < 50001500
                else 'orange' if 50001500 <= x['properties']['overall'] < 1000150000
                else 'red'
                }
            )
        )        

    map.add_child(fg_airports)
    map.add_child(fg_psn)   
    map.add_child(fg_fr)
    map.add_child(fg_ov)   
    map.add_child(folium.LayerControl())
    map.save("templates/map.html")






   

