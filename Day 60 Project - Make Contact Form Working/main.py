import datetime
import smtplib

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"
SMTP_SERVER = "Your Email Provider's SMTP Address"  # Update this with your SMTP server's address


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP(SMTP_SERVER, port=587) as connection:  # Use the appropriate port for your SMTP server
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            break
    return render_template("post.html", post=requested_post)


@app.context_processor
def inject_year():
    current_year = datetime.datetime.now().year
    return {'year': current_year}


if __name__ == "__main__":
    app.run(debug=True)
