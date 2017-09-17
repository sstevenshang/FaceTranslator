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
	    var filename = request.body.image.file_name;
	    where = filename.indexOf(".") - 1;
	    theNum = parseInt(filename.charAt(where)) - 1
	    console.log(where);
	    console.log(theNum);
	    filename = filename.substring(0,where) + theNum +  ".jpg"
	    console.log("***********")
	    console.log(filename)
	    console.log("***********")
	//console.log(request.body.image.file_data);
	console.log(filename);
	console.log("--------------");

	
	var options = {
		  args: ["./imagedata.txt", filename]
	};

	PythonShell.run('../decodeImage.py', options, function (err, results) {
	  	 //if (err) throw err;
	  // results is an array consisting of messages collected during execution
	  	console.log(err)
	  	console.log('results: %j', results);

	  	setTimeout(function() {
	  		console.log("aslkjd");
	  	}, 3000);



		var options2 = {
			  args: ['https://raw.githubusercontent.com/sstevenshang/FaceTranslator/master/nodeserver/' + filename]
		};

		PythonShell.run('../test.py', options2, function (err, results) {
		  if (err) throw err;
		  // results is an array consisting of messages collected during execution
		  console.log('results: %j', results);
		  console.log(results[results.length-1])
		  response.send(results[results.length-1] + "|" + results[results.length-2])
		});

	});
	}); 



	



})





app.listen(port, (err) => {  
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})
