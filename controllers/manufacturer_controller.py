from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturer", __name__)

@manufacturers_blueprint.route("/manufacturer")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturer/index.html", manufacturers = manufacturers)


