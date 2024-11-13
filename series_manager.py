class SeriesManager:
    def __init__(self):
        self.bal_history = []
        self.stock_price_history = []
        self.b_loss_lim_his = []
        self.s_loss_lim_his = []
        self.b_record = []
        self.s_record = []

    def add_step(self, balance, stock_price, buy_loss_limit, short_loss_limit, is_buying, is_shorting):
        self.bal_history.append(balance)
        self.stock_price_history.append(stock_price)
        self.b_loss_lim_his.append(buy_loss_limit)
        self.s_loss_lim_his.append(short_loss_limit)
        if is_buying:
            self.b_record.append(1)
        else:
            self.b_record.append(0)
        if is_shorting:
            self.s_record.append(1)
        else:
            self.s_record.append(0)
