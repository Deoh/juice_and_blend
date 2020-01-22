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

#------------------------Drinks----------------------

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
    #come back to this
    #ingredients = mongo.db.ingredients
    #drink.insert(request.form.to_dict())
    #drink.insert_one(request.form.to_dict(flat=False))

    drink.insert_one({
        'drink_name': request.form.to_dict()['drink_name'],
        'category_name': request.form.to_dict()['category_name'],
        'ingredient_name': request.form.to_dict(flat=False)['ingredient_name'],
        'instruction': request.form.to_dict()['instruction'],
        'general_fitness': request.form.to_dict()['general_fitness'],
        'aerobic_exercise': request.form.to_dict()['aerobic_exercise'],
        'muscular_strength': request.form.to_dict()['muscular_strength'],
        'high_energy_sport': request.form.to_dict()['high_energy_sport'],
        'low_energy_sport': request.form.to_dict()['low_energy_sport'],
        'endurance_activities': request.form.to_dict()['endurance_activities']
    })
    #come back to this
    ingredients.insert({
        'ingredient_name': request.form.to_dict()['ingredient_name'][-1],
    })

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

#------------------------Ingredients----------------------

@app.route('/get_ingredients')
def get_ingredients():
    return render_template('ingredients.html',
                           ingredients=mongo.db.ingredients.find())


@app.route('/edit_ingredient/<ingredient_id>')
def edit_ingredient(ingredient_id):
    the_ingredient = mongo.db.ingredients.find_one({"_id": ObjectId(ingredient_id)})
    return render_template('editIngredient.html', ingredient=the_ingredient)


@app.route('/update_ingredient/<ingredient_id>', methods=["POST"])
def update_ingredient(ingredient_id):
    mongo.db.ingredients.update(
        {'_id': ObjectId(ingredient_id)},
        {'ingredient_name': request.form.get('ingredient_name')})
    return redirect(url_for('get_ingredients'))


@app.route('/delete_ingredient/<ingredient_id>')
def delete_ingredient(ingredient_id):
    mongo.db.ingredients.remove({'_id': ObjectId(ingredient_id)})
    return redirect(url_for('get_ingredients'))


@app.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    category_doc = {'ingredient_name': request.form.get('ingredient_name')}
    mongo.db.ingredients.insert_one(category_doc)
    return redirect(url_for('get_ingredients'))


@app.route('/add_ingredient')
def add_ingredient():
    return render_template('addIngredient.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
