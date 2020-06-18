from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from converter import convertBbtoCUSIP

app = Flask(__name__) #instantiate Flask app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #instantiate SQLAlchemy

@app.route('/')
def index():
    """
    Render templates and display tasks according to status
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
