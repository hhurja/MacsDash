


def db_users_get(user_id, client, all=False):
	db = client.hackathon
	coll = db.users
	if all:
		return coll.find({})
	else:
		db = client.hackathon
		coll = db.users
		# print type(int(params[1]))
		return coll.find_one({"employee_id": int(params[1])})

def db_orders_get(client, filter_params=None):
	db = client.hackathon
	coll = db.orders
	if not filter_params:
		return coll.find({})
	else:
		results = []
		for param in filter_params:
			results.append(coll.find({"Type": param}))
		return results

def db_orders_post(client, params):
	db = client.hackathon
	coll = db.orders
	db.insert_one(
		{ 	Type: params[0], 
			Name: params[1], 
			Time: params[2], 
			User: params[3], 
			Deliverer: params[4], 
			Completed: params[5] 
		}
	)



def db_items_get(params, client, all=False):
	db = client.hackathon
	coll = db.items
	if all:
		return coll.find({})
	else:
		return coll.find({Type: str(params[0]), Name: str(params[1])})

# def db_user(params, client, all=False):
	
# 	db = client.hackathon
# 	coll = db.users
# 	if all:
# 		return coll.find({})
# 	else:
# 		return coll.find_one({'employee_id': int(params['employee_id'])})
