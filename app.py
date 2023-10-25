from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

# Start virtual env - planetary-api\scripts\activate
# flask --app app.py --debug run

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# C:\Users\Shiori.Chiku\OneDrive - InEight\Documents\GitHub\BuildingRESTfulAPIswithFlask (Getting the same path as the app.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
# Built in Flask configuration management system


db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Helo World'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API. Boo yah woo yah')


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404
# Explicit code - 404 (200 is default)


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))

    if age < 18:
        return jsonify(message=f'Sorry, {name}. You are not old enough.'), 404
    else:
        return jsonify(message=f'Welcome, {name}. You are old enough')
    

# Variable rule matching - clearner URL
# http://localhost:5000/url_variables/Shiori/17 - {"message": "Sorry, Shiori. You are not old enough."}
# http://localhost:5000/url_variables/Shiori/19 - { "message": "Welcome, Shiori. You are old enough"}
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age:int):

    if age < 18:
        return jsonify(message=f'Sorry, {name}. You are not old enough.'), 404
    else:
        return jsonify(message=f'Welcome, {name}. You are old enough')


# database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_Key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_Key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)
    


if __name__ == '__main__':
    app.run()


