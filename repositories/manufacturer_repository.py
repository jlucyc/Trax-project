from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
import pdb

def save(manufacturer):
    # pdb.set_trace()
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
    