from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)

app.config.from_pyfile('prod.py')

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Users Class/Model
class Base(db.Model):

  __abstract__  = True
  __bind_key__ = 'test_api'


class Users(Base):
  
  __tablename__  = 'users'
  __table_args__ = {'extend_existing': True}
  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True)
  email = db.Column(db.String(200))
  salary = db.Column(db.Integer)
  phone = db.Column(db.Integer)

  def __init__(self, username, email, salary, phone):
    self.username = username
    self.email = email
    self.salary = salary
    self.phone = phone

# Users Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('username', 'email', 'salary', 'phone')

# Init schema
#user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a Users
@app.route('/user', methods=['POST'])
def add_user():
  username = request.json['username']
  email = request.json['email']
  salary = request.json['salary']
  phone = request.json['phone']

  new_user = Users(username, email, salary, phone)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

# Get All Userss
@app.route('/user', methods=['GET'])
def get_users():
  all_users = Users.query
  result = users_schema.dump(all_users)
  data = {"users":result}
  return data

# Get Single Userss
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
  user = Users.query.get(id)
  return users_schema.jsonify(user)

# Update a Users
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
  user = Users.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  user.name = name
  user.description = description
  user.price = price
  user.qty = qty

  db.session.commit()

  return user_schema.jsonify(user)

# Delete Users
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
  user = Users.query.get(id)
  db.session.delete(user)
  db.session.commit()

  return user_schema.jsonify(user)

# # Run Server
# if __name__ == '__main__':
#   app.run(debug=True)
