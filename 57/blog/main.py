from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_list = []


@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/a796439be42b2322a22d")
    blog_posts = response.json()
    for post in blog_posts:
        posts_list.append(post)
    return render_template("index.html", posts=blog_posts)


@app.route('/post/<int:page>')
def show_post(page):
    post_index = None
    for post in posts_list:
        if post['id'] == page:
            post_index = post
    return render_template("post.html", post=post_index)


if __name__ == "__main__":
    app.run(debug=True)
