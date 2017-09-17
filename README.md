# Face2Book

## Technologies Used

## How to Run

1. First, you need to set up the Face Group on MSFT Cognitive Services

	Change the `Ocp-Apim-Subscription-Key` in

```

	headers = {
	    # Request headers.
	    'Content-Type': 'application/json',

	    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
	    'Ocp-Apim-Subscription-Key': '37e02440a4dd4ef2b738acf9e5dd46ac',
	}	

	
```

in `setupPersonGroup.py` to your Face API Key.
	
 you may want to change the photo files found in the array `peopleInfo` to photos of you choosing in the same format as we have

 Then run `python setupPersonGroup.py`


2. Now you need to train the group

	run `python -c import setupPersonGroup as p; p.train()` and to check when it is done run `python -c import setupPersonGroup as p; p.getStatus()`


=======
## Inspiration
Adding people on Facebook can be so cumbersome because you have to ask for their username or look them up. We wanted to invent a new way to add people on Facebook that is efficient and fun. So we came up with Face2Book!

## What it does
With the Face2Book app, one can use it to snap a selfie of their new friend, and it will automatically pull up their Facebook profile!

## How we built it
In the back-end, we used Python to scrape information on users on Facebook (their name and profile picture using their user id) to obtain data. We then send that data to a Microsoft Azure server that has a Face API for it to train. Then it decides if the picture matches up with your friend, and if it does, it pulls up their Facebook profile!

## Challenges we ran into
Getting the data set from Facebook
Graph API only gets friends who use the Graph API

## What we learned
Facebook scraping
Facebook Graph API
Microsoft Azure

## What's next for FaceTranslator
Add more data!

