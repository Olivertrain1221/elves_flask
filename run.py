import os
# Importing Flask class
from flask import Flask

# Creating a instance of this, storing it in a variable 'app'.
# The first argument of the Flask class, is the "name" of the application's module - our package.
app = Flask(__name__)

# Decorator used to wrap functions 
@app.route("/")
def index():
    return "Hello, world"

# making environment
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)