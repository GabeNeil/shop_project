class Guitar:
    def __init__(self, name, description, quantity, buy_cost, sell_price, manufacturer, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity 
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.manufacturer = manufacturer
        self.id = id