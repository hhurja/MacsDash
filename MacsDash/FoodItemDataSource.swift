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
        let urlString = URL(string: "http://127.0.0.1:5000/api/foods")
        if let url = urlString {
            let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
                if error != nil {
                    print(error)
                } else {
                    if let usableData = data {
                        let json = try? JSONSerialization.jsonObject(with: usableData, options: [])
                        print(json)
                    }
                }
            }
            task.resume()
        }
    }
    
    func getFoodItems() -> [FoodItem] {
        return foods
    }
    
}
