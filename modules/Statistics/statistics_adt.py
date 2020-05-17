from arrays import Array, Array2D
import csv
import json


class StatisticsADT:
    '''Abstract class representing StatisticsADT'''
    STATISTICS = {}
    
    def __init__(self, filename, key):
        '''
        Initializing new file for research

        __init__: str, str -> NoneType
        :param filename: name of the csv file
        :param key: type of the content of the file
        '''
        self._filename = filename
        self._key = key
        self.read_file()
        self.country_summary()

    def read_file(self):
        '''
        Reading the csv and saving its content
        into 2D array

        contents: 2D array with data from csv table
        '''
        with open(self._filename, "r") as f:    
            reader = csv.reader(f)   
            contents = Array2D(264, 64)
            
            i = 0
            for row in reader:
                if len(row) > 3 and row[0] != "Country Name":
                    for j in range(64):
                        contents[(i, j)] = row[j]
                    i += 1    

        self._contents = contents
    
    def country_summary(self):
        '''
        Processing the content of csv file.
        Summarizing the quantity of air traffic
        of all years and saving the results into new 2D array

        Adding the result of the research to class dictionary
        '''
        countries_sum = Array2D(264, 2)
        
        for i in range(264):
            countries_sum[(i, 0)] = self._contents[(i, 0)]
            
            summary = 0 
            for j in range(5, 64):
                summary += float("0" + self._contents[(i, j)])
            countries_sum[(i, 1)] = summary
        
        self._countries_sum = countries_sum
        StatisticsADT.STATISTICS[self._key] = self._countries_sum

    @staticmethod
    def overall_statistics():
        '''
        Summarizing all the statistics collected into
        one overall statistics (2D array)
        
        Adding the result to class dictionary 
        '''
        overall_stat = Array2D(264, 2)
        overall_stat.clear(0)
        
        for key in StatisticsADT.STATISTICS:
            for i in range(264):
                overall_stat[(i, 0)] = StatisticsADT.STATISTICS[key][(i, 0)]
                overall_stat[(i, 1)] += StatisticsADT.STATISTICS[key][(i, 1)]

        StatisticsADT.STATISTICS['overall'] = overall_stat   
    
    @staticmethod
    def write_data():
        '''
        Adding all the statistics from class
        dictionary to a json file content
        '''                
        with open('Files/world.json', 'r', encoding="utf-8-sig") as f:
            decoded = json.load(f)

            world_dict = {}
            for country in decoded['features']:
                properties = {}
                properties['geometry'] = country['geometry']
                properties['passengers'] = 0
                properties['freight'] = 0
                properties['overall'] = 0
                world_dict[country['properties']['NAME']] = properties

        for key in StatisticsADT.STATISTICS:
            stat = StatisticsADT.STATISTICS[key]
            for i in range(264):
                if stat[(i, 0)] in world_dict:
                    world_dict[stat[(i, 0)]][key] = stat[(i, 1)]     
       
        with open('Files/data.json', 'w', encoding="utf-8-sig") as f:
            json.dump(world_dict, f, indent=4, ensure_ascii=False) 


if __name__ == "__main__":
    freight = StatisticsADT("Files/freight_ton.csv", 'freight')
    passenger = StatisticsADT("Files/passenger_number.csv", 'passengers')
    passenger.overall_statistics()
    passenger.write_data()
    

    