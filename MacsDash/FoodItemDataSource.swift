//
//  FoodItemDataSource.swift
//  MacsDash
//
//  Created by Sarah Reyes-Franco on 7/13/17.
//  Copyright © 2017 Apple. All rights reserved.
//

import Foundation

import Foundation

class FoodItemDataSource{
    var foods:[FoodItem]
    
    init() {
        foods = []
        
        //Get the food items from the API here
        
    }
    
    func getFoodItems() -> [FoodItem] {
        return foods
    }
    
}
