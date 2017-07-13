client = MongoClient('107.170.232.140', 27017)

db.orders.insert(
   [
     { order_id: 11, item: "pencil", qty: 50, type: "no.2" },
     { item: "pen", qty: 20 },
     { item: "eraser", qty: 25 }
   ]
)