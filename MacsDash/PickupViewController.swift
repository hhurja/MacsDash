//
//  PickupViewController.swift
//  MacsDash
//
//  Created by Sarah Reyes-Franco on 7/13/17.
//  Copyright © 2017 Apple. All rights reserved.
//

import UIKit

class PickupViewController: UIViewController {

    @IBAction func getData(_ sender: Any) {
        let dataSource = FoodItemDataSource()
        print(dataSource.getFoodItems())
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
