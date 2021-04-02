DROP TABLE IF EXISTS guitars;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY
    name VARCHAR, 
);

CREATE TABLE guitars (
    id SERIAL PRIMARY KEY, 
    name VARCHAR,
    description VARCHAR, 
    quantity INT,
    buy_cost FLOAT,
    sell_price FLOAT,
    manufacturer_id INT REFERENCES manufacturers(id)
);