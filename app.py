import os 
from os import path
if path.exists("env.py"):
    import env #to import environment variables
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config['MONGO_DBNAME'] = 'stan_base'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'Env value not loaded')


mongo = PyMongo(app)


"""The first page users see when visiting the app."""


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")   



"""Users click on button and are taken to login page by default."""


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username' : request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), 
                            login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('welcome'))
            flash("Uh oh! Bad username/password combination. Try again!")
        flash("Uh oh! Bad username/password combination. Try again!")
    return render_template('login.html')



"""If user exists and password is correct, user taken to welcome page."""

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))


"""New users click the signup button, are directed to register page."""


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username' : request.form['username'],
                                'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
        flash("Oh no! Think of another username!")    
    return render_template('signup.html')


"""Users click on logout nav item to close session. 
Visitors are redirected to the homepage."""


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('home'))


"""Functions and routes to direct users to films page to see database entries, to add, edit, update and delete films from app and database"""
  
@app.route('/get_films')
def get_films():
    if 'username' in session:
        username = session['username']
        return render_template("films.html", films=mongo.db.films.find(), username=username)
    else:
        return render_template('login.html')
        

@app.route('/add_film')
def add_film():
    if 'username' in session:
        username = session['username']
        return render_template('addfilm.html', genres=mongo.db.genres.find(), username=username)
    else:
        return render_template('login.html')


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
        'winona_stan': request.form.get('winona_stan')
    })
    return redirect(url_for('get_films'))

@app.route('/delete_film/<film_id>')
def delete_film(film_id):
    mongo.db.films.delete_one({'_id': ObjectId(film_id)})
    return redirect(url_for('get_films'))

@app.route('/get_genres')
def get_genres():
    if 'username' in session:
        username = session['username']
        return render_template('genres.html', genres=mongo.db.genres.find(), username=username)   
    else:
        return render_template('login.html')
    


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
  

"""Route to about page"""

@app.route('/about')
def about():
    return render_template("about.html")  


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
    port=os.environ.get('PORT', '5000'),
    debug=True)