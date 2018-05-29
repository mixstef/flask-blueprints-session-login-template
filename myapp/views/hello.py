from flask import Blueprint,render_template
from flask_login import login_required
from pymongo import ReturnDocument

from ..app import mongo


hello = Blueprint('hello',__name__)


@hello.route('/')
@login_required
def index_page():

	return render_template('index.html')
	

@hello.route('/other')
@login_required
def other_page():

	return render_template('other.html')

