from db.runner import run_sql

from models.manufacturer import Manufacturer
from models.guitar import Guitar

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id 
    return manufacturer

def delete_all():
    sql =  "DELETE FROM manufacturers"
    run_sql(sql)

def all_guitars(manufacturer):
    guitars = []

    sql = "SELECT * FROM guitars WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        guitar = Guitar(row['name'], row['description'], row['quantity'], row['buy_cost'], row['sell_price'], row['manufacturer_id'], row['id'])
        guitars.append(guitar)
    return guitars

def select(id): 
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['id'])
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row["id"])
        manufacturers.append(manufacturer)
    return manufacturers

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(manufacturer):
    sql = "UPDATE manufacturers SET name = %s WHERE id = %s"
    values = [manufacturer.name, manufacturer.id]
    run_sql(sql, values)
    