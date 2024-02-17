# INF601 - Advanced Programming in Python
# Sayed Husain Alawi
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import copy
from pathlib import Path

tickers = ['MSFT', 'TSLA', 'SONY', 'META', 'AAPL']

try:
    Path('charts').mkdir()
except FileExistsError:
    pass

