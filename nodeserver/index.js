const express = require('express')  
const app = express()  
const port = 8000
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({limit: '50mb'}));

app.use(bodyParser.json({limit: '50mb'}));

var PythonShell = require('python-shell');



// app.get('/pic', (request, response) => {  
//   response.send('/Users/campionfellin/Desktop/hackmit/FaceTranslator/nodeserver/face1.jpg')
// })

app.post('/', (request, response) => {
	console.log("--------------");
	var fuckyeah = request.body.image.file_data;
	var fs = require('fs');
	fs.writeFile("./imagedata.txt", fuckyeah, function(err) {
	    if(err) {
	        return console.log(err);
	    }

	    console.log("The file was saved!");
	}); 



	var filename = request.body.image.filename;
	//console.log(request.body.image.file_data);
	console.log(filename);
	console.log("--------------");

	
	var options = {
		  args: ["./imagedata.txt", filename]
	};

	PythonShell.run('../decodeImage.py', options, function (err, results) {
	  if (err) throw err;
	  // results is an array consisting of messages collected during execution
	  	console.log('results: %j', results);
		var options = {
			  args: ['https://raw.githubusercontent.com/sstevenshang/FaceTranslator/master/nodeserver/' + filename]
		};

		PythonShell.run('../test.py', options, function (err, results) {
		  if (err) throw err;
		  // results is an array consisting of messages collected during execution
		  console.log('results: %j', results);
		});

	});
	response.send("nice");
	





	response.send("nice");

})





app.listen(port, (err) => {  
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})
