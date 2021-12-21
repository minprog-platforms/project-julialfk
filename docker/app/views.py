from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user, login_required
import random
import json

from . import db
from app import cache
from .models import Random_restaurant, Saved_restaurant


views = Blueprint('views', __name__)

API_KEY = "AIzaSyC-2_Gt3pY8MwACEdVZBEXA4xHkIHAlFys"


@views.route('/', methods=['GET', 'POST'])
def home():
# returns an API request url if 'Search' or 'Retry' are clicked
    if request.method == 'POST':
        if request.form['submit'] == 'Search':
            restaurant_url = first_search()

            return render_template("home.html", restaurant_url=restaurant_url, user=current_user)
        elif request.form['submit'] == 'Retry':
            restaurant_url = retry_search()

            return render_template("home.html", restaurant_url=restaurant_url, user=current_user)

    return render_template("home.html", user=current_user)


def first_search():
# takes input from user and returns a random restaurant url
    # get conditions from form
    location = request.form.get('location')
    rating = request.form.get('rating')

    # flash errors if form is filled in incorrectly
    if len(location) < 2:
        flash("Location must be longer than 1 character.", category='error')
    elif bool(rating) == False:
        flash("Please enter a minimum rating.", category='error')
    else:
        try:
            # create new search object and run API requests
            search = Random_restaurant(location, rating)
            current_coords = search.current_coords()
            restaurant_data = search.nearby_search(current_coords, search._rating)

            # cache list of restaurant names and ids
            cache.set('restaurants', json.dumps(restaurant_data))

            # take random set of restaurant name and id
            random_restaurant = randomize(restaurant_data)
            restaurant_id = random_restaurant['id']
            restaurant_url = f"https://www.google.com/maps/search/?api=1&query=Google&query_place_id={restaurant_id}&key={API_KEY}"

            # check if this restaurant has been saved before if user is logged in
            if current_user.is_authenticated:
                save_restaurant(random_restaurant, restaurant_url)

            flash("Restaurant found!", category='success')

            return restaurant_url
        except:
            flash("No nearby restaurants found with these conditions. Please try again with a different input.", category='error')


def retry_search():
# takes cached information from previous input and outputs a new random restaurant
    try:
        # load cached list of restaurants
        restaurant_data = json.loads(cache.get('restaurants'))

        # take a random restaurant from the list and create url
        random_restaurant = randomize(restaurant_data)
        restaurant_id = random_restaurant['id']
        restaurant_url = f"https://www.google.com/maps/search/?api=1&query=Google&query_place_id={restaurant_id}&key={API_KEY}"

        # check if this restaurant has been saved before if user is logged in
        if current_user.is_authenticated:
            save_restaurant(random_restaurant, restaurant_url)

        flash("Restaurant found!", category='success')

        return restaurant_url
    except:
        flash("No previous input found. Please submit new input.", category='error')


def randomize(restaurant_data):
# takes a random id from the list
    restaurant_number = len(restaurant_data)
    n = random.randint(0, restaurant_number)

    random_restaurant = restaurant_data[n]

    return random_restaurant


def save_restaurant(random_restaurant, restaurant_url):
# checks if restaurant is saved yet and saves it if not
    saved_restaurant = Saved_restaurant.query.filter_by(place_url=restaurant_url).first()

    if not saved_restaurant:
        restaurant_name = random_restaurant['name']
        new_saved = Saved_restaurant(place_name=restaurant_name, place_url=restaurant_url, user_id=current_user.id)
        db.session.add(new_saved)
        db.session.commit()


@views.route('/saved')
@login_required
def saved():
# page with all previously generated links to restaurants
    return render_template("saved.html", user=current_user)


@views.route('/delete-saved', methods=['POST'])
def delete_saved():
# page that deletes a note when prompted
    saved_restaurant = json.loads(request.data)
    restaurant_id = saved_restaurant
    saved_restaurant = Saved_restaurant.query.get(restaurant_id)

    if saved_restaurant:
        if saved_restaurant.user_id == current_user.id:
            db.session.delete(saved_restaurant)
            db.session.commit()

    return jsonify({})
