from flask import Flask, request, make_response,  render_template, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

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
    # bot_answer = {"location":models.question.get_parsant, "bot_answer": models.question.answer}
    bot_answer = {"location": question, "bot_answer": question}
    res = make_response(jsonify(bot_answer), 200)
    return res
