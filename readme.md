## Instructions

### To use API for conversion
Currently, URL: https://ticker-converter.herokuapp.com/api/convert/ 
Accepts POST request, JSON data with the keys:
- `to-convert`: string of identifiers separated by commas
- `convert-type`: string indicating conversion type. Current possible values are 'bb-to-cusip'.
Returns JSON data with key:
- `converted`: string of converted identifiers separated by commas

### Front-end users
Access the application at https://ticker-converter.herokuapp.com/

### To run the app prototype:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ export FLASK_ENV=development
$ export FLASK_APP=proj
$ python3 -m flask run
```
Please run prototype app on localhost port 5000 (see 'To use API for conversion for more info')

### To test the converter functions
```
$ python3 -m venv venv-test
$ source venv-test/bin/activate
$ pip3 install -r requirements-tests.txt
$ pytest
```
