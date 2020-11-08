from flask import Blueprint, render_template, redirect, request, url_for
from app.database import Story, StoryContent, db
from datetime import datetime
from app import application
from flask_login import current_user
from os import path
from uuid import uuid4


stories = Blueprint('story', __name__)

@stories.route('/storyrequest', methods=['GET', 'POST'])
def add_content():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    print(current_user)
    print(request.form)
    print(request.files)

    # TODO: sanitacija ulaza

    if request.method == "POST":
        if int(request.form['input-number']) > 0:
            newstory = Story(title=request.form["story-title"], author_id=current_user.id, time_created=datetime.now())
            db.session.add(newstory)
            db.session.commit()

            for form in request.form:
                if form.startswith("text"):
                    newcontentpiece = StoryContent(story_id=newstory.id, ordinal_number=int(form.split('-')[-1]), story_text=request.form[form])
                    db.session.add(newcontentpiece)

            for file in request.files:
                filename = request.files[file].filename.split('.')
                filename = uuid4().hex + '.' + filename[-1]
                request.files[file].save(path.join(application.config['STORY_LOCATION'], filename))

                newcontentpiece = StoryContent(story_id=newstory.id, ordinal_number=int(file.split('-')[-1]))
                if file.startswith("image"):
                    newcontentpiece.image_name = filename
                else:
                    newcontentpiece.video_name = filename

                db.session.add(newcontentpiece)

            db.session.commit()
    return render_template("prijedlog_price.html", title="Zahtjev priče")
