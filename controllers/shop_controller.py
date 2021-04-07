from flask import Flask, render_template, request, redirect

from repositories import guitar_respository
from repositories import manufacturer_repository
from repositories import shop_repository


from models.guitar import Guitar
from models.manufacturer import Manufacturer
from models.shop import Shop

from flask import Blueprint

guitar_blueprint = Blueprint("guitars", __name__)

@guitar_blueprint.route("/guitars")
def show_guitars():
    manufacturers = manufacturer_repository.select_all()
    guitars = guitar_respository.select_all()
    return render_template("functions/guitars.html", all_guitars = guitars, all_manufacturers = manufacturers)

@guitar_blueprint.route("/manufacturers")
def show_manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("functions/manufacturers.html", all_manufacturers = manufacturers)

@guitar_blueprint.route("/manufacturers", methods=['POST'])
def add_manufacturer():
    name = request.form['name']
    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@guitar_blueprint.route("/manufacturers/<id>")
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manu_guitars = manufacturer_repository.all_guitars(manufacturer)
    return render_template("functions/showman.html", manufacturer = manufacturer, manu_guitars = manu_guitars)

@guitar_blueprint.route("/manufacturers/<id>/edit")
def man_edit_page(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("functions/editmanu.html", manufacturer = manufacturer)

@guitar_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    manufacturer = Manufacturer(name, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

@guitar_blueprint.route("/manufacturers/<id>/delete", methods=['GET','POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")


@guitar_blueprint.route("/guitars", methods=['POST'])
def add_guitar():
    name = request.form['name']
    description = request.form['description']
    quantity = request.form['quantity']
    buy_cost = request.form['buy_cost']
    sell_price = request.form['sell_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    guitar = Guitar(name, description, quantity, buy_cost, sell_price, manufacturer)
    guitar_respository.save(guitar)
    return redirect('/guitars')


@guitar_blueprint.route("/guitars/<id>", methods=['GET'])
def show_guitar(id):
    guitar = guitar_respository.select(id)
    guitar_markup = guitar.calculate_markup()
    return render_template('functions/showguitar.html', guitar = guitar, guitar_markup = guitar_markup)


@guitar_blueprint.route("/guitars/<id>/edit")
def guitar_edit_page(id):
    guitar = guitar_respository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('functions/editguitar.html', guitar = guitar, all_manufacturers = manufacturers)

@guitar_blueprint.route("/guitars/<id>", methods=['POST'])
def update_guitar(id):
    name = request.form['name']
    description = request.form['description']
    quantity = request.form['quantity']
    buy_cost = request.form['buy_cost']
    sell_price = request.form['sell_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    guitar = Guitar(name, description, quantity, buy_cost, sell_price, manufacturer, id)
    guitar_respository.update(guitar)
    return redirect('/guitars')


@guitar_blueprint.route("/guitars/<id>/delete", methods=['GET','POST'])
def delete_guitar(id):
    guitar_respository.delete(id)
    return redirect("/guitars")

@guitar_blueprint.route("/till")
def get_shop():
    shops = shop_repository.select_all()
    return render_template('functions/shop.html', shops = shops)

@guitar_blueprint.route("/till/<id>")
def get_till(id):
    shop = shop_repository.select(id)
    return render_template('functions/till.html', shop = shop)

@guitar_blueprint.route("/guitars/<id>/order")
def get_order_page(id):
    shops = shop_repository.select_all()
    guitar = guitar_respository.select(id)
    return render_template('functions/order.html', guitar = guitar, shops = shops)

@guitar_blueprint.route("/guitars/<id>/order", methods=["POST"])
def order_guitars(id):
    guitar = guitar_respository.select(id)
    new_quantity = int(request.form['quantity'])
    shop_id = request.form['shop_id']
    shop = shop_repository.select(shop_id)
    amount = guitar.buy_cost * new_quantity
    shop.till = shop.till - amount
    shop_repository.update(shop)
    guitar.quantity = guitar.quantity + new_quantity
    guitar_respository.update(guitar)
    return redirect(f"/guitars/{guitar.id}")

@guitar_blueprint.route("/guitars/<id>/sell")
def get_sales_page(id):
    shops = shop_repository.select_all()
    guitar = guitar_respository.select(id)
    return render_template('functions/sell.html', shops = shops, guitar = guitar)

@guitar_blueprint.route("/guitars/<id>/sell", methods=["POST"])
def sell_guitars(id):
    guitar = guitar_respository.select(id)
    sale_quantity = int(request.form['quantity'])
    shop_id = request.form['shop_id']
    shop = shop_repository.select(shop_id)
    sale_amount = guitar.sell_price * sale_quantity
    shop.till = shop.till + sale_amount
    shop_repository.update(shop)
    guitar.quantity = guitar.quantity - sale_quantity
    guitar_respository.update(guitar)
    return redirect(f"/guitars/{guitar.id}")