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
@app.route('/home')
def home():
    return render_template("home.html")      


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


@app.route('/update_film/<film_id>', methods=["POST"])
def update_film(film_id):
    films = mongo.db.films
    films.update({'_id': ObjectId(film_id)},
    {
        'film_name':request.form.get('film_name'),
        'film_year':request.form.get('film_year'),
        'co_stars':request.form.get('co_stars'),
        'genre_type':request.form.get('genre_type'),
        'film_plot': request.form.get('film_plot'),
        'film_rec': request.form.get('film_rec'),
        'date_watched': request.form.get('date_watched'),
    })
    return redirect(url_for('get_films'))


@app.route('/delete_film/<film_id>')
def delete_film(film_id):
    mongo.db.films.delete_one({'_id': ObjectId(film_id)})
    return redirect(url_for('get_films'))


@app.route('/get_genres')
def get_genres():
    return render_template('genres.html', genres=mongo.db.genres.find())   


@app.route('/edit_genre/<genre_id>')
def edit_genre(genre_id):
    return render_template('editgenre.html',genre=mongo.db.genres.find_one({'_id': ObjectId(genre_id)})) 


@app.route('/update_genre/<genre_id>', methods=["POST"])
def update_genre(genre_id):
    mongo.db.genres.update(
        {'_id': ObjectId(genre_id)},
        {'genre_type':request.form.get('genre_type')})
    return redirect(url_for('get_genres')) 


@app.route('/delete_genre/<genre_id>')
def delete_genre(genre_id):
    mongo.db.genres.delete_one({'_id': ObjectId(genre_id)})
    return redirect(url_for('get_genres'))     


@app.route('/insert_genre', methods=['POST'])     
def insert_genre():
    genres = mongo.db.genres
    genre_ins = {'genre_type': request.form.get('genre_type')}
    mongo.db.genres.insert_one(genre_ins)
    return redirect(url_for('get_genres'))  


@app.route('/add_genre')
def add_genre():
    return render_template('addgenre.html')    


@app.route('/about')
def about():
    return render_template("about.html")  




if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
    port=os.environ.get('PORT', '5000'),
    debug=True)