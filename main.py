
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

post_list = "https://api.npoint.io/f12c82394cf54590cf2c"

@app.route('/')
def home():
    current_date = time.strftime("%Y-%m-%d")
    response = requests.get(post_list)
    all_posts = response.json()
    return render_template('index.html', all_posts=all_posts, time=current_date)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog/<blog_id>')
def get_post(blog_id):
    current_date = time.strftime("%Y-%m-%d")
    response = requests.get(post_list)
    all_posts = response.json()
    requested_post = all_posts[int(blog_id) - 1]
    return render_template('post.html', blog_id=blog_id, post = requested_post, time=current_date)

if __name__ == '__main__':
    app.run(debug=True)