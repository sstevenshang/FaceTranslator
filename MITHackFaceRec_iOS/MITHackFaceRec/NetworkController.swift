//
//  NetworkController.swift
//  MITHackFaceRec
//
//  Created by Steven Shang on 9/16/17.
//  Copyright © 2017 Steven Shang. All rights reserved.
//

import UIKit

protocol NetworkControllerProtocol {
    func displayResult(name: String)
}

class NetworkController: NSObject {
    
    static var imageRequestCount: Int = 0
    
    let delegate: NetworkControllerProtocol? = nil
    
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

        startNetworkRequest(urlString: "18.10.4.234", image: image, completionHandler: completionHandler)
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
        
        print(base64String)
        
        currentTask = session.dataTask(with: request) { (data, response, error) in
            
            NetworkController.imageRequestCount += 1
            completionHandler(nil)
            if let delegate = self.delegate, let data = data {
                if let name = NSString(data: data, encoding: String.Encoding.utf8.rawValue) as String? {
                    delegate.displayResult(name: name)
                }
            }
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
