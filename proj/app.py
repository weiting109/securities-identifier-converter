from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from converter import convert_fns, convertBbtoCUSIP, convert_id

app = Flask(__name__) #instantiate Flask app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #instantiate SQLAlchemy

@app.route('/')
def index():
    """
    Render templates and display tasks according to status
    """
    return render_template('index.html',to_convert='',converted='')

@app.route('/convert/',methods=['GET','POST'])
def convert():
    """
    'GET' method API call takes string URL argument to-convert, a string of
        identifiers to be converted separated by commas and returns a string
        of converted identifiers, separated by commas.
    'POST' method does similar, except arguments are received through front-end
        form and displayed on front-end.
    """

    if request.method == 'POST':
        to_convert_str=request.form['to-convert']
        convert_type = request.form['convert-type']
    elif request.method == 'GET':
        query_parameters = request.args
        to_convert_str = query_parameters.get('to-convert')
        convert_type = query_parameters.get('convert-type')

    to_convert = to_convert_str.split(',')
    converted = ', '.join(convert_id(to_convert,convert_fns[convert_type]))

    if request.method == 'POST':
        return render_template('index.html',to_convert=to_convert_str,converted=converted)
    elif request.method == 'GET':
        return converted

if __name__ == '__main__':
    app.run(debug=True)
