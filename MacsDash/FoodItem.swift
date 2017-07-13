//
//  FoodItem.swift
//  MacsDash
//
//  Created by Sarah Reyes-Franco on 7/13/17.
//  Copyright © 2017 Apple. All rights reserved.
//

import Foundation

class FoodItem {
    var foodId: String
    //Category (aka beverage, pasta, etc.)
    var type: String!
    //Name of the food
    var name: String
    //Calory count
    var calories: Int
    //Price
    var price:Float
    
    init(foodId: String, type: String, name: String, calories: Int, price: Float){
        self.foodId = foodId
        self.type = type
        self.name = name
        self.calories = calories
        self.price = price
    }
    
}
