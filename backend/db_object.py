connect_to_db('107.170.232.140', 27017)
	db = client.hackathon
	coll = db.users
	pprint(coll.find_one({"employee_id": 1}))

def db_object(params, client):
	db = client.hackathon
	if params[0] == 'users':
		coll = db.users
		return coll.find_one({"employee_id": 1})