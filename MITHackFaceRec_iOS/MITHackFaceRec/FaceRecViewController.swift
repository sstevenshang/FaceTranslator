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
    
    @IBOutlet weak var nameLabel: UILabel!
    
    @IBOutlet weak var openInFacebookButton: UIButton!
    
    var imageToRecognize: UIImage!
    
    var linkToFacebook: String?
    
    let networkManager = NetworkController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        setupUI()
        networkManager.delegate = self
        networkManager.sendImage(image: imageToRecognize) { (error) in
            print(error.debugDescription)
        }
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
            self.nameLabel.text = "Recognizing Your Face"
            self.openInFacebookButton.isEnabled = false
        }
    }
    
    @IBAction func restartButtonPressed(_ sender: Any) {
        self.dismiss(animated: true) {
            self.networkManager.stopNetworkRequest()
        }
    }
    
    @IBAction func openInFacebookButtonPressed(_ sender: Any) {
        if let urlString = linkToFacebook {
            if let url = URL(string: urlString) {
                UIApplication.shared.open(url, options: [:], completionHandler: nil)
            } else {
                print("Couldn't get url!")
            }
        } else {
            print("No URL specified!")
        }
    }
    
    fileprivate func displayName(name: String) {
        
        DispatchQueue.main.async {
            self.loadingIndicator.stopAnimating()
            self.nameLabel.text = "Your Name is \(name)!"
            self.openInFacebookButton.isEnabled = true
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

extension FaceRecViewController: NetworkControllerProtocol {

    func displayResult(name: String, link: String) {
        self.displayName(name: name)
    }
}


