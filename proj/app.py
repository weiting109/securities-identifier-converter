from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from converter import convert_fns, convertBbtoCUSIP, convert_id

app = Flask(__name__) #instantiate Flask app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    """
    Render templates and display tasks according to status
    """
    return render_template('index.html',to_convert='',converted='')

@app.route('/api/convert/',methods=['POST'])
def api_convert():
    """
    API that accepts JSON input with keys 'to-convert' and 'convert-type',
    returns JSON
    """
    if not request.json:
        abort(400)

    to_convert_str = request.json.get('to-convert','')
    convert_type = request.json.get('convert-type','bb-to-cusip')

    to_convert = to_convert_str.split(',')
    converted = ', '.join(convert_id(to_convert,convert_fns[convert_type]))

    return jsonify({'converted':converted}), 201

@app.route('/convert/',methods=['POST'])
def convert():
    """
    Passes form values to /api/convert/ to convert one identifier to another.
    """

    r = requests.post('http://127.0.0.1:5000/api/convert/', json = request.form) #update URL to global variable or when deployed

    to_convert_str = request.form['to-convert']
    convert_type = request.form['convert-type']

    return render_template('index.html',to_convert=to_convert_str,converted=r.json()['converted']), 201

if __name__ == '__main__':
    app.run(debug=True)
