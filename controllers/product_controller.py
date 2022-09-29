from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import pdb
products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)


# NEW - GET '/products/new'
@products_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    
    return render_template("products/new.html", all_products = products, manufacturers = manufacturers)


#CREATE - POST '/products'
@products_blueprint.route("/products", methods = ['POST'])
def create_product():

    name = request.form['product_name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']

    manufacturer = manufacturer_repository.select(manufacturer_id)

    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer)

    product_repository.save(product)
    return redirect('/products')


#SHOW - GET '/products/id'
@products_blueprint.route("/products/<id>", methods=['GET'])
def show(id):
    product = product_repository.select(id)
    manufacturer = product_repository.manufacturers(product)
    return render_template("manufacturers/show.html", product = product, manufacturer = manufacturer)


#EDIT - GET '/product/id/edit'
@products_blueprint.route("/products/<id>/edit", methods= ['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product = product, manufacturers = manufacturers)

    
#UPDATE - PUT '/product/id'
@products_blueprint.route("/products/<id>", methods = ['POST'])
def update_product(id):
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']

    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer, id)

    product_repository.update(product)
    return redirect('/products')

    

#DELETE - DELETE '/products/id'
@products_blueprint.route("/products/<id>/delete", methods = ['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')



