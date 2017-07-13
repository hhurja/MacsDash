def db_object(params, client):
	db = client.hackathon
	if params[0] == 'users':
		coll = db.users
		print type(int(params[1]))
		return coll.find_one({"employee_id": int(params[1])})