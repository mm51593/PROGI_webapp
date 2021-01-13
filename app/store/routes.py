from flask import Blueprint, render_template, url_for, redirect, request, session
from sqlalchemy import exc
from app.database import User, db, Model, ModelPhoto, ModelPrice, Cart, CartModel, ModelNotification
from app.store.forms import ModelForm
from app import application
from flask_login import current_user
from uuid import uuid4
from os import path, listdir

store = Blueprint('store', __name__)

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
    models = Model.query.filter_by(approved=True)
    return render_template('makete_prikaz.html', title='Makete', models=models)

@store.route('/makete/<int:model_id>', methods=['GET', 'POST'])
def model_Instance(model_id):
    model = Model.query.get_or_404(model_id)
    model_photo = ModelPhoto.query.filter_by(model_id=model.id).first().image_name
    model_dimensions = model.dimension.split(',')
    model_colors = model.colors.split(',')
    materials = ModelPrice.query.filter_by(model_id=model.id).all()
    model_creator = User.query.filter_by(id=model.creator_id).first()
    if request.method == "POST":
        if current_user.is_authenticated:
            cart_user = Cart.query.filter_by(buyer_id=current_user.id).first()
            if cart_user is None:
                cart_user = Cart(buyer_id=current_user.id)
                db.session.add(cart_user)
                try:
                    db.session.commit()
                except exc.SQLAlchemyError:
                    pass
            material_choice = request.form.get("materijaliChoose")
            item_in_cart = CartModel.query.filter_by(cart_id=cart_user.buyer_id, model_id=model.id, material=material_choice).first()
            if item_in_cart is None:
                item_price = ModelPrice.query.filter_by(model_id=model.id, material=material_choice).first().price
                cart_m_user = CartModel(cart_id=cart_user.buyer_id, model_id=model.id, material=material_choice, price=item_price, quantity=1)
                db.session.add(cart_m_user)
            else:
                item_in_cart.quantity += 1
            try:
                db.session.commit()
                #flash('Maketa dodana u košaricu!', 'succes')
            except exc.SQLAlchemyError:
                pass
        else:
            if not session.get('cart', None):
                session['cart'] = []
            material_choice = request.form.get("materijaliChoose")
            inCart = False
            for elem in session['cart']:
                if elem['model_id'] == model_id and elem['material'] == material_choice:
                    elem['quantity'] += 1
                    inCart = True
                    break
            if not inCart:
                item_price = ModelPrice.query.filter_by(model_id=model_id, material=material_choice).first().price
                session['cart'].append(dict(model_id=model_id, material=material_choice, price=item_price, quantity=1))
    return render_template('makete.html', title=model.name, model=model, model_photo=model_photo, materials=materials, dimensions=model_dimensions, colors=model_colors, model_creator=model_creator)

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
            notif = ModelNotification(model_id=model_id, receiver_id=model.creator_id)
            db.session.add(notif)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            pass
        return redirect(url_for('store.model_approval'))
    orders = Model.query.filter_by(approved=False)
    return render_template('prihvat_makete.html', orders=orders, materials=application.config['MATERIALS'])

@store.route('/obavijesti')
def my_notifications():
    if current_user.is_authenticated:
        notifs = ModelNotification.query.filter_by(receiver_id=current_user.id).order_by(ModelNotification.time_create.desc()).all()
        models = []
        for notif in notifs:
            models.append(Model.query.filter_by(id=notif.model_id).first())
            notif.seen = True
        db.session.commit()
    else:
        return redirect(url_for("auth.login"))
    return render_template('makete_prikaz.html', title='Obavijesti', models=models)

