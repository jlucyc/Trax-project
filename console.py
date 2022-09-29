import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository


product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Body Skill", "id")
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Live Fitness", "id")
manufacturer_repository.save(manufacturer_2)

def margin(selling_price, buying_cost):
    return (selling_price - buying_cost)




product_1 = Product("Treadmill", "Indoor running machine", 7, 500, 80, margin, manufacturer_1)
product_repository.save(product_1)


product_2 = Product("Air Bike", "conditioning bike", 1, 750, 1000, margin, manufacturer_2)
product_repository.save(product_2)

product_3 = Product("Rowing Machine", "Indoor rower", 3, 400, 650, margin, manufacturer_2)
product_repository.save(product_3)

product_4 = Product("Power Bag", "20kg Weighted Bag", 15, 20, 40, margin, manufacturer_1)
product_repository.save(product_4)

product_5 = Product("Battle Rope", "Big heavy rope", 0, 40, 75, margin, manufacturer_1)
product_repository.save(product_5)

product_6 = Product("Resistance Band", "Band used for strength training", 20, 10, 20, margin, manufacturer_1)
product_repository.save(product_6)


pdb.set_trace()