from flask import Flask
from datetime import datetime
app = Flask(__name__)
import os
import random
from flask import send_file
import time

@app.route('/get_image')
def get_image():
    filename = 'ip.png'
    return send_file(filename, mimetype='image/png')


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

