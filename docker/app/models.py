from urllib.request import urlopen

import json
import random

API_KEY = "AIzaSyC-2_Gt3pY8MwACEdVZBEXA4xHkIHAlFys"
location = "Leidseplein Amsterdam"
rating = "4"

class Random_restaurant:

    def __init__(self, location, rating):
        self._location = location
        self._rating = rating

    # looks up coordinates of current location
    def current_coords(self):

        # reformat prompted location string
        address = self._location.replace(" ", "%20")

        # request json data from Geocoding API
        geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
        json_response = urlopen(geocoding_url)
        data_geocoding = json.load(json_response)

        # select relevant info for coordinates and reformat
        coordinates_dict = data_geocoding['results'][0]['geometry']['location']
        coordinates_str = str(coordinates_dict['lat']) + "%2C" + str(coordinates_dict['lng'])

        return coordinates_str

    def nearby_search(self, current_coords, rating):

        # request json data of nearby restaurants from Places API
        search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={current_coords}&radius=1000&type=restaurant&key={API_KEY}"
        json_response = urlopen(search_url)
        data_search = json.load(json_response)

        # add all relevant place_ids to list
        all_restaurants = data_search['results']
        restaurant_ids = []

        for restaurant in all_restaurants:
            if restaurant['business_status'] == "OPERATIONAL" and restaurant['rating'] >= float(rating) and "lodging" not in restaurant['types']:
                restaurant_ids.append(restaurant['place_id'])

        return restaurant_ids

    def randomize(self, restaurant_ids):
        
        # take a random id from the list
        restaurant_number = len(restaurant_ids)
        n = random.randint(0, restaurant_number)

        restaurant = restaurant_ids[n]

        restaurant_url = f"https://www.google.com/maps/search/?api=1&query=Google&query_place_id={restaurant}&key={API_KEY}"

        return restaurant_url
