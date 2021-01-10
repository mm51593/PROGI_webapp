from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from sqlalchemy import exc
from app.database import User, db, bcrypt, Model, ModelPhoto, ModelPrice, ModelNotification
from app.store.forms import ModelForm, MaterialForm, ModelPriceForm
from app import application
from flask_login import login_user, current_user, logout_user
from uuid import uuid4
from os import path, listdir

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
        print("success")
        dimension = f"{form.dimension_1.data},{form.dimension_2.data},{form.dimension_3.data}"   #unesene dimenzije su spojene ',' npr. '100,120,150'
        colors = form.colors.data                                                                #unesene boje odvojene zarezom npr. 'plava,crvena,zelena'
        model = Model(name=form.name.data, description=form.description.data, creator_id=current_user.id, dimension=dimension, colors=colors) #dodati image_name
        db.session.add(model)
        db.session.commit()
        #dodati za photo i video obradu podataka    # file upload image/video
        filename = form.image.data.filename.split('.')
        extension = filename[-1]
        while True:
            filename = uuid4().hex + '.' + extension
            if filename not in listdir(path.join(application.root_path, application.config['MODEL_LOCATION'])):
                break

        form.image.data.save(path.join(application.root_path, application.config['MODEL_LOCATION'], filename))
        model_photo = ModelPhoto(image_name=filename, model_id=model.id)
        db.session.add(model_photo)
        db.session.commit()
        #flash('Nova maketa dodana!', 'succes')
        return redirect(url_for('index.homepage'))
    else:
        print(form.errors)
        for error in form.errors:
            print(error)
    return render_template('narudzba.html', title='Nova maketa', form=form)



@store.route('/makete_prikaz', methods=['GET', 'POST'])
#@login_required
def makete_prikaz_Instance():
    models = Model.query.all()
    return render_template('makete_prikaz.html', title='Makete', models=models)

@store.route('/makete/<int:model_id>', methods=['GET', 'POST'])
def model_Instance(model_id):
    model = Model.query.get_or_404(model_id)
    print(model_id)
    model_photo = ModelPhoto.query.filter_by(model_id=model.id).first().image_name
    model_dimensions = model.dimension.split(',')
    model_colors = model.colors.split(',')
    materials = ModelPrice.query.filter_by(model_id=model.id).all()
    #ModelPrice(model_id=model.id, material=m_form.material.data, price=price)
    #model = Model(name=form.name.data, description=form.description.data, creator_id=current_user) #dodati image_name
    #db.session.add(model_price)
    #db.session.commit()
    #print(materials)
    if request.method == "POST":
        if current_user.is_authenticated:
            if current_user.cart == None:
                current_user.cart = []
            #current_user.cart.append("")
            print(model_id, request.form.get("materijaliChoose"))
        else:
            return redirect(url_for("auth.login"))
    return render_template('makete.html', title=model.name, model=model, model_photo=model_photo, materials=materials, dimensions=model_dimensions, colors=model_colors)

@store.route('/prihvatimaketu', methods=['GET', 'POST'])
def model_approval():
    if request.method == 'POST':
        print(request.form)
        model_id = request.form['order_id']
        model = Model.query.filter_by(id=model_id).first()
        if request.form['response'] == 'Odbij':
            db.session.delete(model)
        else:
            model.approved = True
            for mat in application.config['MATERIALS']:
                MP = ModelPrice(model_id=model_id, material=mat, price=request.form[mat])
                db.session.add(MP)
            notif = ModelNotification(model_id=model_id, receiver=model.creator_id)
            db.session.add(notif)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            pass
        return redirect(url_for('store.model_approval'))
    orders = Model.query.filter_by(approved=False)
    return render_template('prihvat_makete.html', orders=orders, materials=application.config['MATERIALS'])
