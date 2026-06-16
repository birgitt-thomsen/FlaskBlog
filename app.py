""" This module handles Flask app initialization and routes. """

import json
from flask import Flask, render_template, request, redirect, url_for

FILE_PATH = 'data/data.json'

app = Flask(__name__)


def load_posts():
    with open(FILE_PATH, encoding='utf-8') as file:
        return json.load(file)


def save_posts(posts):
    with open(FILE_PATH, "w", encoding='utf-8') as file:
        json.dump(posts, file, indent=4)


def fetch_post_by_id(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route('/')
def index():
    """ Loads the json data file and displays it via the index page. """
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = load_posts()

        # Generate next ID
        next_id = max(post["id"] for post in posts) + 1 if posts \
            else 1

        new_post = {
            "id": next_id,
            "author": request.form["author"],
            "title": request.form["title"],
            "content": request.form["content"],
            "likes": 0,
        }

        posts.append(new_post)

        save_posts(posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()

    posts = [post for post in posts if post["id"] != post_id]

    save_posts(posts)

    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    posts = load_posts()

    post = next(
        (p for p in posts if p["id"] == post_id),
        None
    )

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        post["author"] = request.form["author"]
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]

        save_posts(posts)

        return redirect(url_for("index"))

    return render_template("update.html", post=post)


@app.route('/like/<int:post_id>')
def like_post(post_id):
    posts = load_posts()

    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
            break

    save_posts(posts)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000, debug=True) # returns Not Found
