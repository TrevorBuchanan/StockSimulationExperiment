import math
from matplotlib import pyplot as plt
import matplotlib as mpl


class Grapher:
    @staticmethod
    def graph(stock_price_history, bal_history, b_loss_lim_his, b_record, s_loss_lim_his, s_record):
        # Set dark mode
        plt.style.use('dark_background')
        mpl.rcParams.update({
            'axes.facecolor': 'black',
            'axes.edgecolor': 'white',
            'axes.labelcolor': 'white',
            'figure.facecolor': 'black',
            'xtick.color': 'white',
            'ytick.color': 'white',
            'grid.color': 'gray',
            'text.color': 'white',
            'legend.facecolor': 'gray',
            'legend.edgecolor': 'white'
        })

        plt.figure(figsize=(16, 8))

        # Subplot 1: Stock Price History
        plt.subplot(2, 2, 1)
        plt.plot(stock_price_history, label='Stock Price History', color='blue')
        plt.plot(b_loss_lim_his, label='Buy loss limit history', color='green')
        plt.plot(s_loss_lim_his, label='Short loss limit history', color='red')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Stock Price History')
        plt.legend()

        # Subplot 2: PnL History
        plt.subplot(2, 2, 2)
        plt.plot(bal_history, label='PnL History', color='purple')
        plt.xlabel('Time')
        plt.ylabel('PnL')
        plt.title('PnL History')
        plt.legend()

        # Subplot 3: Buying History
        plt.subplot(2, 2, 3)
        plt.plot(b_record, label='Buy record', color='orange')
        plt.xlabel('Time')
        plt.ylabel('Buying')
        plt.title('Buying History')
        plt.legend()

        # Subplot 4: Shorting History
        plt.subplot(2, 2, 4)
        plt.plot(s_record, label='Short record', color='brown')
        plt.xlabel('Time')
        plt.ylabel('Shorting')
        plt.title('Shorting History')
        plt.legend()

        plt.tight_layout()  # Adjust layout for better spacing
        plt.show()

    @staticmethod
    def graph_util(series_list: list, labels: list) -> None:
        if len(series_list) != len(labels):
            raise Exception("Must provide same number of series as labels")

        # Set dark mode
        plt.style.use('dark_background')
        mpl.rcParams.update({
            'axes.facecolor': 'black',
            'axes.edgecolor': 'white',
            'axes.labelcolor': 'white',
            'figure.facecolor': 'black',
            'xtick.color': 'white',
            'ytick.color': 'white',
            'grid.color': 'gray',
            'text.color': 'white',
            'legend.facecolor': 'gray',
            'legend.edgecolor': 'white'
        })

        num_series = len(series_list)
        plt.figure(figsize=(16, 8))
        num_rows = math.floor(math.sqrt(num_series))
        num_columns = math.ceil(math.sqrt(num_series))

        for i, series in enumerate(series_list):
            plt.subplot(num_rows, num_columns, i + 1)
            plt.plot(series, label=labels[i], color='cyan')  # Default color for consistency
            if len(labels) - 1 >= i:
                plt.title(labels[i])
            plt.axis('off')  # Optional: remove axis for a cleaner look in `graph_util`

        plt.tight_layout()
        plt.show()
