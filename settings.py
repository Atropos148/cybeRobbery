class Player:
    def __init__(self, name, money, heat, intel, inventory):
        self.name = name
        self.money = money
        self.heat = heat
        self.intel = intel
        self.inventory = inventory


class World:
    def __init__(self, server_security):
        self.server_security = server_security


class Store:
    def __init__(self, intel_price, intel_amount):
        self.intel_price = intel_price
        self.intel_amount = intel_amount
