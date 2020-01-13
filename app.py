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
                           categories=mongo.db.categories.find())


@app.route('/insert_drink', methods=['POST'])
def insert_drink():
    drink = mongo.db.drink
    drink.insert_one(request.form.to_dict())
    return redirect(url_for('get_drink'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
