from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from app.database import User, db, bcrypt, Model, ModelPhoto, ModelPrice
from app.store.forms import ModelForm
from flask_login import login_user, current_user, logout_user

store = Blueprint('store', __name__)

#static model for testing

models = [{
        'name': 'Maketa 1',
        'description': 'blablabla bla',
        'creator_id': '1'
#        'price': '100',
#        'image_file': '',
#        'material': ''
    },
    {
        'name': 'Maketa 2',
        'description': 'blablabla blagragra',
        'creator_id': '2'
#        'price': '100',
#        'image_file': '',
#        'material': ''
    }
]

@store.route('/admin_post_page', methods=['GET', 'POST']) #potrebno dodati stranicu za admina
#@login_required
def new_model():
    form = ModelForm()
    if form.validate_on_submit():
        model = Model(name=form.name.data, description=form.description.data, creator_id=current_user) #dodati image_name
        db.session.add(model)
        db.session.commit()
        #flash('Nova maketa dodana!', 'succes')
        return redirect(url_for('index'))
    return render_template('create_model.html', title='Nova maketa', form=form)



@store.route('/makete_prikaz')
#@login_required
def makete_prikaz():
    #models = Model.query.all() staticki za svrhu testiranja trenutno
    return render_template('makete_prikaz.html', title='Makete', models=models)

@store.route('/makete/<int:model_id>')
def model(model_id):
    model = Model.query.get_or_404(model_id)
    return render_template('makete.html', title=Model.name, model=model)



#@store.route('/material', methods=['GET', 'POST'])
#def updatePrice():
#    pass