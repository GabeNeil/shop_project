import pdb

from models.shop import Shop
from models.guitar import Guitar 
from models.manufacturer import Manufacturer

shop = Shop("Gabe's Gabetars", 4000)


guitar1 = Guitar("Stratocaster", "classic, timeless design", 5, 200, 600, "Fender")

guitar2 = Guitar("Les Paul", "perfect for hard rock", 3, 500, 1000, "Gibson")


manufacturer1 = Manufacturer("Fender")

manufacturer2 = Manufacturer("Gibson")




