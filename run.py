import os
# Importing Flask class
from flask import Flask, render_template

# Creating a instance of this, storing it in a variable 'app'.
# The first argument of the Flask class, is the "name" of the application's module - our package.
app = Flask(__name__)

# Decorator used to wrap functions 
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template(careers.html)


# making environment
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
        ##never have debug = true in pose depoloyment
