from flask import Flask, request, json
from pymongo import MongoClient
from pprint import pprint
from fake_data_functions import fake_user, fake_order

app = Flask(__name__)

client = MongoClient('107.170.232.140', 27017)

@app.route('/api')
def api_root():
	return 'hello and welcome to the MacsDash API'

@app.route('/api/users')
def api_users():
	user_list = []
	output = {'user_list': user_list}
	return json.dumps(output)

@app.route('/api/user/<user_id>', methods=['GET', 'PUT', 'POST'])
def api_user(user_id):
	output = fake_user(user_id)
	# db = client.hackathon
	# coll = db.users
	# return coll.find_one({"employee_id": 1})
	return output

@app.route('/api/orders/')
def api_orders():
	pass

@app.route('/api/order/<order_id>', methods=['GET', 'PUT', 'POST'])
def api_order(order_id):
	output = fake_order(order_id)
	return output
	pass

@app.route('/api/order/<building>')
def api_order_by_building(building):
	pass

@app.route('/api/foods')
def api_foods():
	pass

@app.route('/api/food/<food_id>', methods=['GET', 'PUT', 'POST'])
def api_food(food_id):
	pass


if __name__ == '__main__':
	app.run()






'''
USERS - employee_id, full_name, building, office
ORDERS - ID, food item, time, user, deliverer, completed, building
FOOD ITEMS - ID, name, calories, price, asset path
'''