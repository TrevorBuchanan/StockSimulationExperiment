import random
from collections import deque


class Coin:
    def __init__(self):
        self.current = None
        self.history = deque(maxlen=2)

    def flip(self, autocorrelation):
        if len(self.history) > 0:
            prev_flip = self.history[-1]
        else:
            prev_flip = None
        temp = 1 - autocorrelation
        if prev_flip is not None:
            if random.random() < (1 - temp):
                coin = prev_flip
            else:
                coin = random.choice([True, False])
        else:
            coin = random.choice([True, False])
        self.current = coin
        self.history.append(coin)
        return coin

    def show(self):
        if self.current:
            print("Heads")
        else:
            print("Tails")
