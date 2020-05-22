# financial-stock-market-app
Stock Market Analysis with Python

## Overview.
Getting stock market data via Python, so without having to browse and download files from websites.
* You're going to get these data in [Pandas]() data frames, so in tables inside Python and then they are ready to analyze (recent data, almost real-time). 
* We'll use the Bokeh library to visualizing stock market data by creating this graph.

### Requirements.
1. [Pandas_datareader](https://pypi.org/project/pandas-datareader/).
2. [Bokeh](https://docs.bokeh.org/en/latest/index.html).
3. [Flask](https://flask-doc.readthedocs.io/en/latest/).
* **NOTE** - For Windows users use [precompiled standard library packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/) to install the required libraries. 

## Introduction.
The stock market works like an auction where investors buy and sell shares of stocks; These are a small piece of ownership of a public corporation. Stock prices usually reflect investors' opinions of what the company's earnings will be. Buyers try to get the lowest price so that they can sell it for a profit later. Stock market returns are known to be influenced by the key macro economic variables such as the GDP, inflation rate, and exchange rate,

### Example stock table
|Open| High | Low    | Name (Symbol)	    | Div   | Vol   | Yld	| P/E	| Close/Day Last | Net Chg |
| -- | ---- | ------ | -------------------- | ----- | ----- | ----- | ----- | -------------- | ------- |
|20  |21.50 | 8.00	 | SkyHighCorp (SHC)	|       | 3143  |       | 76	| 21.25	         | +.25    |
|43  |47.00 | 31.75	 | LowDownInc (LDI)	    | 2.35  | 2735	| 5.7	| 18	| 41.00	         | –.50    |
|20  |25.00 | 21.00	 | ValueNowInc (VNI)	| 1.00	| 1894	| 4.5	| 12	| 22.00	         | +.10    |
|82  |83.00 | 33.00	 | DoinBadlyCorp (DBC)	|       | 7601  |		|	    | 33.50	         |–.75     |

To properly read stocks, you must first understand what each column in the stock chart means:
* **Open:** The first price of the beginning of the day.
* **High:** This column gives you the highest price that particular stock has reached in the most recent period.
* **Low:** This column gives you the lowest price that particular stock has reached in the most recent period.
* **Close:** The last price before the end of the day.
* **Name (symbol):** This column tells you the company name (usually abbreviated) and the stock symbol assigned to it. Financial tables list stocks in alphabetical order by symbol, and you need to use them in all stock communications.
* **Dividend:** A value in this column indicates that payments have been made to stockholders. The amount you see is the annual dividend quoted as if you owned one share of that stock.
* **Volume:** This column tells you how many shares of that particular stock were traded that day. If only 100 shares are traded in a day, the trading volume is 100.
* **Yield:** This column refers to what percentage that particular dividend is to the stock price. Yield, which is most important to income investors, is calculated by dividing the annual dividend by the current stock price.
* **P/E(Price/Earnings):** This column indicates the ratio between the price of the stock and the company’s earnings. This ratio (also called the earnings multiple or just multiple) is frequently used to determine whether a stock is a good value.
* **Day last:** This column tells you how trading ended for a particular stock on the day represented by the table. Some newspapers report the high and low for that day in addition to the stock’s ending price.
* **Net change:** This column answers the question “How did the stock price end today compared with its trading price at the end of the prior trading day?

### There are three main parts to a candlestick:
<a href="url"><img src="https://github.com/RocqJones/financial-stock-market-app/blob/master/imgs/CandlestickBasicsChart.png" height="400" width="400" ></a>

* Upper Shadow: The vertical line between the high of the day and the close (bullish candle) or open (bearish candle) 
* Real Body: The difference between the open and close; colored portion of the candlestick 
* Lower Shadow: The vertical line between the low of the day and the open (bullish candle) or close (bearish candle)
[Read more here](https://commodity.com/technical-analysis/candlestick-basics/)
