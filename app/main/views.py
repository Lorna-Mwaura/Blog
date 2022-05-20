from flask import Flask, render_template
from . import main
# from flask_login import login_required, current_user
# from ..models import User
# from .forms import UpdateProfile
from .. import db

@main.route('/')
def index():
   
    title = 'Welcome to Pitches'

    # business_pitches = Pitch.get_pitches('business')
    # product_pitches = Pitch.get_pitches('product')
    # promotion_pitches = Pitch.get_pitches('promotion')

    return render_template('index.html', title = title)

