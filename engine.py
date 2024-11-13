from vars import Vars
from utility import end_decreasing_for_length, end_increasing_for_length, lerp


class Engine:
    def __init__(self, current_price):
        self.is_buying = False
        self.is_shorting = False
        self.sell_fraction = 1 / 5
        self.buy_loss_limit = current_price
        self.short_loss_limit = current_price
        self.b_bought_price = 0
        self.s_bought_price = 0
        self.balance = 0

    def run(self, price_series):
        if len(price_series) < 3:
            return
        current_price = price_series[-1]
        self._buy(price_series)
        self._sell(current_price)
        self._short(price_series)
        self._buy_back(current_price)

    def _buy(self, price_series):
        current_price = price_series[-1]
        stock_move_amt = abs(price_series[-2] - price_series[-1])
        if self.is_buying:
            self.buy_loss_limit = lerp(self.buy_loss_limit, current_price, self.sell_fraction)
        if self._should_buy(price_series):
            self.is_buying = True
            self.b_bought_price = current_price
            self.buy_loss_limit = current_price - stock_move_amt

    def _sell(self, current_price):
        if self._should_sell(current_price):
            self.is_buying = False
            self.balance += current_price - self.b_bought_price

    def _short(self, price_series):
        current_price = price_series[-1]
        stock_move_amt = abs(price_series[-2] - price_series[-1])
        if self.is_shorting:
            self.short_loss_limit = lerp(self.short_loss_limit, current_price, self.sell_fraction)
        if self._should_short(price_series):
            self.is_shorting = True
            self.s_bought_price = current_price
            self.short_loss_limit = current_price + stock_move_amt

    def _buy_back(self, current_price):
        if self._should_buy_back(current_price):
            self.is_shorting = False
            self.balance += self.s_bought_price - current_price

    def _should_buy(self, price_series):
        return end_increasing_for_length(price_series, 2) and not self.is_buying

    def _should_sell(self, current_price):
        if self.is_buying:
            return current_price <= self.buy_loss_limit or Vars.instance().CURRENT_STEP == Vars.instance().TIME_STEPS
        else:
            return False

    def _should_short(self, price_series):
        return end_decreasing_for_length(price_series, 2) and not self.is_shorting

    def _should_buy_back(self, current_price):
        if self.is_shorting:

            return current_price >= self.short_loss_limit or Vars.instance().CURRENT_STEP == Vars.instance().TIME_STEPS
        else:
            return False

    def get_bl_limit(self):
        if self.is_buying:
            return self.buy_loss_limit
        return None

    def get_sl_limit(self):
        if self.is_shorting:
            return self.short_loss_limit
        return None
