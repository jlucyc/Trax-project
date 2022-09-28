from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

#NEW - GET '/manufacturers/new'
@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    products = product_repository.select_all()
    return render_template("manufacturers/new.html", products=products)


#CREATE - POST '/manufacturers'
@manufacturers_blueprint.route("/manufacturers", methods = ['POST'])
def create_manufacturer():
    name = request.form['manufacturer_name']
    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

#SHOW - GET '/manufacturers/id'
@manufacturers_blueprint.route("/manufacturers/<id>")
def show(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer = manufacturer)

#EDIT - GET '/manufacturers/id/edit'
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)

#UPDATE - PUT 'manufacturer/id'
@manufacturers_blueprint.route("/manufacturers/<id>", methods = ['POST'])
def update_manufacturer(id):
    name = request.form['name']
    manufacturer = Manufacturer(name, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')



#DELETE - DELETE '/products/id'
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods = ['POST'])
def delete_manufacturer(id):
    print("Here")
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')

