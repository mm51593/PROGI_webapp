from flask import Blueprint, render_template, redirect, request
from app.stories.forms import UploadForm, SingleFileForm

stories = Blueprint('story', __name__)

@stories.route('/storyrequest', methods=['GET', 'POST'])
def add_content():
    print(request.form)
    return render_template("prijedlog_price.html", title="Zahtjev priče")
