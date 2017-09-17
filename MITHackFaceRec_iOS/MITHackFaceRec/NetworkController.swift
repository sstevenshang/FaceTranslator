//
//  NetworkController.swift
//  MITHackFaceRec
//
//  Created by Steven Shang on 9/16/17.
//  Copyright © 2017 Steven Shang. All rights reserved.
//

import UIKit
import Alamofire

protocol NetworkControllerProtocol {
    func displayResult(name: String, link: String)
}

class NetworkController: NSObject {
    
    static var imageRequestCount: Int = 0
    
    var delegate: NetworkControllerProtocol? = nil
    
    static public func createAlertViewController(title: String, message: String) -> UIAlertController {
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        let action = UIAlertAction(title: "Okay", style: .cancel, handler: nil)
        alert.addAction(action)
        return alert
    }
    
    enum networkErrors {
        case urlFailure
        case compressionFailure
        case serializationFailure
    }
    
    private var currentTask: URLSessionDataTask?
    
    func sendImage(image: UIImage, completionHandler: @escaping ((_ error: networkErrors?)->())) {
        
        //startNetworkRequestAlamofire(urlString: "http://eb987564.ngrok.io", image: image, completionHandler: completionHandler)
        startNetworkRequest(urlString: "http://eb987564.ngrok.io", image: image, completionHandler: completionHandler)
        
    }
    
    private func startNetworkRequestAlamofire(urlString: String, image: UIImage, completionHandler: @escaping ((_ error: networkErrors?)->())) {
        //depricated

        if let imageData = UIImageJPEGRepresentation(image, 0.9) {
            Alamofire.upload(imageData, to: urlString).response(completionHandler: { (response) in
                
                guard let data = response.data else {
                    print("Received no data back")
                    return
                }
                
                if let responseString = NSString(data: data, encoding: String.Encoding.utf8.rawValue) as String? {
                    
                    print(responseString)
                    
                    let responseArray = responseString.components(separatedBy: ":")
                    let name = responseArray[0]
                    let link = responseArray[1]
                    
                    self.delegate?.displayResult(name: name, link: link)
                }
            })
        } else {
            print("Failed to get JPEG")
            return
        }
    }
    
    func stopSending() {
        //depricated
    }
    
    private func startNetworkRequest(urlString: String, image: UIImage, completionHandler: @escaping ((_ error: networkErrors?)->())) {
        
        guard let url = URL(string: urlString) else {
            print("Failed to get url")
            completionHandler(.urlFailure)
            return
        }
        
        var request = URLRequest(url: url)
        
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        
        guard let imageData = UIImageJPEGRepresentation(image, 0.9) else {
            print("Fialed to compress jpeg")
            completionHandler(.compressionFailure)
            return
        }
        let base64String = imageData.base64EncodedString(options: Data.Base64EncodingOptions.init(rawValue: 0))
        let filename = "face\(NetworkController.imageRequestCount).jpg"
        let params = ["image":[ "content_type": "image/jpeg", "filename":"\(filename)", "file_data": base64String]]
        
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: params, options: JSONSerialization.WritingOptions.init(rawValue: 0))
        } catch {
            completionHandler(.serializationFailure)
            print("Failed to serialize data.")
            return
        }
        
        let session = URLSession.shared
        
        // print(base64String)
        
        currentTask = session.dataTask(with: request) { (data, response, error) in
            
            print(error?.localizedDescription ?? "no error in response")
            
            NetworkController.imageRequestCount += 1
            
            guard let delegate = self.delegate else {
                print("no delegate found for network manager")
                return
            }
            
            guard let data = data else {
                print("no data found in response")
                return
            }
            
            guard let responseString = NSString(data: data, encoding: String.Encoding.utf8.rawValue) else {
                print("no string gotten from data")
                return
            }
            
            print(responseString)
            
            let responseArray = responseString.components(separatedBy: "|")
            let name = responseArray[0]
            let link = responseArray[1]
            
            self.delegate?.displayResult(name: name, link: link)
        }
        
        if let currentTask = currentTask {
            currentTask.resume()
        }
    }
    
    func stopNetworkRequest() {
        
        if let currentTask = currentTask {
            currentTask.cancel()
        }
    }
    
    static public func writeStringToFile(text: String) {
        
        let file = "test.txt"
        
        if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            
            let path = dir.appendingPathComponent(file)
            do {
                try text.write(to: path, atomically: false, encoding: String.Encoding.utf8)
            }
            catch {
                print("Failed to write")
            }
        }
    }
}
