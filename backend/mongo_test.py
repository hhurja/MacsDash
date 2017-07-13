from pymongo import MongoClient
from pprint import pprint


client = MongoClient('107.170.232.140', 27017)
db = client.hackathon
collection = db.collection
coll_items = db.items
#pprint(collection.find_one({"USERS": {"employee_id": 1}}))
#pprint(collection.find_one({"_id": "5967af71ba3e1ccd8ec74490"}))
# pprint(db.users.find_one({"employee_id": 1.0}))
items = coll_items.find()

# for item in items:
# 	pprint(item)


for o in db.orders.find({"Type": "Beverage"}):
	pprint(o)
