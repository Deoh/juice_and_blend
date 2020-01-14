import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = "recipe_book"

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_drink')
def get_drink():
    return render_template("drink.html",
                           drink=mongo.db.drink.find())


@app.route('/add_drink')
def add_drink():
    return render_template('addDrink.html',
                           categories=mongo.db.categories.find(),
                           ingredients=mongo.db.ingredients.find())


@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    drink = mongo.db.drink
    drink.insert_one(request.form.to_dict())
    drink.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('get_drink'))


@app.route('/edit_drink/<drink_id>')
def edit_drink(drink_id):
    the_drink = mongo.db.drink.find_one({"_id": ObjectId(drink_id)})
    return render_template('editDrink.html', drink=the_drink,
                           categories=mongo.db.categories.find(),
                           ingredients=mongo.db.ingredients.find())


@app.route('/update_drink/<drink_id>', methods=["POST"])
def update_drink(drink_id):
    drink = mongo.db.drink
    drink.update({'_id': ObjectId(drink_id)},
    {
        'drink_name': request.form.get('drink_name'),
        'category_name': request.form.get('category_name'),
        'ingredient_name': request.form.get('ingredient_name'),
        'instruction': request.form.get('instruction'),
        'general_fitness': request.form.get('general_fitness'),
        'aerobic_exercise': request.form.get('aerobic_exercise'),
        'muscular_strength': request.form.get('muscular_strength'),
        'high_energy_sport': request.form.get('high_energy_sport'),
        'low_energy_sport': request.form.get('low_energy_sport'),
        'endurance_activities': request.form.get('endurance_activities')
    })
    return redirect(url_for('get_drink'))


@app.route('/remove_drink/<drink_id>')
def remove_drink(drink_id):
    mongo.db.drink.remove({'_id': ObjectId(drink_id)})
    return redirect(url_for('get_drink'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
