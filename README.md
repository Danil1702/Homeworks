# Homeworks
## Interactive map of internatinal airlines

***Description***

Provides a web app for generating an interactive map of internatinal airlines
from the chosen airport. The map helps to distinguish the most popular destinations
from the chosen airport and in general define most commonly used airlines.
On the whole, map helps to understand which countries are among the first to use
air transport and which places of the Earth are the least connected with others by air.

Web app asks the user to choose any city for research. Then, user has to choose one airport
from a number of airports forund in the in the area of the chosen city. Finally, web app 
generates the *folium* world map presenting:
1. The quantity of using air transport (passenger, freight, both) in each country. 
(country color from green to red with the growth of air transport prevalance)
2. Markers - available routes to fly from the chosen airport (blue marker).
(marker color from green to red according to the rising number of daily flights
in this destionation)

---
***Contents***

* **docs**

Directory containing text documents (reports on completing parts of homework).

1. **Diagrams: **

Directory with UMl diagrams of all abstract data types (ADT) and
data structures used in the project.

2. **Video: **

Directory containing video representation of the 
usage of the project.

* **examples**

Directory containing example programs, as parts of certain tasks.

1. **API_examples: **

Contains python modules - examples of using APIs, which were provided in the project.

2. **Class_examples: **

Contains python modules - examples of using classes (Abstract Data Types), which
were implemented in the project.

3. **Modules_examples: **
Contains python modules - examples of using JSON and CSV libraries for reading and 
writing ''.json'' and ''.csv'' files.

* **modules**

Directory containing programming modules - direct components of final program.

1. **Airlines: **
Directory containing implementation of Airlines ADT

''airlines_ADT.py: '' - class implementing Airlines ADt

''API.py: '' - contains functions for finding the airports in the area of certain city
(API_location) and available routes to fly (API_destination)

''airport.py: '' - class Airport (helper class for Airlines ADT)

''arrays.py: '' - class Array and class DynamicArray (data structures used in Airlines ADT)

[Full description](https://github.com/Danil1702/Homeworks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)

2. **Statistics**
Directory containing implementation of Statistics ADT

''statistics_adt.py: '' - class implementing Statistics ADT

''arrays.py: '' - class Array and class Array2D (data structures used in Statistics ADT)

''Files: '' - files containing data for research

[Full description](https://github.com/Danil1702/Homeworks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)


3. **static: **
Directory containing components for generating HTML pages used in web app.

4. **templates: **
Directory containing HTML pages used in web app.

''index1.html: '' - introductory page with a forn for choosing a city.

''index2.html: '' - page for choosing the airport from the options provided.

''index3.html: '' - page rendered in case of any unexpected error.

''map.html: '' - html representation of folium map (generated after every request of the user)

5. **app.py: ** - module for launching the web app and   components of the project

6. **map_generation.py: ** - building folium map and saving it in file 'map.html'

* **tests**

Directory containing test modules for final program.
