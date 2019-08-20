import os
from flask import Flask, render_template

# the all-important app variable:
app = Flask(__name__)

@app.route('/')
def main():
    try:
        titel = 'ledderboge.net'
        return render_template('index_bootstrap.html', titel = titel, line1 = '+---- ledderboge.net ----+')
    except Exception as e:
        return str(e)
@app.route('/about')
def about():
    return render_template('about.html', titel = 'About me', line1 = 'nothing to say')

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5001, passthrough_errors=True)
