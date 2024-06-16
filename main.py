import random
import matplotlib.pyplot as plt
from collections import deque

running_total: int = 0

prev: bool = random.choice([True, False])
coin: bool = False
same: bool = False
past = deque(maxlen=2)

buying: bool = False
shorting: bool = False
buy: bool = False
short: bool = False
sell: bool = False
buy_back: bool = False

stock_price: int = 500
original_price: int = stock_price
sell_fraction: float = 1 / 5
b_loss_limit: float = stock_price
s_loss_limit: float = stock_price

balance: int = 0
pnl: int = 0

num_flips: int = 10000

b_bought_price: int = 0
s_bought_price: int = 0

bal_history = []
stock_price_history = []
b_loss_lim_his = []
s_loss_lim_his = []
b_record = []
s_record = []

# High standard deviations indicate high volatility in stocks
# Volatility value (1 means always the same as previous, 0 means completely random)
volatility = 0.8

# TJ threshold
threshold = 3


def all_items_same(lst):
    return all(x == lst[0] for x in lst)


def show():
    if coin:
        print("Heads")
    else:
        print("Tails")


def flip(volatility_amt, prev_flip):
    global coin
    temp = 1 - volatility_amt
    if prev_flip is not None:
        if random.random() < (1 - temp):
            coin = prev_flip
        else:
            coin = random.choice([True, False])
    else:
        coin = random.choice([True, False])
    return coin


def lerp(a, b, t):
    return a + t * (b - a)


flip(volatility, prev)
past.append(coin)
for i in range(num_flips):
    if stock_price <= 0:
        print("Stock price invalid")
        break
    prev = coin
    flip(volatility, prev)
    past.append(coin)

    # Move stock price up or down based on coin flip
    if coin:
        stock_price += 1
    else:
        stock_price -= 1

    # Get whether the stock has increased over 2 iterations
    if all_items_same(list(past)):
        same = True
    else:
        same = False

    # Make the decision to buy or short the stock
    # if same:
    #     if coin and not buying:
    #         buy = True
    #         buying = True
    #
    #     if not coin and not shorting:
    #         short = True
    #         shorting = True

    # TJ's strategy
    if not buying and stock_price == original_price - threshold:
        b_bought_price = stock_price
        buy = True
        buying = True
    if not shorting and stock_price == original_price + threshold:
        s_bought_price = stock_price
        short = True
        shorting = True

    # Option to only buy or short at one time
    # if same_twice:
    #     if coin and not buying and not shorting:
    #         buy = True
    #         buying = True
    #     if not coin and not shorting and not buying:
    #         short = True
    #         shorting = True

    # Sell strategy 1: Sell when stock goes down
    # if not coin and buying:
    #     sell = True
    # if coin and shorting:
    #     buy_back = True

    # Sell strategy 2: Sell when stock goes back to sell fraction
    # if buying:
    #     if buy:
    #         b_bought_price = stock_price
    #         # Log lower bound
    #         b_loss_limit = stock_price - 1
    #     # Update loss limit
    #     if same:
    #         b_loss_limit = lerp(b_loss_limit, stock_price, sell_fraction)
    #
    #     if stock_price <= b_loss_limit or i == num_flips - 1:
    #         sell = True
    #
    # if shorting:
    #     if short:
    #         s_bought_price = stock_price
    #         # Log lower bound
    #         s_loss_limit = stock_price + 1
    #     # Update loss limit
    #     if same:
    #         s_loss_limit = lerp(s_loss_limit, stock_price, sell_fraction)
    #     if stock_price >= s_loss_limit or i == num_flips - 1:
    #         buy_back = True

    # TJ's strategy
    if (buying and not buy and stock_price == original_price) or (buying and num_flips - 1 == i):
        sell = True
    if (shorting and not short and stock_price == original_price) or (shorting and num_flips - 1 == i):
        buy_back = True

    # Perform the buy or sell action
    if buy:
        balance -= stock_price
        buy = False
    if sell:
        balance += stock_price
        buying = False
        sell = False
        pnl += (stock_price - b_bought_price)

    if short:
        balance += stock_price
        short = False
    if buy_back:
        balance -= stock_price
        shorting = False
        buy_back = False
        pnl += (s_bought_price - stock_price)

    # Print state data
    show()
    print(f'Stock price: {stock_price}')
    if buying:
        print(f'Buying bought price: {b_bought_price}')
        print(f'Buying loss limit: {b_loss_limit}')
    if shorting:
        print(f'Shorting bought price: {s_bought_price}')
        print(f'Shorting loss limit: {s_loss_limit}')
    print(f'PnL: {pnl}')
    print()

    # Loop changes
    bal_history.append(pnl)
    stock_price_history.append(stock_price)
    b_loss_lim_his.append(b_loss_limit)
    s_loss_lim_his.append(s_loss_limit)
    if buying:
        b_record.append(20)
    else:
        b_record.append(10)
    if shorting:
        s_record.append(20)
    else:
        s_record.append(10)

# Print end result
print("Ending")
print(pnl)

# Plot the bal history

plt.figure()
plt.plot(stock_price_history, label='Stock Price History')
plt.plot(bal_history, label='PnL History')
# plt.plot(b_loss_lim_his, label='Buy loss limit history')
# plt.plot(b_record, label='Buy record')
# plt.plot(s_loss_lim_his, label='Short loss limit history')
# plt.plot(s_record, label='Short record')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Balance and Stock Price History')
plt.legend()
plt.show()
