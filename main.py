# INF601 - Advanced Programming in Python
# Sayed Husain Alawi
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import copy
from pathlib import Path

tickers = ['MSFT']  # TODO add 'TSLA', 'SONY', 'META', 'AAPL' back to tickers

try:
    Path('charts').mkdir()
except FileExistsError:
    pass

for i in tickers:
    data = (yf.Ticker(i)).history(period='10d')

    closing_prices_list = []

    for i in data['Close']:
        closing_prices_list.append(i)

    closing_prices_array = np.array(closing_prices_list)

    plt.plot(closing_prices_array)
    plt.xlabel('Days')
    plt.ylabel('Closing Price')
    plt.title(f"{tickers} Closing Prices")
    plt.axis((1, 10, (min(closing_prices_list) - 2), max(closing_prices_list) + 2))

    plt.show()
    # print(closing_prices)
    # min(closing_prices)
    # max(closing_prices)

# TODO delete Temp.py
# TODO Don't forget to fulfill the requirements.txt
# TODO Don't forget to finish the README.md
