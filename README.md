# TODO-list
A simple webapp that creates a TODO-list for a user to add and remove tasks as they wish to it. Python is used to build the backend,
While HTML, Jinja and CSS was used to build the frontend. Flask is used to connect the backend to the frontend. SQL is used to create
a database that the app stores data on each TODO-list task as well as retrieve and modify. 

## Features
Features of the webapp include
* Adding and removing tasks to the list
* Change the status of a task in the list from incomplete to finished and vice versa
* For any task added on the list the user can update the task description
* A counter for the total number of tasks that are completed based on how many tasks have the finished status on the list and the ones that have the finished status after being removed as well

## How to Run
Navigate to the working directory of the project

Install the requirements
```
	$ pip install -r requirements.txt
```
Initialize the Database and export background
```
	$ export FLASK_APP=background
	$ flask init-db
```
This is only required when starting up the app the first time

To begin running 
```
	$ waitress-serve --call 'background:create_app'
```
On your browser insert 'http://localhost:8080/'

## Run the pytests
Install the directory 

Move to your project directory 
```
	$ pip install -e .
```
Run the test cases
```
	$ pytest
``` 
