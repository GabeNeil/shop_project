from db.runner import run_sql

from models.shop import Shop

from models.guitar import Guitar 

from models.manufacturer import Manufacturer

import repositories.guitar_respository as guitar_respository
import repositories.manufacturer_repository as manufacturer_repository

def save(shop):
    sql = "INSERT INTO shops (name, till) VALUES (%s, %s) RETURNING *"
    values = [shop.name, shop.till]
    results = run_sql(sql, values)
    id = results[0]['id']
    shop.id = id
    return shop 

def select_all():
    shops = []

    sql = "SELECT * FROM shops"
    results = run_sql(sql)

    for row in results:
        shop = Shop(row['name'], row['till'], row['id'])
        shops.append(shop)
    return shops

def select(id):
    shop = None
    sql = "SELECT * FROM shops WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        shop = Shop(result['name'], result['till'])
        
    return shop

def delete_all():
    sql = "DELETE FROM shops"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM shops WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(shop):
    sql = "UPDATE shops SET (name, till) = (%s, %s) WHERE id = %s"
    values = [shop.name, shop.till, shop.id]
    run_sql(sql, values)



