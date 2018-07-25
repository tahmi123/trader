from flask import Flask, request, render_template, flash
import starter 

# Stuff to initialize the Flask app
app = Flask(__name__)

# This decorator tells Flask to use this function as a webpage handler/renderer

@app.route('/')
def start():
    return ("hello tammy you fucker")

if __name__ == '__main__':
    app.run()