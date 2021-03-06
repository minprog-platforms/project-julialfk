# project-julialfk

## Problem statement

When you make plans to go out to eat with someone, you might have had the problem that none of you have any inspiration of where to go. Maybe nobody is prefering any type of food in particular or you want to try something new.

## Solution sketch

This application will ask you for the minimum rating of the restaurant and location. 
![MVP Frontpage](https://github.com/minprog-platforms/project-julialfk/blob/main/doc/MVP%20Frontpage.png)

Then it will open up a new window with the google maps location of a random restaurant that meets these conditions.
![Redirect Output](https://github.com/minprog-platforms/project-julialfk/blob/main/doc/Redirect%20Output.PNG)

## Prerequisites

### Data sources

The data I will be using will be from Google. Google Maps data in particular will be used. For this I will be using Google's Places API.

### External components

- Flask: For the implementation of the site, I will be using Flask. 
- Places API: For the data collection I will be using Google's Places API.
- Geocoding API: I will need Google's Geocoding API to convert the prompted location to coordinates.
- Maps Javascript API: If I have enough time, I might make use of Google's Maps Javascript API to implement a map on the site, so it does not have to redirect to a Google Maps search. 
- W3C Geolocation: If have even more time left, I might even be able to ask the user to share their current location using W3C Geolocation, but I doubt that I will come that far.

### Similar apps

Many review sites provide a lookup function based on different categories, which outputs a long list of relevant restaurants. A problem with this is that oftentimes, the indecision stems from the great amount of choice in restaurants. By only showing one result, this app tries to combat the paradox of choice.

There are also web apps, of which [Random Restaurant Generator](https://budgetbranders.com/restaurant-generator/) is the most similar. This app however, uses Yelp as their data source. The app I am creating will be using Google, so this app will primarily focus on those that prefer to use Google over other reviewing sites.

### Hardest parts

I need to figure out how to use Google's API for this app. I think the hardest part would be connecting the prompted input on the webpage to the python script to make the API requests.