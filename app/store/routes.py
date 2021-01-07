from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from app.database import User, db, bcrypt, Model, ModelPhoto, ModelPrice
from app.store.forms import ModelForm, MaterialForm
from flask_login import login_user, current_user, logout_user

store = Blueprint('store', __name__)

#static model for testing

#models = [{
#        'name': 'Maketa 1',
#        'description': 'blablabla bla',
#        'creator_id': '1'
#        'price': '100',
#        'image_file': '',
#        'material': ''
#    },
#    {
#        'name': 'Maketa 2',
#        'description': 'blablabla blagragra',
#        'creator_id': '2'
#        'price': '100',
#        'image_file': '',
#        'material': ''
#    }
#]

@store.route('/admin_post_page', methods=['GET', 'POST']) #potrebno dodati stranicu za admina
#@login_required
def new_model():
    form = ModelForm()
    if form.validate_on_submit():
        model = Model(name=form.name.data, description=form.description.data, creator_id=current_user) #dodati image_name
        db.session.add(model)
        db.session.commit()
        # file upload image/video
        #flash('Nova maketa dodana!', 'succes')
        return redirect(url_for('index'))
    return render_template('create_model.html', title='Nova maketa', form=form)



@store.route('/makete_prikaz', methods=['GET', 'POST'])
#@login_required
def makete_prikaz_Instance():
    models = Model.query.all()
    return render_template('makete_prikaz.html', title='Makete', models=models)

@store.route('/makete/<int:model_id>', methods=['GET', 'POST'])
def model_Instance(model_id):
    model = Model.query.get_or_404(model_id)
    model_photo = ModelPhoto.query.filter_by(model_id=model.id).first().image_name
    model_video = ModelPhoto.query.filter_by(model_id=model.id).first().video_name

    materials = ModelPrice.query.filter_by(model_id=model.id).all()

    #ModelPrice(model_id=model.id, material=m_form.material.data, price=price)
    #model = Model(name=form.name.data, description=form.description.data, creator_id=current_user) #dodati image_name      uvezati model s material atributom + dodati dimenzije i boje u Model()
    #db.session.add(model_price)
    #db.session.commit()
    print(materials)
    return render_template('makete.html', title=model.name, model=model, model_photo=model_photo, model_video=model_video, materials=materials)
    
@store.route('/makete/<int:model_id>/updated', methods=['GET', 'POST'])    
def updatePrice(model_id, price):
    model = Model.query.get_or_404(model_id)
    model_photo = ModelPhoto.query.filter_by(model_id=model.id).first().image_name
    model_video = ModelPhoto.query.filter_by(model_id=model.id).first().video_name
    
    return render_template('makete.html', title=model.name, model=model, model_photo=model_photo, model_video=model_video, price=price, form=m_form) #model_material=m_form.material)
    #post request za updatePrice()






