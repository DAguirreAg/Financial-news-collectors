# Financial-news-collectors

A financial news collector and aggregator service that not only collects the data, but processes and enriches it, while providing a simple UI for basic analytics.

<div>
	<div align="middle">
		<img src="documentation/Main design.png" alt="Main design" width=500>
	</div>
	<div align="middle">
	  <i>Overview of architectural design.</i>
	</div>
</div>

# Introduction
Even most financial news outlets provide API services for data consumption, most of them have very high fees, so this repository tries to create a cheaper alternative while providing some custom analytics.

<div>
	<div align="middle">
		<img src="documentation/Frontend view.png" alt="Frontend view" height=350>
	  	<img src="documentation/Database table content view.png" alt="Database table content view" height=400>
	</div>
	<div align="middle">
	  <i>Overview of frontend and database.</i>
	</div>
</div>

# How to use it
Follow the next steps:

* Prepare the database:
	  * Open your favourite SQL database and create the database and the table using `setup.sql` helper script.
	  * Open the `config.py` file and modify the `SQLALCHEMY_DATABASE_URL` to use the database you just created.

* Prepare the data-backend service:
	* Install the required python packages via `pip install -r requirements.txt`. (It is recommended to use virtual environments when installing them to avoid conflicting version issues).
	* Schedule the data-backend to run every 30mins by opening a `terminal` window and typing `crontab -e`. Then go to the end of the file and type and save the following `*/30 * * * * bash {absolute/path/to/script.sh}`.
	* You can see the scheduled script run by typing `crontab -e`.
<div>
	<div align="middle">
		<img src="documentation/Running the data-backend service.png" alt="Running the data-backend service" width=700>
	</div>
	<div align="middle">
	  <i>Running the data-backend service.</i>
	</div>
</div>

* Prepare the backend service:
	* Install the required python packages via `pip install -r requirements.txt`. (It is recommended to use virtual environments when installing them to avoid conflicting version issues).
	* Open a terminal window and type `uvicorn main:app --reload` to launch the application.
	* (Optional) Open a browser and type `http://127.0.0.1:8000/docs` in the address bar to open an interactive view of the backend service.

<div>
	<div align="middle">
		<img src="documentation/Running the backend service.png" alt="Running the backend service" width=900>
	</div>
	<div align="middle">
	  <i>Running the backend service.</i>
	</div>
</div>

* Prepare the frontend:
	* Run the `index.html` in a live server and open the provided URL. (I recommend using VScode's Live server plug-in due to its ease of use. For non-local deployments you will need to look for more advanced web servers like Apache HTTP server).

<div>
	<div align="middle">
		<img src="documentation/Running the frontend.png" alt="Running the frontend" height=300>
	</div>
	<div align="middle">
	  <i>Running the frontend.</i>
	</div>
</div>

# Technical details

## Back-of-the-envelope calculations

Find below a rough estimation of database requirements.

Assumptions:
* Size per webpage: 0.65Mb
* Webpages downloaded every time: 20 pages
* Number of downloads per day: 48 / day (2 download per hour)
* Number of days to run: 5 * 365 

Database size:
* Required storage: 0.65 (Mb/webpage) * 20 (webpages/download) * 48 (downloads/day) * 5 * 365 (days) = 1,138 Gb

## Technology stack

* Vanilla JS, JQuery and d3.js were selected due to the simple nature of the frontend application.
* FastAPI was selected due to its performance and great community adoption.
* SQL was selected due the robustness of it and the structured nature of the data to be received.
* Selenium was selected due to its power and wide capabilities.

## How it works
The repository is divided into three parts: 

* Data-backend: Contains the code to collect news webpages and extract and enrich headline related data and place it into a database. It can store the downloaded webpages in three ways: Local storage, Google drive and mongoDB. The reason for having multiple options of storage is to facilitate the deployment of this code in simple machines, as well utilize more advance (and costly options).
* Frontend: Contains the code for the UI to facilitate the basic analytics functionality.
* Backend: Contains the code for the frontend to consume the data. It is an intermediary API service to facilitate data fetching.

Note that each service should be ran in their own environment, as they work independently from each other (just communicate over API/Database).
<div>
	<div align="middle">
		<img src="documentation/Main design.png" alt="Main design" width=800>
	</div>
	<div align="middle">
	  <i>Overview of architectural design.</i>
	</div>
</div>

# Future functionalities

* When using the folder/Google drive storage mode, the ETL will load and analyze all the files, **even the ones already analyzed**. This is can easily be avoid by fetching the latest file's date, and avoiding loading it. Another solution may include moving those already processed files to another location. 

* Due to the simplicity of the program, the files will be keep being reanalyzed to be uploaded, even when the files where already analyzed!

* Due to Bloomberg's anti bot features (which blocks any get request to urls), it was decided to open/close a browser everytime a url is visted. This, even if a bit unperformant, circumbents this issue and allows for retrieval of the pages.

## To DO

* Add logging functionality
* Add unit testing to at least the basic extraction functions
* Improve documentation
* Add frontend to do some basic analytics
* Replace SQL insert functionality to do it more efficiently (currently it is being done via pandas)
* Add type hinting to all functions