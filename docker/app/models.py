from urllib.request import urlopen
from time import sleep
from flask_login import UserMixin
from sqlalchemy.sql import func
import json

from . import db


API_KEY = "AIzaSyC-2_Gt3pY8MwACEdVZBEXA4xHkIHAlFys"

class Saved_restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(10000))
    place_url = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    saved = db.relationship('Saved_restaurant')
    
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
        
        restaurant_data = []

        while True:
            json_response = urlopen(search_url)
            data_search = json.load(json_response)

            # add all relevant place_ids to list
            all_restaurants = data_search['results']
            get_ids(all_restaurants, restaurant_data, rating)

            # goes to next page if available
            if 'next_page_token' in data_search:
                pagetoken = data_search['next_page_token']
                search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={pagetoken}&key={API_KEY}"
                sleep(1.5)
            else:
                break

        return restaurant_data


def get_ids(all_restaurants, restaurant_data, rating):
    # looks for restaurants meeting the conditions and adds them to a list
    for restaurant in all_restaurants:
        single_restaurant = {}

        if restaurant['business_status'] == "OPERATIONAL" and restaurant['rating'] >= float(rating) and "lodging" not in restaurant['types']:
            single_restaurant['name'] = restaurant['name']
            single_restaurant['id'] = restaurant['place_id']
            restaurant_data.append(single_restaurant)


