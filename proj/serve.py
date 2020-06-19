from flask import render_template, request, redirect, url_for, jsonify
import requests
from proj import app
from .converter import convert_fns, convertBbtoCUSIP, convert_id

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

    r = requests.post('https://ticker-converter.herokuapp.com/api/convert/', json = request.form) #update URL to global variable or when deployed

    to_convert_str = request.form['to-convert']
    convert_type = request.form['convert-type']

    return render_template('index.html',to_convert=to_convert_str,converted=r.json()['converted']), 201
