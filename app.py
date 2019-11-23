import os 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import env
MONGO_URI = os.getenv('MONGO_URI', "Env value not loaded")

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_films')
def get_films():
    return render_template("films.html", films=monggo.db.film.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
    port=os.environ.get('PORT', '5000'),
    debug=True)