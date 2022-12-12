from . import bp as app
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.blog.models import Pokemon
from flask_login import current_user, login_required

@app.route('/posts')
@login_required
def posts():
    all_posts = Pokemon.query.all()
    return render_template('pokemon.html', posts=all_posts)

#create a route that allows us to get a single post based on its id 

@app.route('/post/<id>')
@login_required
def post_by_id(id):
    post = Pokemon.query.get(int(id))
    return render_template('pokemon_single.html', post=post)

@app.route('/create_post', methods=["POST"])
@login_required
def create_post():
    name = request.form['inputName']
    description = request.form['inputDescription']
    type = request.form['inputType']
    new_post = Pokemon(name = name, description = description, type = type, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash('Pokemon post created successfully', 'success')
    return redirect(url_for('blog.posts')) 

@app.route('/create_pokemon', methods=["GET", "POST"])
@login_required
def create_pokemon():
    item = input('pokemon?: ')
    select_pokemon = request.get(f'https://pokeapi.co/api/v2/pokemon/{item}')
    data = select_pokemon.json()
    item = {
    'name': data['name'],
    'weight': data['weight'],
    'types': data['types']
}
    data['sprites']['front_default']
    
    new_post = Pokemon(name = select_pokemon, data = data, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash('Pokemon post created successfully', 'success')
    return redirect(url_for('blog.posts')) 
