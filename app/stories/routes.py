from flask import Blueprint, render_template, redirect, request, url_for, send_from_directory, abort
from app.database import Story, StoryContent, Comment, User, db
from datetime import datetime
from app import application
from flask_login import current_user
from os import path, listdir
from uuid import uuid4


stories = Blueprint('story', __name__)

@stories.route('/storyrequest', methods=['GET', 'POST'])
def add_content():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    ret_error = None

    if request.method == "POST":
        passing = True
        for form in request.form:
            if form.startswith('text') and request.form[form] == '':
                passing = False
                break
        for file in request.files:
            if request.files[file].filename == '':
                passing = False
                break
        if passing:
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
                    extension = filename[-1]
                    while True:
                        filename = uuid4().hex + '.' + extension
                        if filename not in listdir(path.join(application.root_path, application.config['STORY_LOCATION'])):
                            break

                    request.files[file].save(path.join(application.root_path, application.config['STORY_LOCATION'], filename))

                    newcontentpiece = StoryContent(story_id=newstory.id, ordinal_number=int(file.split('-')[-1]))
                    if file.startswith("image"):
                        newcontentpiece.image_name = filename
                    else:
                        newcontentpiece.video_name = filename

                    db.session.add(newcontentpiece)

                db.session.commit()
                return redirect(url_for('story.display_story', story_id=newstory.id))
        else:
            ret_error = "Greška pri prijenosu"
    return render_template("prijedlog_price.html", title="Zahtjev priče", error=ret_error)



@stories.route('/story/<story_id>', methods=['GET', 'POST'])      ## ?????
def display_story(story_id):
    try:
        story = Story.query.filter_by(id=story_id).first()
        story_author = User.query.filter_by(id=story.author_id).first()
        comments = Comment.query.filter_by(id_story=story_id).order_by(Comment.timestamp.desc()).all()
        for comment in comments:
            if comment.author_id == 0:
                comment.author_name = 'Anonymous'
            else:
                comment.author_name = User.query.filter_by(id=comment.author_id).first().username
    except AttributeError:
        return abort(404)

    if not story.validated and (not current_user.is_authenticated or current_user.is_authenticated and not (current_user.id == 1 or current_user.id == story.author_id)):
        abort(403)
    
    if request.method == "POST":                                    ## ??????????                      
        if len(request.form['objavitiKomentar']) > 0:
            if current_user.is_authenticated:
                author_id = current_user.id
            else:
                author_id = 0
            comment = Comment(text=request.form['objavitiKomentar'], author_id=author_id, timestamp = datetime.now(), id_story=story_id)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('story.display_story', story_id=story_id))    ##   request.url umjesto stories.display_story ??
                              
    story_elements = sorted(StoryContent.query.filter_by(story_id=story_id), key=lambda x: x.ordinal_number)
    print(story_elements)
    return render_template("citavaPrica.html", title="Prica", story=story, story_author=story_author, story_elements=story_elements, comments=comments, elem_len=len(story_elements)) ##my


@stories.route('/story_element/<file>')
def pull_file(file):
    route = path.join(application.root_path, application.config['STORY_LOCATION'])
    return send_from_directory(route, file)


@stories.route('/storyvalidation/<story_id>', methods=['GET', 'POST'])
def validation(story_id):

    validationstory = Story.query.filter_by(id=story_id).first()
    story_title = validationstory.title
    story_elements = sorted(StoryContent.query.filter_by(story_id=story_id), key=lambda x: x.ordinal_number)
    if request.method == 'POST':
        print(request.form)
        if current_user.id == 1:
            if request.form.get('prihvPonudaPric', False) == 'Prihvati':
                validationstory.validated = True
                db.session.add(validationstory)
                db.session.commit()
                return redirect(url_for('story.display_story_list_validation'))
            elif request.form.get('odbPonudaPric', False) == 'Odbaci':
                db.session.delete(validationstory)
                db.session.commit()
                return redirect(url_for('story.display_story_list_validation'))
        else:
            abort(404)
    return render_template("prihvat_price.html", title="Prihvat price", story_title=story_title, story_elements=story_elements, elem_len=len(story_elements))


@stories.route('/stories')
def display_story_list():
    stories = Story.query.filter_by(validated=True).all()
    for elem in stories:
        elem.author_name = User.query.filter_by(id=elem.author_id).first().username
    return render_template('price.html', stories=stories)

@stories.route('/storiesforvalidation')
def display_story_list_validation():
    stories = Story.query.filter_by(validated=False).all()
    for elem in stories:
        elem.author_name = User.query.filter_by(id=elem.author_id).first().username
    return render_template('prihvat_price_list.html', stories=stories)
