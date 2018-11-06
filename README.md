# MyFavShows App <img src="./myfavshows/static/tvshow.png" alt="drawing" width="50" align="center"/>


## Installation
1. Install the Python `virutalenv` package: 

	`pip install virtualenv`


2. Download the projet directory. Once the files unzipped/downloaded, create a python virtual environment in the said directory: 

	`cd /project_directory`
	
	`virtualenv .`


3. From the same directory, install the app:

	`pip install -e myfavshows/`
  
## Running the MyFavShows
   
1. Go to your virtualenv. Add the app to your environment variables:

	Linux / MacOS:`export FLASK_APP=myfavshows`
	
	Windows: `set FLASK_APP=myfavshows`

2. Run the app:

	`flask run`
	
	
## Collaborative school project

MyFavShows App enables any user to search for TV Shows. 
Registered users can add TV Shows to their favourites in order to get more details on the show such as the episodes' description.
They also can enable notifications whenever a new episode of one of their favourites is aired.



## Project specifications

### Authentification
Each user can create an account with an username, a mail address and a password.
Then, the user will be able to log in each time he goes to the website.

### My favorites
Each user can add and remove TV shows from his favorites.
To do it, he has to be connected. Once logged in, he can do these actions by simply clicking on the heart icon. 

#### Object oriented programming
All the results of our API requests are stored in Python objects.
We have created 3 main classes :
	- one Show class
	- one Season class
	- one Episode class
For each class, there is a subclass that inherits it, for example a class ShowDetailedView. The subclass completes our objects with a more precise API request.
All our attributes are in private or protected status according to their use. We have defined our properties for all of them.

### Errors and exceptions
When an error occured, an exception is raised for the developers and the final user is redirected to an error page.
The following errors are handled by our code:
	1. The API is down
	2. The API results have changed : some arguments have been deleted or have changed of typefor example






