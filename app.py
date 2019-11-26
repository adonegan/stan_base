import os 
from os import path
if path.exists("env.py"):
    import env #to import environment variables
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'stan_base'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'Env value not loaded')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_films')
def get_films():
    return render_template("films.html", 
    films=mongo.db.films.find())

@app.route('/add_film')
def add_film():
    return render_template('addfilm.html',
    genres=mongo.db.genres.find())    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
    port=os.environ.get('PORT', '5000'),
    debug=True)