# INF601 - Advanced Programming in Python
# Sayed Husain Alawi
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path

tickers = ['MSFT']  # TODO add 'TSLA', 'SONY', 'META', 'AAPL' back to tickers

try:
    Path('charts').mkdir()
except FileExistsError:
    pass

for ticker in tickers:
    data = (yf.Ticker(ticker)).history(period='10d')

    closing_prices_list = []

    for i in data['Close']:
        closing_prices_list.append(i)

    closing_prices_array = np.array(closing_prices_list)

    plt.plot(closing_prices_array)
    plt.xlabel('Last 10 Days')
    plt.ylabel('Closing Prices')
    plt.title(f"{ticker} Closing Prices")
    plt.axis((1, 10, (min(closing_prices_list) - 2), max(closing_prices_list) + 2))

    plt.savefig(f'charts/{ticker}.png')

    plt.show()


# TODO delete Temp.py
# TODO Don't forget to finish the README.md
