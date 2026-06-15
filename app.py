""" This module handles Flask app initialization and routes. """

import json
from flask import Flask, render_template

FILE_NAME = 'data/data.json'


app = Flask(__name__)


@app.route('/')
def index():
    """ Loads the json data file and displays it via the index page. """
    with open(FILE_NAME, encoding='utf-8') as json_file:
        blog_posts = json.load(json_file)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000, debug=True) # returns Not Found
