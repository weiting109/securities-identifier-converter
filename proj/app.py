from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from converter import convertBbtoCUSIP

app = Flask(__name__) #instantiate Flask app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #instantiate SQLAlchemy

@app.route('/', methods=['GET'])
def index():
    """
    Render templates and display tasks according to status
    """
    return render_template('index.html',to_convert="",converted="")

@app.route('/convert/',methods=['POST'])
def convert():
    to_convert_orig=request.form['to-convert']
    to_convert = to_convert_orig.split(',')
    converted=[]
    for bbticker in to_convert:
        converted.append(convertBbtoCUSIP(bbticker))
    converted = ', '.join(converted)
    return render_template('index.html',to_convert=to_convert_orig,converted=converted)

if __name__ == '__main__':
    app.run(debug=True)
