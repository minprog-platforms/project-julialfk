# Restaurant Randomizer

[Screencast](https://youtu.be/y3OMFDob1Lw)

This program is a web application that redirects you to a random Google Maps page of a restaurant nearby a prompted location. Users can utilize this app if they have trouble deciding a restaurant to go to.

Users can also create an account to save all the links they have been redirected to.

## Installation

To use this program, you need a Google API key. You can generate a key by following [this guide](https://developers.google.com/maps/documentation/javascript/get-api-key). Copy this repository into your desired directory.

When all files are copied, open up `models.py` and `views.py` and replace {YOUR_KEY} with your generated API key. It might also be a good idea to change the configured secret key in `__init__.py`.

If you are using Docker to run this image, move to `path_to_your_directory/project-julialfk/docker` and run the following command:

```bash
docker-compose up -d
```

If you are using Python, simply run `main.py`.

The web app will now run on the server on port 5000.

## Usage

On the homepage, you can find a short form, in which the user can fill in a location and a minimum rating for the restaurant you are looking for. After clicking "Search", a Google Maps page with information about a random restaurant nearby will open in a new window (this might take a few seconds).

If the user is not happy with the restaurant they are redirected to, they can click on the "Retry" button to look for a new restaurant with the same parameters.

If the error "No nearby restaurants found with these conditions. Please try again with a different input." occurs after filling in correct input, try submitting the same input after waiting a few seconds. The Google APIs might have briefly timed out.

![Homepage](https://github.com/minprog-platforms/project-julialfk/blob/main/doc/Home.PNG)

In the navigation bar, the user can also find the "Sign Up" and the "Login" page if they are not logged in yet. On these pages, the user can create an account by filling in their email adress, first name and a password, and login to their account respectively. After signing in, the user can find the "Saved" and "Logout" page in the navigation bar. On the "Saved" page, the user can find a list links to Google Maps pages they have visited before while logged in and remove restaurants that they are not interested in from the list. 

![Saved page](https://github.com/minprog-platforms/project-julialfk/blob/main/doc/Saved.PNG)

## Acknowledgements

For this program, I followed a guide on Flask by Tim Ruscica (Tech With Tim). As such, most of my files are modeled after his example. The code written in his tutorial can be found in [this repository](https://github.com/techwithtim/Flask-Web-App-Tutorial).