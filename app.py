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

# ------------------------Drinks List Page----------------------
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", categories=mongo.db.categories.find())


@app.route('/get_drink')
def get_drink():
    return render_template("drink.html",
                           drink=mongo.db.drink.find(),
                           categories=mongo.db.categories.find())


# ------------------------Add Drink Page----------------------
@app.route('/add_drink')
def add_drink():
    return render_template('addDrink.html',
                           categories=mongo.db.categories.find(),
                           ingredients=mongo.db.ingredients.find())


@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    mongo.db.drink.insert_one({
        'category_name': request.form.to_dict()['category_name'],
        'drink_name': request.form.to_dict()['drink_name'],
        'ingredient_name': request.form.to_dict(flat=False)['ingredient_name'],
        'instruction': request.form.to_dict()['instruction'],

    })
    return redirect(url_for('get_drink'))

# ------------------------Edit Drink Page----------------------
@app.route('/edit_drink/<drink_id>')
def edit_drink(drink_id):
    the_drink = mongo.db.drink.find_one({"_id": ObjectId(drink_id)})
    return render_template('editDrink.html', drink=the_drink,
                           categories=mongo.db.categories.find(),
                           ingredients=mongo.db.ingredients.find())


@app.route('/update_drink/<drink_id>', methods=["POST"])
def update_drink(drink_id):
    mongo.db.drink.update({'_id': ObjectId(drink_id)},
                          {
        'category_name': request.form.get('category_name'),
        'drink_name': request.form.get('drink_name'),
        'ingredient_name': request.form.to_dict(flat=False)['ingredient_name'],
        'instruction': request.form.get('instruction')
    })
    return redirect(url_for('get_drink'))

# ------------------------Delete Drink----------------------
@app.route('/remove_drink/<drink_id>')
def remove_drink(drink_id):
    mongo.db.drink.remove({'_id': ObjectId(drink_id)})
    return redirect(url_for('get_drink'))

# ------------------------Ingredients List Page----------------------
@app.route('/get_ingredients')
def get_ingredients():
    return render_template('ingredients.html',
                           ingredients=mongo.db.ingredients.find())

# ------------------------Edit Ingredient Page----------------------
@app.route('/edit_ingredient/<ingredient_id>')
def edit_ingredient(ingredient_id):
    the_ingredient = mongo.db.ingredients.find_one(
        {"_id": ObjectId(ingredient_id)})
    return render_template('editIngredient.html', ingredient=the_ingredient)


@app.route('/update_ingredient/<ingredient_id>', methods=["POST"])
def update_ingredient(ingredient_id):
    mongo.db.ingredients.update(
        {'_id': ObjectId(ingredient_id)},
        {'ingredient_name': request.form.get('ingredient_name')})
    return redirect(url_for('get_ingredients'))

# ------------------------Delete Ingredient----------------------
@app.route('/delete_ingredient/<ingredient_id>')
def delete_ingredient(ingredient_id):
    mongo.db.ingredients.remove({'_id': ObjectId(ingredient_id)})
    return redirect(url_for('get_ingredients'))

# ------------------------Add Ingredient Page----------------------
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
