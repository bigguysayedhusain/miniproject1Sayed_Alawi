# INF601 - Advanced Programming in Python
# Sayed Husain Alawi
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path

tickers = ['MSFT', 'CSCO', 'AMZN', 'GOOGL', 'SAP']

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

    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], closing_prices_array)
    plt.xlabel('Last 10 Days')
    plt.xticks(range(1, 11, 1))
    plt.ylabel('Closing Prices')
    plt.grid(True)
    plt.title(f"{ticker} Closing Prices")
    plt.axis((0, 11, (min(closing_prices_list) - 2), max(closing_prices_list) + 2))

    plt.savefig(f'charts/{ticker}.png')

    plt.show()
