""" This module handles Flask app initialization and routes. """

import json
from flask import Flask, render_template, request, redirect, url_for

FILE_NAME = 'data/data.json'


app = Flask(__name__)


@app.route('/')
def index():
    """ Loads the json data file and displays it via the index page. """
    with open(FILE_NAME, encoding='utf-8') as file:
        blog_posts = json.load(file)
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with open(FILE_NAME, "r", encoding='utf-8') as file:
            blog_posts = json.load(file)

        # Generate next ID
        next_id = max(post["id"] for post in blog_posts) + 1 if blog_posts \
            else 1

        new_post = {
            "id": next_id,
            "author": request.form["author"],
            "title": request.form["title"],
            "content": request.form["content"]
        }

        blog_posts.append(new_post)

        with open(FILE_NAME, "w", encoding='utf-8') as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    with open(FILE_NAME, "r", encoding='utf-8') as file:
        posts = json.load(file)

    posts = [post for post in posts if post["id"] != post_id]

    with open(FILE_NAME, "w", encoding='utf-8') as file:
        json.dump(posts, file, indent=4)

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000, debug=True) # returns Not Found
