
from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
import pdb

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results [0]['id']
    manufacturer.id = id
    return manufacturer


def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = Manufacturer(result['name'], result['id'])
    return manufacturer


def update(manufacturer):
    sql = "UPDATE manufacturers SET name = %s WHERE id = %s"
    values = [manufacturer.name, manufacturer.id]
    run_sql(sql, values)
    # pdb.set_trace()



def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def products(manufacturer):
    manufacturer = []

    sql = "SELECT * FROM products WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        products.append(product)
    return products

        
    