from coin import Coin
from engine import Engine
from grapher import Grapher
from series_manager import SeriesManager
from stock import Stock
from vars import Vars


def main():
    # Set up
    variables = Vars()
    stock = Stock(100)
    engine = Engine(stock.current_price)
    coin = Coin()
    coin.flip(autocorrelation=variables.AUTOCORRELATION)
    series_manager = SeriesManager()
    series_manager.add_price(stock.current_price)
    series_manager.add_step(engine.balance,
                            engine.buy_loss_limit,
                            engine.short_loss_limit,
                            engine.is_buying,
                            engine.is_shorting)

    # Perform market sim
    while variables.CURRENT_STEP <= variables.TIME_STEPS:
        if stock.current_price <= 0:
            print("Stock price has bottomed -> Company went bankrupt")
            break
        coin.flip(autocorrelation=variables.AUTOCORRELATION)
        stock.price_change(coin.current)
        series_manager.add_price(stock.current_price)
        engine.run(series_manager.stock_price_history)
        series_manager.add_step(engine.balance,
                                engine.get_bl_limit(),
                                engine.get_sl_limit(),
                                engine.is_buying,
                                engine.is_shorting)

        # Update time step
        variables.CURRENT_STEP += 1

    # Plot the bal history
    print(series_manager)
    grapher = Grapher()
    grapher.graph(series_manager.stock_price_history,
                  series_manager.bal_history,
                  series_manager.b_loss_lim_his,
                  series_manager.b_record,
                  series_manager.s_loss_lim_his,
                  series_manager.s_record)


if __name__ == "__main__":
    main()
