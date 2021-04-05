from flask import Flask, render_template, request, redirect

from repositories import guitar_respository
from repositories import manufacturer_repository


from models.guitar import Guitar
from models.manufacturer import Manufacturer

from flask import Blueprint

guitar_blueprint = Blueprint("guitars", __name__)

@guitar_blueprint.route("/guitars")
def show_guitars():
    guitars = guitar_respository.select_all()
    return render_template("functions/guitars.html", all_guitars = guitars)

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