import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


# the all-important app variable:
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#bootstrap
bootstrap = Bootstrap(app)

#flaskform
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    age  = IntegerField('How old are U?', validators=[DataRequired(), NumberRange(3, 100)])
    submit = SubmitField('Submit')


#index route
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    try:
        titel = '0x2019.de'
        line1 = 'You are using {}'.format(user_agent)
        return render_template('index.html', titel = titel, line1 = line1)
    except Exception as e:
        return str(e)
#user pages
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

#about page
@app.route('/about')
def about():
    try:
        return render_template('about.html', titel = 'About me', line1 = 'nothing to say')
    except Exception as e:
        return str(e)

#next page
@app.route('/next')
def next():
    try:
        return render_template('next.html', titel = 'NextPage', line1 = 'this follows next')
    except Exception as e:
        return str(e)

#quickform
@app.route('/quickform', methods = ['GET', 'POST'])
def quickform():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age']  = form.age.data
        flash('Everything is awesome.')
        return redirect('/quickform')           #url_for('quickform', _external=True))
    return render_template('quickform.html', \
                                form = form, \
                                name = session.get('name'), \
                                age = session.get('age'))
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5001, passthrough_errors=True)