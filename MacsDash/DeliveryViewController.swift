//
//  DeliveryViewController.swift
//  MacsDash
//
//  Created by Sarah Reyes-Franco on 7/13/17.
//  Copyright © 2017 Apple. All rights reserved.
//

import UIKit

class DeliveryViewController: UIViewController {

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
    
    @IBAction func goBackToOneButtonTapped(_ sender: Any) {
        performSegue(withIdentifier: "unwindSegueToVC1", sender: self)
    }
    
    
    @IBOutlet weak var segmentedControl: UISegmentedControl!
    @IBOutlet weak var orderView: UIView!
    @IBOutlet weak var pickupView: UIView!
    
    @IBAction func indexChanged(_ sender: UISegmentedControl) {
        switch segmentedControl.selectedSegmentIndex
        {
        case 0:
            orderView.isHidden = false
            pickupView.isHidden = true
        case 1:
            orderView.isHidden = true
            pickupView.isHidden = false
        default:
            break;
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        orderView.isHidden = false
        pickupView.isHidden = true
        // Do any additional setup after loading the view.
    }


}
