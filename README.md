# full-throttle-labs-api

## steps to run the project
* Go to the roo directory
* python manage.py makemigrations core
* python manage.py migrate
* python manage.py runserver

## server runs at `localhost:8000` in local

## type of api
* **/retrieve all** - retrieves all the users and their activity period
* **/<id>** - retries information of specific user using id
  
## populate data
* go to root directory
* python manage.py populate_py ./testfile/test_data.json
