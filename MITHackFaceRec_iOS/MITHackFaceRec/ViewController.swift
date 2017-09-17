//
//  ViewController.swift
//  MITHackFaceRec
//
//  Created by Steven Shang on 9/16/17.
//  Copyright © 2017 Steven Shang. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var takePhotoButton: UIButton!
    
    @IBOutlet weak var loadingIndicator: UIActivityIndicatorView!
    
    var imageBuffer: UIImage?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        showLoadingIndicator(show: false)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    fileprivate func showLoadingIndicator(show: Bool) {
        loadingIndicator.isHidden = !show
        takePhotoButton.isHidden = show
        if show {
            self.loadingIndicator.startAnimating()
        } else {
            self.loadingIndicator.stopAnimating()
        }
    }
    
    @IBAction func takePhotoButtonPressed(_ sender: Any) {
        
        let photoAlertController = UIAlertController(title: "Select Image", message: nil, preferredStyle: .alert)
        
        let cameraAction = UIAlertAction(title: "Camera", style: .default) { (handler) in
            
            self.showLoadingIndicator(show: true)
            self.openCamera()
        }
        
        let libraryAction = UIAlertAction(title: "Library", style: .default) { (handler) in
            
            self.showLoadingIndicator(show: true)
            self.openLibrary()
        }
        
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
        
        photoAlertController.addAction(cameraAction)
        photoAlertController.addAction(libraryAction)
        photoAlertController.addAction(cancelAction)
        
        self.present(photoAlertController, animated: true)
    }
    
    func openCamera() {
        if UIImagePickerController.isSourceTypeAvailable(.camera) {
            let imagePicker = UIImagePickerController()
            imagePicker.delegate = self
            imagePicker.sourceType = UIImagePickerControllerSourceType.camera
            // imagePicker.allowsEditing = true
            self.present(imagePicker, animated: true, completion: nil)
        } else {
            self.present(NetworkController.createAlertViewController(title: "No Camera Found", message: "Your device doesn't not have a camera!"), animated: true, completion: nil)
        }
    }
    
    func openLibrary() {
        if UIImagePickerController.isSourceTypeAvailable(.photoLibrary) {
            let libraryPicker = UIImagePickerController()
            libraryPicker.delegate = self
            libraryPicker.sourceType = UIImagePickerControllerSourceType.photoLibrary
            // libraryPicker.allowsEditing = true
            self.present(libraryPicker, animated: true, completion: nil)
        } else {
            self.present(NetworkController.createAlertViewController(title: "No Photo Library Found", message: "Your device doesn't not have a photo library!"), animated: true, completion: nil)
        }
    }
    
    func displayImage(with image: UIImage) {
        self.imageBuffer = image
        self.performSegue(withIdentifier: "showFaceRecViewController", sender: self)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        if (segue.identifier == "showFaceRecViewController") {
            guard let destViewController: FaceRecViewController = segue.destination as? FaceRecViewController else {
                print("Failed to segue")
                return
            }
            if let image = self.imageBuffer {
                destViewController.imageToRecognize = image
            } else {
                print("Failed because of nil imageBuffer")
            }
        }
    }
}

extension ViewController: UIImagePickerControllerDelegate {
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {

        picker.dismiss(animated: true) {
            
            self.showLoadingIndicator(show: false)

            guard let mediaType = info[UIImagePickerControllerMediaType] as? NSString else {
                print("Failed to cast media info")
                return
            }
            
            guard mediaType.isEqual(to: "public.image") else {
                print("Failed to find public image")
                return
            }
            
            guard let imageFile = info[UIImagePickerControllerOriginalImage] as? UIImage else {
                print("Failed to get UIImage")
                return
            }
            
            self.displayImage(with: imageFile)
        }
    }
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true) { 
            self.showLoadingIndicator(show: false)
        }
    }
}

extension ViewController: UINavigationControllerDelegate {
    
}
