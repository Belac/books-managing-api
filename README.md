# books-managing-api
API for managing books of a library, created with Flask

## Getting started

### Installing dependencies

#### Python
First of all, you must have at least **Python 3.10.0** on your computer.       
If not, click [download python](https://www.python.org/downloads/) to install the latest version of python for your platform.

#### Pip or another package manager
Secondly, be sure you have a **package manager** installed on your computer.    
For instance pip 22.0.3 from C:\Users\Username\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

#### Virtual environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

#### Pip dependencies
Once you have your virtual environment setup and running, install dependencies by running :
  pip install -r requirements.txt 
  or 
  pip3 install -r requirements.txt

### Database Setup
With Postgres running, restore a database using the books_managing.sql file provided.     
From the backend folder in terminal run:
  psql books_managing < books_managing.sql

### Running the server
Ensure you are working using your created virtual environment.
To run the server on Linux or Mac, execute:
  export FLASK_APP=app.py
  export FLASK_ENV=development
  flask run
To run the server on Windows, execute:
  set FLASK_APP=app.py
  set FLASK_ENV=development
  flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.
Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.

## Api reference
This app can be run locally or hosted as a base URL. 
The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format: { "success": False, "error": 404, "message": "Not found" }       
The API will return xxxx error types when requests fail: 
- 400: Bad request 
- 500: Internal server error 
- 422: Unprocessable 
- 404: Not found

## Endpoints
