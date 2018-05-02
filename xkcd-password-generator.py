from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
import records

class PasswordForm(FlaskForm):
    min_word_length = IntegerField('Minimum Length of Word')
    max_word_length = IntegerField('Maximum Length of Word')
    overall_word_length = IntegerField('Overall Maximum Length')
    generate = SubmitField('Generate password')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oqbe5vgm(&y)xjsuph$zx*-z8(3wp84a2#wlo%bqsipd-g%y#x'


@app.route('/')
def index():
    return render_template('index.html',form=PasswordForm())

@app.route('/generate_password',methods=['POST'])
def generate_password():
    form = PasswordForm(request.form)
    engine = records.Database('sqlite:///./xkcd.db')
    query = "SELECT word FROM xkcd_words WHERE length(word) > :min AND length(word) < :max"
    rows = engine.query(query,min=form.min_word_length.data,max=form.max_word_length.data)
    password = []
    for index in range(4):
        row = rows[index]
        password.append(row['word'])
    engine.close()
    return render_template('index.html',form=PasswordForm(),password=password)


if __name__ == '__main__':
    app.run(debug=True)
