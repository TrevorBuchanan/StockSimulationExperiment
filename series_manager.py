from tabulate import tabulate


class SeriesManager:
    def __init__(self):
        self.bal_history = []
        self.stock_price_history = []
        self.b_loss_lim_his = []
        self.s_loss_lim_his = []
        self.b_record = []
        self.s_record = []

    def add_price(self, stock_price):
        self.stock_price_history.append(stock_price)

    def add_step(self, balance, buy_loss_limit, short_loss_limit, is_buying, is_shorting):
        self.bal_history.append(balance)
        self.b_loss_lim_his.append(buy_loss_limit)
        self.s_loss_lim_his.append(short_loss_limit)
        self.b_record.append(is_buying)
        self.s_record.append(is_shorting)

    def __repr__(self):
        if not (len(self.bal_history) == len(self.stock_price_history) == len(self.b_loss_lim_his) ==
                len(self.s_loss_lim_his) == len(self.b_record) == len(self.s_record)):
            raise Exception()

        headers = [
            "Step",
            "Balance",
            "Stock Price",
            "Buy Loss Limit",
            "Short Loss Limit",
            "Buying?",
            "Shorting?"
        ]
        rows = [
            [
                i,
                self.bal_history[i],
                self.stock_price_history[i],
                self.b_loss_lim_his[i],
                self.s_loss_lim_his[i],
                self.b_record[i],
                self.s_record[i],
            ]
            for i in range(len(self.bal_history))
        ]
        return tabulate(rows, headers=headers, tablefmt="grid")
