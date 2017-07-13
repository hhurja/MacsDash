from flask import json

def fake_user(user_id):
	if user_id == '1':
		output = {
			'employee_id': 1,
			'full_name': 'Steve Jobs',
			'building': 'IL0',
			'office': 1
		}
	elif user_id == '2':
		output = {
			'employee_id': 2,
			'full_name': 'Steve Wozniak',
			'building': 'IL0',
			'office': 2
		}
	elif user_id == '3':
		output = {
			'employee_id': 3,
			'full_name': 'Tim Cook',
			'building': 'IL0',
			'office': 3
		}
	elif user_id == '4':
		output = {
			'employee_id': 4,
			'full_name': 'Eddy Cue',
			'building': 'IL0',
			'office': 4
		}
	elif user_id == '5':
		output = {
			'employee_id': 5,
			'full_name': 'Mary Demby',
			'building': 'Mary 3',
			'office': 142
		}
	return json.dumps(output)

def fake_order(order_id):
	if order_id == '1':
		output = {
			'food_item': 'pizza',
			'time': '11:30',
			'user': 'Steve Jobs',
			'deliverer': '',
			'completed': False,
			'building': 'IL0'
		}
	elif order_id == '2':
		output = {
			'food_item': ['pizza', 'cookie'],
			'time': '11:15',
			'user': 'Steve Wozniak',
			'deliverer': 'Steve Jobs',
			'completed': False,
			'building': 'IL0'
		}
	elif order_id == '3':
		output = {
			'food_item': 'hamburger',
			'time': '11:00',
			'user': 'Tim Cook',
			'deliverer': 'Mary Demby',
			'completed': False,
			'building': 'IL0'
		}
	elif order_id == '4':
		output = {
			'food_item': ['hamburger', 'salad', 'cookie'],
			'time': '12:30',
			'user': 'Steve Wozniak',
			'deliverer': 'Mary Demby',
			'completed': False,
			'building': 'IL0'
		}
	elif order_id == '5':
		output = {
			'food_item': 'hamburger',
			'time': '13:30',
			'user': 'Steve Jobs',
			'deliverer': 'Tim Cook',
			'completed': False,
			'building': 'IL0'
		}
	return json.dumps(output)
