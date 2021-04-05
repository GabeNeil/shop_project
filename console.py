import pdb

from models.shop import Shop
from models.guitar import Guitar 
from models.manufacturer import Manufacturer

import repositories.shop_repository as shop_repository
import repositories.guitar_respository as guitar_respository
import repositories.manufacturer_repository as manufacturer_repository


guitar_respository.delete_all()
manufacturer_repository.delete_all()
shop_repository.delete_all()


Fender = Manufacturer("Fender")
manufacturer_repository.save(Fender)

Gibson = Manufacturer("Gibson")
manufacturer_repository.save(Gibson)

guitar1 = Guitar("Stratocaster", "classic design", 5, 200, 600, Fender)
guitar_respository.save(guitar1)

guitar2 = Guitar("Les Paul", "perfect for hard rock", 3, 500, 1000, Gibson)
guitar_respository.save(guitar2)

shop1 = Shop("Gabetars", 3000)
shop_repository.save(shop1)

shop1.till = 3500
shop_repository.update(shop1)

guitar_respository.select_all()




