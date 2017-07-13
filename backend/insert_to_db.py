client = MongoClient('107.170.232.140', 27017)

db.items.insert(
   [
     { Type: "Beverage", Name: "Coca cola", cal: 150, price: 1, image: "images/Coca cola"},
     { Type: "Beverage", Name: "Honest Tea, Just Black", price: 2, image: "images/Honest Tea, Just Black"},
     { Type: "Beverage", Name: "Kevita Kombucha, Citrus", cal: 35, price: 3, image: "images/Kevita Kombucha, Citrus"},
     { Type: "Beverage", Name: "Kevita Kombucha, Ginger",cal: 70,  price: 3, image: "images/Kevita Kombucha, Ginger"},
     { Type: "Beverage", Name: "Kevita, Lemon Cayenne",cal: 10, price: 3, image: "images/Kevita, Lemon Cayenne"},
     { Type: "Pasta", Name: "Pasta with Bolognese", price: 7, image: "images/Pasta with Bolognese"},
     { Type: "Pasta", Name: "Pasta with Pesto", price: 7, image: "images/Pasta with Pesto"},
     { Type: "Soup", Name: "Potato leek soup", price: 4, image: "images/Potato leek soup"},
     { Type: "Sushi", Name: "Caffe roll", cal: 520, price: 9, image: "images/Caffe roll"},
     { Type: "Sushi", Name: "Soba sushi roll", cal: 900, price: 5, image: "images/Soba sushi roll"},
     { Type: "Burrito", Name: "Burrito Vegetable", price: 6, image: "images/Burrito Vegetable"},
     { Type: "Burrito", Name: "Burrito Bison", price: 6, image: "images/Burrito Bison"},
     { Type: "Salad", Name: "Chef Salad", cal: 820, price: 7, image: "images/Chef Salad"}
   ]
)


db.orders.insert(
   [
     { Type: "Beverage", Name: "Coca cola", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Beverage", Name: "Honest Tea, Just Black", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Beverage", Name: "Kevita Kombucha, Citrus", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Beverage", Name: "Kevita Kombucha, Ginger",  Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Beverage", Name: "Kevita, Lemon Cayenne", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Pasta", Name: "Pasta with Bolognese", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Pasta", Name: "Pasta with Pesto", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Soup", Name: "Potato leek soup", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Sushi", Name: "Caffe roll", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Sushi", Name: "Soba sushi roll", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Burrito", Name: "Burrito Vegetable", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Burrito", Name: "Burrito Bison", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False },
     { Type: "Salad", Name: "Chef Salad", Time: "00:00", User: "Steve Jobs", Deliverer: "Tim Cook", Completed: False }
   ]
)