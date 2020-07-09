from flask import Flask, request,  render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config.from_object('config')

class UserInput(FlaskForm):
    user_question = StringField('', validators=[DataRequired()])


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', form=UserInput())

@app.route('/', methods=['POST'])
@app.route('/index/', methods=['POST'])
def answer():
    question = request.form['user_question']
    return question
