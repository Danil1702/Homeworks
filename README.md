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

1. __Diagrams:__

Directory with UMl diagrams of all abstract data types (ADT) and
data structures used in the project.

2. __Video:__

Directory containing video representation of the 
usage of the project.

* **examples**

Directory containing example programs, as parts of certain tasks.

1. __API_examples:__

Contains python modules - examples of using APIs, which were provided in the project.

2. __Class_examples:__

Contains python modules - examples of using classes (Abstract Data Types), which
were implemented in the project.

3. __Modules_examples:__

Contains python modules - examples of using JSON and CSV libraries for reading and 
writing _.json_ and _.csv_ files.

* **modules**

Directory containing programming modules - direct components of final program.

1. __Airlines:__

Directory containing implementation of Airlines ADT

_airlines_ADT.py:_ - class implementing Airlines ADt

_API.py:_ - contains functions for finding the airports in the area of certain city
(API_location) and available routes to fly (API_destination)

_airport.py:_ - class Airport (helper class for Airlines ADT)

_arrays.py:_ - class Array and class DynamicArray (data structures used in Airlines ADT)

[Full description](https://github.com/Danil1702/Homeworks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)

2. __Statistics__

Directory containing implementation of Statistics ADT

_statistics_adt.py:_ - class implementing Statistics ADT

_arrays.py:_ - class Array and class Array2D (data structures used in Statistics ADT)

_Files:_ - files containing data for research

[Full description](https://github.com/Danil1702/Homeworks/wiki/%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)


3. __static:__

Directory containing components for generating HTML pages used in web app.

4. __templates:__

Directory containing HTML pages used in web app.

_index1.html:_ - introductory page with a forn for choosing a city.

_index2.html:_ - page for choosing the airport from the options provided.

_index3.html:_ - page rendered in case of any unexpected error.

_map.html:_ - html representation of folium map (generated after every request of the user)

5. _app.py:_ - module for launching the web app and   components of the project

6. _map_generation.py:_ - building folium map and saving it in file 'map.html'

* **tests**

Directory containing test modules for final program.

_API_test.py_ - testing module for _API.py_
_airlines_test.py_ - testing module for _airlines_ADT.py_
_airport_test.py_ - testing module for _airport.py_
_arrays_test.py_ - testing module for _arrays.py_ in __Statistics__ and __Airlines__
_statistics_test.py_ - testing module for _statistics_adt.py_
