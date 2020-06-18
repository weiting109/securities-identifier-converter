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
    return render_template('index.html')

@app.route('/convert/',methods=['POST'])
def convert():
    to_convert=request.form['to-convert']
    return to_convert

if __name__ == '__main__':
    app.run(debug=True)
