//
//  NetworkController.swift
//  MITHackFaceRec
//
//  Created by Steven Shang on 9/16/17.
//  Copyright © 2017 Steven Shang. All rights reserved.
//

import UIKit

class NetworkController: NSObject {
    
    static public func createAlertViewController(title: String, message: String) -> UIAlertController {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        let action = UIAlertAction(title: "Okay", style: .cancel, handler: nil)
        alert.addAction(action)
        return alert
    }

}
