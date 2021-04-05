from db.runner import run_sql

from models.guitar import Guitar

import repositories.manufacturer_repository as manufacturer_repository

def save(guitar):
    sql = "INSERT INTO guitars (name, description, quantity, buy_cost, sell_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [guitar.name, guitar.description, guitar.quantity, guitar.buy_cost, guitar.sell_price, guitar.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    guitar.id = id
    return guitar 

def delete_all():
    sql =  "DELETE FROM guitars"
    run_sql(sql)

def select_all():
    guitars = []

    sql = "SELECT * FROM guitars"
    results = run_sql(sql)
    print(results)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        manufacturer_name = manufacturer.name
        guitar = Guitar(row['name'], row['description'], row['quantity'], row['buy_cost'], row['sell_price'], manufacturer_name)
        guitars.append(guitar)
    return guitars 


def select(id):
    guitar = None
    sql = "SELECT * FROM guitars WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        guitar = Guitar(result['name'], result['description'], result['quantity'], result['buy_cost'], result['sell_price'], manufacturer, result['id'])

    return guitar 

def delete(id):
    sql = "DELETE FROM guitars WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(guitar):
    sql = "UPDATE guitars SET (name, description, quantity, buy_cost, sell_price, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [guitar.name, guitar.description, guitar.quantity, guitar.buy_cost, guitar.sell_price, guitar.manufacturer.id, guitar.id]
    run_sql(sql, values)
