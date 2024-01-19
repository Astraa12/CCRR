from flask import Flask, redirect, url_for, render_template, request
import requests, random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html', randInt = randInt)

randInt = random.randint(0, 6)