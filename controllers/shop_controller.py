from flask import Flask, render_template

from repositories import guitar_respository
from repositories import manufacturer_repository


from models.guitar import Guitar
from models.manufacturer import Manufacturer

from flask import Blueprint

guitar_blueprint = Blueprint("guitars", __name__)

@guitar_blueprint.route("/")
def 