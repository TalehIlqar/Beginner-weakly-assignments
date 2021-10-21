from flask import render_template

from app import app


post_list = ['Post 1', 'Post 2', 'Post 3']

@app.route('/book')
def home():
    return render_template('index.html', post_list = post_list)


@app.route('/book/<int:post_index>')
def post_detail(post_index):
    post = post_list[post_index]
    return render_template('posts.html', post_var = post)


@app.route('/posts')
def posts():
    return render_template('post_list.html', show_block=True, posts = post_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')
