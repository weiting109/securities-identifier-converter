## Instructions

### To run the app prototype:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 proj/app.py
```
Please run prototype app on localhost port 5000 (see 'To use API for conversion for more info')

### To test the converter functions
```
$ python3 -m venv venv-test
$ source venv-test/bin/activate
$ pip3 install -r requirements-tests.txt
$ pytest
```

### To use API for conversion
Currently, URL: http://127.0.0.1:5000/api/convert/
Accept JSON data with the keys:
- `to-convert`: string of identifiers separated by commas
- `convert-type`: string indicating conversion type. Current possible values are 'bb-to-cusip'.
Returns JSON data with key:
- `converted`: string of converted identifiers separated by commas

### Front-end users
Access the application at http://127.0.0.1:5000/
