from flask import Blueprint, render_template

## define that this file is a blueprint of our application

views = Blueprint("views", __name__)


#define out first view

@views.route('/')
def home():
    return render_template("home.html")
    
