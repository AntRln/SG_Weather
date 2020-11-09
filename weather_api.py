# Python program to consume public weather API
# and store the fetched data in a database.

import requests, json, os, sqlite3, time

# Creating a temp folder where the database will
# be stored.

con = sqlite3.connect('weather.db')

cur = con.cursor()

weather_sql = """
CREATE TABLE weather_reports (
	id integer PRIMARY KEY,
	city_name text NOT NULL,
	temperature decimal NOT NULL,
	pressure bigint NOT NULL,
	humidity int,
	description text NOT NULL
)"""

cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='weather_reports' ''')
if cur.fetchone()[0]==0 : {
	cur.execute(weather_sql)
}


api_key = "b12c48f3c7ae33832cfb143d5654be7e"
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key

url = base_url + "&q=" + "Montreal"

#result_json = requests.get(url).json()

def parse_data(x):

	result = {}

	if x["cod"] != "404": 
		y = x["main"] 
		current_temperature = y["temp"] 
		current_pressure = y["pressure"] 
		current_humidity = y["humidity"] 
		z = x["weather"] 
		weather_description = z[0]["description"]
		city_name = x["name"]

		result = {
			"city_name" : city_name,
			"temperature" : current_temperature,
			"pressure" : current_pressure,
			"humidity" : current_humidity,
			"description" : weather_description
		}

	else: 
		print(" City Not Found ")
	
	return result


#result = parse_data(result_json)

def add_data(row_id, res, cur, con):
	cur.execute("Insert into weather_reports values (?,?,?,?,?,?)",
				(row_id, res['city_name'], res['temperature'],
				res["pressure"], res["humidity"], res["description"]))
	con.commit()


#add_data(result, cur)


def get_weather(row_id):
	result_json = requests.get(url).json()
	result = parse_data(result_json)
	add_data(row_id, result, cur, con)

cur.execute('SELECT COUNT(id) FROM weather_reports')

count = cur.fetchone()[0]

while True :
	cur.execute('SELECT COUNT(id) FROM weather_reports')
	count = cur.fetchone()[0] + 1
	get_weather(count)
	time.sleep(5)