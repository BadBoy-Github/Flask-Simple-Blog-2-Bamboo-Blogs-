
from flask import Flask, render_template, request
import requests
import time
import smtplib
from dotenv import load_dotenv
import os

# Load environmental variables
load_dotenv()
email_id = os.getenv("EMAIL_ID")
password = os.getenv("PASSWORD")

# API Endpoint for posts
post_list = "https://api.npoint.io/f12c82394cf54590cf2c"

app = Flask(__name__)

@app.route('/')
def home():
    current_date = time.strftime("%Y-%m-%d")
    response = requests.get(post_list)
    all_posts = response.json()
    return render_template('index.html', all_posts=all_posts, time=current_date)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        mail_message = f"Subject:New Message from {name}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

        # Send mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email_id, password)
            connection.sendmail(from_addr=email_id, to_addrs="elayabarathiedison@gmail.com", msg=mail_message)

        return render_template('contact.html', tit="Successfully sent your message")
    return render_template('contact.html', tit="Let’s Connect!")

@app.route('/blog/<blog_id>')
def get_post(blog_id):
    current_date = time.strftime("%Y-%m-%d")
    response = requests.get(post_list)
    all_posts = response.json()
    requested_post = all_posts[int(blog_id) - 1]
    return render_template('post.html', blog_id=blog_id, post = requested_post, time=current_date)

if __name__ == '__main__':
    app.run(debug=True)