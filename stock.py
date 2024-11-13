import random


class Stock:
    def __init__(self, price):
        self.original_price = price
        self.current_price = price

    def price_change(self, coin):
        stock_move_amt = random.uniform(0, 5) ** 2 / 5
        if coin:
            self.current_price += stock_move_amt
        else:
            self.current_price -= stock_move_amt
