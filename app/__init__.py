from flask import Flask
from flask import render_template

app = Flask(__name__)

app.config.from_object('config')
from app import views

