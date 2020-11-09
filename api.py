import sqlite3, flask

from flask import Flask, request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/search', methods=['POST', 'GET'])
def search():
    
    idToSearch = request.form.get('idToSearch')

    idToSearch = (idToSearch,)

    con = sqlite3.connect("weather.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * from weather_reports WHERE id=?', idToSearch)

    print("idToSearch = ", idToSearch)

    rows = cur.fetchall()

    print(rows)

    return render_template("search.html", rows = rows)



@app.route('/list')
def list():

    con = sqlite3.connect("weather.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT * from weather_reports')

    rows = cur.fetchall()
    return render_template("list.html",rows = rows)


@app.route('/')
def home():
   return render_template('home.html')


app.run()