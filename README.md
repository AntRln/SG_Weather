# SG_Weather
Prototype for a weather API.

This project aims to regularly fetch data from a [public weather API](openweathermap.org) and store this data in a database.
An API allows to expose this data from two endpoints : one for every data in the database, the other to fetch data using their ID.

## General information

This code was developped in Python 3.7.2. The database is handled using SQLite3. The API used to expose the data uses Flask 1.0.2.

## Initializing the database

This project already contains a database **weather.db** with existing values. If you would rather start from scratch, run the **weather_api.py** to fetch weather data every 30 seconds. 

## Accessing the data

The data can be accessed by running the **api.py** file. Flask must be installed with your version of Python.
The API can be found on your web browser at the address http://127.0.0.1:5000/

On the homepage, you will find two links :
* **Full list**, allowing the user to access the complete list of data from the database
* **Search for ID**, allowing the user to look for data using a specific ID value
