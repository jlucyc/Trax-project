from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.manufacturer.id]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['manufacturer_id'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        product = Product(result['name'], result['description'], result['stock_quantity'],result['buying_cost'], result['selling_price'], result['manufacturer'], result['id'])
    return product
    