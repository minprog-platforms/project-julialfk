from flask import Blueprint, render_template, request, flash
from webbrowser import open_new_tab

from .models import Random_restaurant


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        location = request.form.get('location')
        rating = request.form.get('rating')

        if len(location) < 2:
            flash("Location must be longer than 1 character.", category='error')
        elif bool(rating) == False:
            flash("Please enter a minimum rating.", category='error')
        else:
            search = Random_restaurant(location, rating)
            current_coords = search.current_coords()
            restaurant_ids = search.nearby_search(current_coords, search._rating)

            if len(restaurant_ids) < 1:
                flash("No nearby restaurants found with these conditions.\nPlease try again with a different input.", category='error')
            else:
                restaurant_url = search.randomize(restaurant_ids)
                flash(f"Restaurant found!", category='success')

                open_new_tab(restaurant_url)

    return render_template("home.html")