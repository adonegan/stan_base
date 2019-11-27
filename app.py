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


@app.route('/insert_film', methods=['POST'])     
def insert_film():
    films = mongo.db.films
    films.insert_one(request.form.to_dict())
    return redirect(url_for('get_films'))

@app.route('/edit_film/<film_id>')
def edit_film(film_id):
    the_film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    all_genres = mongo.db.genres.find()
    return render_template('editfilm.html', film=the_film, genres=all_genres)    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
    port=os.environ.get('PORT', '5000'),
    debug=True)