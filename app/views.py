from flask import Flask, request, make_response,  render_template, url_for, jsonify
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
    return render_template('question.html', form=UserInput())


@app.route('/answer', methods=['POST'])
def answer():

    question = request.get_json()['user_input']
    # bot_answer = {"location":models.question.get_parsant, "bot_answer": models.question.answer}
    bot_answer = {"location": question, "bot_answer": question}
    text = open('app/templates/answer', 'r').read().encode('latin1').decode('utf8')

    string_answer = text.format(location=bot_answer['location'], bot_answer=bot_answer['bot_answer'])

    res = make_response(jsonify({'answer': string_answer}), 200)
    return res
