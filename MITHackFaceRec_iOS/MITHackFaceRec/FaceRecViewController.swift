//
//  FaceRecViewController.swift
//  MITHackFaceRec
//
//  Created by Steven Shang on 9/16/17.
//  Copyright © 2017 Steven Shang. All rights reserved.
//

import UIKit

class FaceRecViewController: UIViewController {

    @IBOutlet weak var faceImage: UIImageView!
    
    @IBOutlet weak var loadingIndicator: UIActivityIndicatorView!
    
    @IBOutlet weak var restartButton: UIButton!
    
    var imageToRecognize: UIImage!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    private func setupUI() {
        DispatchQueue.main.async {
            self.faceImage.contentMode = .scaleAspectFit
            self.faceImage.image = self.imageToRecognize
            self.loadingIndicator.startAnimating()
        }
    }
    
    @IBAction func restartButtonPressed(_ sender: Any) {
        self.dismiss(animated: true) {
            
        }
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
