import os
from flask import Flask, render_template

# the all-important app variable:
app = Flask(__name__)

#main route
@app.route('/')
def main():
    try:
        titel = '0x2019.de'
        return render_template('index_bootstrap.html', titel = titel, line1 = '+---- 0x2019.de ----+')
    except Exception as e:
        return str(e)

#about page
@app.route('/about')
def about():
    try:
        return render_template('about.html', titel = 'About me', line1 = 'nothing to say')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5001, passthrough_errors=True)