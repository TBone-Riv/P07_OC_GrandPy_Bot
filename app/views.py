from flask import Flask, request, make_response,  render_template, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import app.models as models

app = Flask(__name__)

app.config.from_object('config')


class UserInput(FlaskForm):
    user_question = StringField('')

    submit = SubmitField('Submit')


@app.route('/')
@app.route('/index/')
def index():
    return render_template('question.html', form=UserInput())


@app.route('/answer', methods=['POST', 'GET'])
def answer():
    question = request.json['user_input']
    question = models.Question(question)
    bot_answer = {"location": question.parse(), "bot_answer": question.answer()}
    res = make_response(jsonify(bot_answer), 200)
    return res
