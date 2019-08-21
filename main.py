import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# the all-important app variable:
app = Flask(__name__)

#bootstrap
bootstrap = Bootstrap(app)

#index route
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    try:
        titel = '0x2019.de'
        line1 = 'You are using {}'.format(user_agent)
        return render_template('index_bootstrap.html', titel = titel, line1 = line1)
    except Exception as e:
        return str(e)

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


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5001, passthrough_errors=True)