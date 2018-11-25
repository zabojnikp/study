#!/usr/bin/env python3

''' This module gets locations details from Kiwi.com API based on location type (eg.: aiports, station, country, ...), 
selected country code and displays related info based on options.
>>> opts = {'cities': None, 'coordinates': None, 'iata': True, 'names': True, 'full': None}
>>> UK_airports = Locations(opts)
>>> print(UK_airports.country_code + "," + UK_airports.location_type)
GB,airport
>>> UK_stations = Locations(opts, location_type='station')
>>> print(UK_stations.country_code + "," + UK_stations.location_type)
GB,station
>>> CZ_airports = Locations(opts, country_code='CZ')
>>> print(CZ_airports.country_code + "," + CZ_airports.location_type)
CZ,airport'''

import requests
from pprint import pprint

class Locations:
    __api_url = "https://api.skypicker.com/locations"
    
    def __init__(self, options, country_code="GB", location_type='airport'):
        '''Creates an instance of data type: Locations. country code:'GB' and location_type:'airport' are set 
        as default values'''
        self.country_code = country_code
        self.location_type = location_type
        self.__options = options 

    def __download_locations(self): 
        '''This private method connects to Kiwi.com locations API and returns json file with all details to specific location type and country.'''
        parameters = dict(type="subentity", term=self.country_code, location_types=self.location_type, limit=1000)
        response = requests.get(self.__api_url, params=parameters)
        print(response.status_code)
        assert response.status_code in (200, 301), "Incorrect reponse status code, please check your request."
        json_data = response.json()
        locations_data = json_data["locations"]
        assert locations_data, "There are no {0} locations for {1} country".format(self.location_type, self.country_code)
        return locations_data
    
    def __map_locations(self, locations_data):
        '''This private method maps locations data to dictionary based on defined options and returns dictionary'''
        locations_details = dict()
        for i in range(0, len(locations_data)):
            locations_details[i] = {}
            if self.__options.full:
                locations_details[i] = locations_data[i]
                continue
            if self.__options.names:
                locations_details[i]['name'] = locations_data[i]["name"]
            if self.__options.iata:
                locations_details[i]['iata'] = locations_data[i]["code"]
            if self.__options.coordinates:
                locations_details[i]['coordinates'] = locations_data[i]["location"]
            if self.__options.cities:
                locations_details[i]['city'] = locations_data[i]["city"]['name']
        return locations_details

    def print_locations(self):
        '''This method prints location dictionary created by private mapping method'''
        locations_json = self.__download_locations()
        locations_dict = self.__map_locations(locations_json)
        for k in locations_dict.keys():
            pprint(locations_dict.get(k))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
