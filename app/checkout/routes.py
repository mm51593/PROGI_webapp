from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.profile.forms import UpdateForm
from app.database import db, Profile

profile = Blueprint('checkout', __name__)

