# OVERALL FOCUS
1. accurately forcast future stock activity
2. figure out most profitable response to prediction
3. generate orders based on response

www.moomoo.com
finviz.com

https://dzone.com/articles/improve-mariadb-performance-using-query-profiling


# STOCK PROJECT
https://staragile.com/blog/time-series-forecasting
https://www.influxdata.com/time-series-forecasting-methods/
https://medium.com/@yennhi95zz/a-guide-to-time-series-models-in-machine-learning-usage-pros-and-cons-ac590a75e8b3
https://www.toppr.com/guides/fundamentals-of-business-mathematics-and-statistics/time-series-analysis/models-of-time-series-analysis/
https://neptune.ai/blog/select-model-for-time-series-prediction-task
https://www.cybrosys.com/blog/what-are-the-different-types-of-time-series-forecasting-methods
https://www.tableau.com/learn/articles/time-series-analysis
https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/
https://vitalflux.com/different-types-of-time-series-forecasting-models/
https://towardsdatascience.com/an-overview-of-time-series-forecasting-models-a2fa7a358fcb
https://www.sciencedirect.com/topics/neuroscience/time-series-model

# Indicators
AD: Accumulation Distribution
ADX: Average directional index
ADX: Average Directional Index
AO: Aroon Oscillator
ATR: Average True Range
ATRB: Average True Range Bands
ATRTS: Average True Range Trailing Stops
BB: Bollinger Bands
BBA: Bollinger Bandwidth
BPB: Bollinger Percentage B
CCI: Commodity Channel Index
CCI: Commodity channel index
CE: Chandelier Exits
CI: Choppiness Index
CIB: Comparisons on Indigo for Browser
CIN: Coppock Indicator
CMF: Chaikin Money Flow
CMO: Chande Momentum Oscillator
CO: Chaikin Oscillator
CPCSC: Compare Prices on Classic Stock Charts
CV: Chaikin Volatility
DMA: Displaced Moving Average
EM: Ease of Movement
EMA: Exoponential moving average
EMA: Exponential Moving Average
ERI: Elder Ray Index
FI: Force Index
FRE: Fibonacci Retracements & Extensions
HA: Heikin Ashi
HMA: Hull Moving Average
IC: Ichimoku Cloud
KC: Keltner Channels
KST: KST Indicator
LRI: Linear Regression Indicator
MA: Moving average
MA: Moving Averages
MA: Oscillator
MACDH: MACD Histogram
MACDPPO: MACD Percentage Price Oscillator
MACD: Moving average convergence Divergence 
MACDPPO: Percentage Price Oscillator
MAS: Moving Average Systems
MFI: Money Flow Index
MI: Mass Index
MI: Momentum Indicator
MMA: Multiple Moving Averages
MP: Median Price
NVI: Negative Volume Index
OBV: On Balance Volume
OBV: On-balance volume
PB: Percentage Bands
PC: Price Comparison (Classic Stock Charts)
PD: Price Differential
PE: Price Envelope
PP: Pivot Points
PR: Price Ratio
PSAR: Parabolic SAR
PTS: Percentage Trailing Stops
PVI: Positive Volume Index
PVT: Price Volume Trend
R3DMA: Rainbow 3D MA
RCP: Rate of Change (Price)
RCV: Rate of Change (Volume)
RSC: Relative Strength (Compare) - Classic Stock Charts Only
RSI: Relative Strength Index
RSI: Relative strength index
SD: Standard deviation
SDC: Standard Deviation Channels
SI: Stochastic oscillator
SMA: Simple moving average
SNA: Simple Moving Average
SO: Stochastic Oscillator
SO: Stochastic Oscillator
SROC: Smoothed Rate of Change
SRSI: Stochastic RSI
ST: Slow Stochastic
SZ: Safezone
TL: Trendlines
TMA: Three Moving Averages
TMA: Two Moving Averages
TMF: Twiggs ® Money Flow
TMO: Twiggs ® Momentum Oscillator
TP: Typical Price
TR: True Range
TRIX: TRIX
TSI: True strength index
TSM: Twiggs ® Smoothed Momentum
TTI: Twiggs ® Trend Index
TTI: Twiggs® Trend Index
TV: Twiggs ® Volatility
UO: Ultimate Oscillator
V: Volatility
V: Volume
VHF: Vertical Horizontal Filter
VO: Volume Oscillator
VR: Volatility Ratio
VS: Volatility Stops
VWAP: Volume weighted average price
WAD: Williams Accumulate Distribute
WAD: Williams Accumulation Distribution
WC: Weighted Close
WMA: Weighted Moving Average
WPR: Williams Percent R
WWMA: Wilder Moving Average


Required time horizon of predictions
Forecast update frequency
Forecast temporal frequency: 


Timeseries models based on Exponential smoothing model
* SES: Single exponential smoothing
* DES: double exponential smoothing
* Triple exponential smoothing model (holt-winter method)

Purpose of time series forecasting
* quantity of data thats accessible
* duration of forecasts time horizon
* forecast modification frequency
* forecast temporal frequency


  * train model on previous trades
  * confirm polygon.io TS are right
  * stock suggestions from polititions
    - API fetch
    
  * DONE a way to get missing date ranges for symbols

  * generate forcast data (AI training)

Need to have uniform time slices i.e. the same amount of entries per day
* query that only selects rows between a certain span of time per day

After model is trained, how to evaluate accuracy
* forcast next few records


fetch latest ticks
- from now to oldest
    yahoo api: limit 30 days
fetch older data
- from oldest tick to past
    polygon api: limit 120 days

* how to track recommendations and how accurate they are
  - who made the recommendation
  - buy or sell
  - price
  - date when they said to make the action
  - accuracy: after the fact, find out how accurate they were in a score


* activity for one or more stocks on a particular day but not others
* find last captured date for a stock month and see if 
* why do some days have a lot of records while others don't
* check to make sure there are no records during weekends or holidays
  - find out when market is closed

find gaps between dates for each stock accounting for weekends and holidays
* for a month, get stock and min/max dates of that month

* query that shows days under 390 ticks
SELECT sym,DATE_FORMAT(recorded_at,'%Y-%m-%d'),COUNT(*) AS ticks FROM activity_min GROUP BY sym,DATE_FORMAT(recorded_at,'%Y-%m-%d') HAVING ticks < 390;

* query that selects syms with no activity data
* query that selects syms with incomplete months
mysqldump -uroot -ppass -h127.0.0.1 --column-statistics=0 --databases stocks 

* make routine that runs daily to capture yesturday activity across all stocks (no run on weekends)
* make routine that runs to fill missing data


``` month report - missing days between last recorded day and end of month
SELECT sym,DATE_FORMAT(MAX(recorded_at),'%Y-%m') AS lastpoint,LAST_DAY(recorded_at) AS lastday,DATEDIFF(LAST_DAY(recorded_at),MAX(recorded_at)) AS missing_days FROM activity_min WHERE sym='CDZI' GROUP BY sym,DATE_FORMAT(recorded_at,'%Y-%m') HAVING missing_days>0;
```
```
SELECT sym,COUNT(*) AS total FROM activity_min GROUP BY sym HAVING total<5000 ORDER BY total DESC LIMIT 1000;
```
```
SELECT sym,MIN(recorded_at) AS MIN,MAX(recorded_at) AS MAX,LAST_DAY(recorded_at) AS LAST, DATEDIFF(LAST_DAY(recorded_at),MAX(recorded_at)) AS DIFF FROM activity_min GROUP BY sym,DATE_FORMAT(recorded_at,'%Y-%m') HAVING DIFF>0 ORDER BY DIFF;
```

# EXCLUSIONARY RULES: excluse a stock from being a potential candidate
* apply to recent data points only
* a way to show stocks that were rejected and for what reason(s)
- not moving very much
- price gradually falling not due to any major events
- 
# INCLUSIVE RULES: includes a stock as a potential candidate
- 

# KEYWORDS
ACF: Autocorrelation function
PACF: Partial autocorrelation function
ADF test: augmented dicky fuller test

ARIMA (auto reggresive integrated moving average)
EXP Smoothing (more weight to recent vals, less weight to older vals)
# PHASES


find data (find sym and date ranges)
collect data (api calls)

save data
* save to dir
docs/activity-sym-from-to.json

## COLLECT DATA
* populate most recent data to oldest data
* detect discrepencies in data batween sources i.e. two sources shows different values for a PIT
* detect missing data sorted by most recent
* populate by recent to oldest
* batch script
  - gets list of markets and recent date ranges of missing data
* source worker (pops from queue)
  * from date
  * to date
  * market
* figure out how to work around data source fetch limits
## RATE LIMITS

https://api.nasdaq.com/api/quote/MSFT/historical?assetclass=stocks&fromdate=2014-01-10&limit=9&todate=2024-01-10&random=8
https://api.nasdaq.com/api/quote/watchlist?symbol=meta%7cstocks&symbol=lulu%7cstocks&symbol=tsla%7cstocks&type=Rv
https://api.nasdaq.com/api/quote/META/summary?assetclass=stocks
https://api.nasdaq.com/api/market-info
https://api.nasdaq.com/api/quote/META/info?assetclass=stocks
https://api.nasdaq.com/api/quote/META/chart?assetclass=stocks

* polygon.io
  - 5 in 60 seconds
* yahoo
  https://query1.finance.yahoo.com/v7/finance/download/NVDA?period1=1682035200&period2=1713657600&interval=1d&events=history&includeAdjustedClose=true
  https://yahooquery.dpguthrie.com/
* finnhub.io
  - free doesn't have quote info and pay is way too expensive
* marketstack.com
  - 100 in 1 month
* alphavantage.co
  25 per 86400
* iexcloud.io
  - trial is 7 days
* twelvedata.com
  - free has limit stocks
  - pay starts at $80
  - 800 in 86400
* nasdaq: 
  - annon: 20 calls per 10 minutes and 50 calls per day
  50 in 86400
  20 in 600
  - authed: 300 calls per 10 seconds, 2,000 calls per 10 minutes, and 50,000 calls per day
  50000 in 86400 seconds
  2000 in 1440 seconds
  300 in 10 seconds

* scraper scheduler
  - deploys schedulers
  - knows limits of scrapper sources i.e. x markets per day
* market scraper
  - source
  - stock
  - date range
  - sql dump to table
* market list scraper
  - source
  - sql dump to table
* local up to date copy of all markets
  - get list of all stocks for a market
* collect outside suggestions i.e. stock x is a good suggestion by source A and B
  - source
  - recommended stock
  - date
* data tables
  - markets
    + market
  - history
    + date
    + close
    + volume
    + open
    + high
    + low
  - suggestion
    + source
    + date
    + market
    + score

# QUERY DATA
  * run a prediction strategy against all stocks
    - returns suggested purchase order params
    - predictions table
      + market
      + model (name of prediction model used)
      + buy date
      + buy price
      + sell date
      + sell price
      + stocks
      + from history date
      + to history date
# TRAINING
  * anomoly detection
    - a model that looks for anomolies that might screw up training model
  * timeseries forcasting
  * schema for how to capture forcast data
    - activity_min table columns
    - model desc column
    - model ID column
  * files
    - {SYM}-{FROMDATE}-{TODATE}-training.csv: rows from db to train/test from
    - {SYM}-{FROMDATE}-{TODATE}-test.csv: next set of rows from db to compare predictions to
    - {SYM}-{FROMDATE}-{TODATE}-{model}-predictions.csv: data predicted from model with overlapping dates
  * timeseries classification
  * as models get slower to train, look for training providers to speed it up

# MODEL
  https://www.tensorflow.org/tutorials/structured_data/time_series
  * reduce overal accuracy of model to a score
  * capture config of model in some way
  * after training, pass a date range to generate predictions   
  https://keras.io/examples/timeseries/
  * keywords
    - balanced binary classification
    - standard deviation
    - multivariate
    - sparse categorical crossentropy
    - permutation
    - validation accuracy
    - training accuracy

# REPORT DATA
  * import etrade orders in table

# WORKERS
  * one worker per api source
  * pulls requests from queue and appends results to another queue
    - --api-src=<tag> --api-key=<hash> --in-queue=<String> --out-queue=<String> --broker=<Url> 
  * scripts
    - updatesymbols: fetch big file, upsert stocks table
    - activity: grabs trades summery grouped by minute
    - gen-api-requsts: generates and appends api requests for missing data across all symbols starting with recent first
      + 
      --from-date=<Date> --to-date=<Date> 
      --table=<String> --db=<String> --rdbms=<url> 
      --broker=<Url> --out-queue=<String>
# QUEUES
  * api_requests
  * api_responses
  * api_errors
# SCHEMAS
```json
{ // activity_request
  "data": {
    "symbol": "APPL",
    "fromDate": "mm-dd-yyyy hh:mm:00AM",
    "toDate": "mm-dd-yyyy hh:mm:00PM",
    "interval": "min",  // min,hour,day,week,month
    "limit": 10 // limit results set
  },  
  "type": "activity",
  "retries": 10,  // how many times to retry
  "ttl": 400 // time to wait
}
```
```json
{ // activity_request_fail
  "request": {...},
  "error": {
    "api": "string", // NYSE, yahoo, etc etc
    "status": 12312, // status code of error response
    "response": "string" // payload of error response
  }
}
```



# DB TABLES
```sql
CREATE DATABASE IF NOT EXISTS stocks;

USE stocks;
DROP TABLE IF EXISTS activity_min;

CREATE TABLE IF NOT EXISTS activity_min (
    sym CHAR(5) NOT NULL,
    recorded_at DATETIME NOT NULL,
    open FLOAT(7,2) UNSIGNED NOT NULL,
    high FLOAT(7,2) UNSIGNED NOT NULL,
    low FLOAT(7,2) UNSIGNED NOT NULL,
    close FLOAT(7,2) UNSIGNED NOT NULL,
    volume MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (sym,recorded_at)
);
// activity_hour
// activity_day
// activity_month
// activity_year

DROP TABLE IF EXISTS forcast_min;
CREATE TABLE IF NOT EXISTS forcast_min (
    model_id INT UNSIGNED NOT NULL,
    symbol CHAR(5) NOT NULL,
    recorded_at DATETIME NOT NULL,
    open FLOAT(7,2) UNSIGNED NOT NULL,
    high FLOAT(7,2) UNSIGNED NOT NULL,
    low FLOAT(7,2) UNSIGNED NOT NULL,
    close FLOAT(7,2) UNSIGNED NOT NULL,
    volume MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (model,sym,recorded_at),
    FOREIGN KEY (model_id)
        REFERENCES models(id)
        ON DELETE CASCADE
);
// forcast_hour
// forcast_day
// forcast_month
// forcast_year

CREATE TABLE IF NOT EXISTS activity_min (
    sym CHAR(5) NOT NULL,
    recorded_at DATETIME NOT NULL,
    open FLOAT(7,2) UNSIGNED NOT NULL,
    high FLOAT(7,2) UNSIGNED NOT NULL,
    low FLOAT(7,2) UNSIGNED NOT NULL,
    close FLOAT(7,2) UNSIGNED NOT NULL,
    volume MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (sym,recorded_at)
);


DROP TABLE IF EXISTS models;
CREATE TABLE IF NOT EXISTS models (
    info VARCHAR(255) NOT NULL,
    id INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);

Symbol|Security Name|Market Category|Test Issue|Financial Status|Round Lot Size|ETF|NextShares
AACG|ATA Creativity Global - American Depositary Shares, each representing two common shares|G|N|N|100|N|N
CREATE TABLE IF NOT EXISTS symbols (
    sym CHAR(5) NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (sym)
);


```

orders: where orders are stored
  * columns: broker, order ID, market, term, status, type, ...
forcasts-markets-daily: where models dump predictions of each stock
  * indicates how accurate the prediction was for that day
markets-daily: projection table where data is inserted from source tables
  * goes in source priority
{src}-markets-daily
  * columns: market, date, open, close, high, low, volume
suggested-order
  * columns: buy price, sell price, peak price, sell date
# MODELS
* define models to apply to each market to forcast changes
* define why a market didn't meet the models criteria



https://keras.io/api/datasets/mnist/
https://keras.io/api/datasets/cifar10/

# ML courses
2h https://www.coursera.org/learn/machine-learning-overview $80 7 day free trial
## 3 categories of Unsupervised learning problems
1. Clustering problems: find inherient groupings in data
2. association problems
Association rule learning: id new and interesting patterns in data
3. Dimensionality reduction problems: reducing the num of vars present in the dataset
feature selection vs feature extraction
## reinforcement learning: solving sequential decision-making problems
## supervised learning problems
* X vars: features, predictors or attributes
* Y vars: targets, responses or labels
learn a model that will approximate the func relationship f, between the input variables x and the output variables y
## When is SL useful?
* where there is no human expert
* where humans can perform task but can't describe it i.e. object detection in images
* where the desired func changes freq
* where each user needs custom func
Approximate the unknown func F that relates input X to output Y given a dataset D
function approximiation
empirical loss function

Components of supervised learning
Evaluation
  - MSE
Optimization
Representation
Parametric method
Non-parametric method
Stocastic gradient decent

6h https://www.coursera.org/learn/machine-learning-introduction-for-everyone
6h https://www.coursera.org/learn/introduction-to-ai
12h https://www.coursera.org/learn/introduction-to-machine-learning-with-python
15h https://www.coursera.org/learn/machine-learning-under-the-hood
19h https://www.coursera.org/learn/uol-machine-learning-for-all
32h https://www.coursera.org/learn/advanced-learning-algorithms
32h https://www.coursera.org/learn/machine-learning


https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-predict-new-samples-with-your-keras-model.md

* understand this
`inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values`

https://www.youtube.com/watch?v=Wgu8ggtAr80
https://www.youtube.com/watch?v=OryO301RmX8
`inputs = inputs.reshape(-1,1)`
`inputs = sc.transform(inputs)`

`dataset_train = pd.read_csv(url)`
`training_set = dataset_train.iloc[:, 1:2].values`

python array slicing
https://www.w3schools.com/python/numpy/numpy_array_slicing.asp

np.reshape won't make lopsided shapes
turn this...
[0,0,0,1,1,1,2,2,2]
into this...
[[0,0,0],
[1,1,1],
[2,2,2]]
turn 12 el array into 2D array
turn 2D array into 3D array
rotate cube 180 degrees
set values to all values in one demention

understand what .shape looks like

make a shape for a 10x10 image with RGB values for each pixel
add an alpha channel field for each pixel
https://i.stack.imgur.com/p2PGi.png
https://www.w3resource.com/w3r_images/n-dimension-array.png
https://www.plus2net.com/python/images/np-dimensions.jpg

* find where shape of training data and shape of predict input
* make a hello world example
* can minmaxer be swapped
* learn reshape
* understand diff between these
x -
y |
X train:
X test:
Y train:
Y test:

https://www.youtube.com/watch?v=kGdbPnMCdOg
https://www.youtube.com/watch?v=nS1J-2uoKto
https://www.youtube.com/watch?v=8uC-WT1LYnU
https://www.youtube.com/watch?v=q_HS4s1L8UI
https://www.youtube.com/watch?v=gDqbnDK1-lM
https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-predict-new-samples-with-your-keras-model.md
https://www.w3schools.com/python/numpy/numpy_array_slicing.asp

https://www.w3schools.com/python/numpy/trypython.asp?filename=demo_numpy_array_slicing_2d
```python
import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5,6,7,8,9])
arr = arr.reshape(3,3)
print(arr)
print(arr.shape)

arr1 = np.array([0,0,0,0,0,0,0,0,0])
arr1 = arr1.reshape(3,3)
print(arr1)
print(arr1.shape)

arr2 = np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2])
print(len(arr2))
arr2 = arr2.reshape(3,3,3)
print(arr2)
print(arr2.shape)


arr2 = np.random.rand(10*10*3)
arr2 = arr2.reshape(10,10,3)
print(arr2)
print(arr2.shape)
print(arr2.dtype)
```

# TODO - stock open price predictions
* fail on missing rows i.e. a missing date (days between top row date and bottom row date != row count)
* if dataset is in wrong sort order, flip it
* save/load model to disk (will speed up dev process)
  - use saved model instead of training a new one if exists
* predict stock price x days into the future
  - find a way to output next x predictions

# TODO - support rest of fields (new file)
* adding rest of fields to prediction including volume
* convert chart to candlestick
  - see if candlestick chart can support multiple datasets with different markings

# TODO - group prediction comparisons
* score accuracy between each prediction and source training set
* determine which of the models to use based on that score
* generate excel of predictions (for manual testing)
  - each models prodictions on a seperate sheet
  - first sheet empty for real stock values
  - formulas for how off the prediction is for each day

# TODO - research how to generate stock analytics datapoints - in:stock data out:datapoints
* trend i.e. bull/bear market
* momentum
* volitility

# Stock data points
* strength
* Close: EMA
* Consolidation

# trade types
high frequency trading: zillions of trades per min
day trading: small quick trades through out the day
long trading: medium trades for a few days
swing trading: big trades that last for weeks

# What to optimize for buy/sell?
* stock prediction accuracy
* making a minimum amount per day?
* reduce risk

# third party suggestions for candidate symbol
* API support
* accuracy score: based on accuracy of previous predictions

# common mistakes: list of universal common mistakes to avoid across all trading strategies
* mistake must be defined and testable
* mistake must be universal across any strategy
* used for picking a stock to buy or sell

# webull questions
1. API query limit?
2. copy of all stock changes?
3. any major diff between paper trading and the market?
4. can taxes be taken out automaticly?

# what to learn
* how to refine stock market predictions

# trade types
* limit order
* market order
* stop limit
* stop order
* stop loss: if the price goes below it, sell

trailing stop-loss

# what to calc in forcast data
* target sell price: price to sell at within forcast window
* bail price: lowest price to sell at incase failure to sell at a profit. optimized to reduce loss at much as possible
* quantity: based on probability of stock hitting forcasted sell price. i.e. if stock reaches best price, whats the optimul quantity that will attract sell quickly. to start, this is set to 1
* exit date: when order is expected to complete
## assumptions
* sale orders settle quickly

## if failed to sell within window determine if...
* a new order with adjusted values would work
* leave as is
* 
* probability of selling at X price 
* keep forcasting and find next opportunity to sell at and start over

# how to collect market data for free
* DO script that scales out several droplets that fetch a batch of symbol datasets from multiple sources and downloads to one target
* a docker image for each source. 
* args for all sources: symbol, date range, stocks or trades, sum type (day/mon/year)

# S3 object nameing convention
SYMBOL = market
INTERVAL = m,h,d,w,mo,y summary of each row
RANGE = FROM DATE - TO DATE 03/12/23
SRC = (YAH)yahoo finance, (NAS)nasdaq, (used to predict data schema)
SYMBOL-INTERVAL-RANGE-SRC.csv

# how to train on market data
* docker image for each AI training type and use args for customizing
* extended args for output target i.e. local csv, screen or S3
# how to prevent downloading duplicate data
* check for random duplicate rows in target data

# training docker image
* args
  - src dir for files
  - trg dir to dump projections
  - model dir (build model if not found)
  - gpu (/proc/dev) path to gpu to leverage for model build performance

# Stock status buckets
* trending up
* trending down
* trending neutral

How to resolve these accronyms
* RNN: Recurrent Neural Network
  - LSTM: child of 
* RNN: Rotating Name Number
  

# AI TERMS
* naive forecast random walk
* min max scaling
* RNN vs DNN vs CNN
* LSTM is a subset of RNN
* Pearson correlation coefficient
* Gradient vanishing
* exploding gradient

RSI relative strength index
moving avg
Exponential moving avg
stop hunting

# formations
flag
pennant
cup with handle
ascending triangle
symetrical triangle
measured move up
ascending scallop
3 rising valleys
continuation pattern
rising wedge
falling wedge
flag pattern
head and shoulder
reverse head and shoulder
double bottom

# stategies
* cut the fat: find and ignore stuff to not trade/train on for each strategy
* candidate stocks to find
* model popular strategies and write AIs to detect and trade with them
* formation pattern detection
* long term dividen optomizing
* 

technical analysis vs fundimental analysis

# General stock Questions
* can stock prices change in relation to other stock prices?
* do stock prices change in relation to it's self? yes and candle stick patterns are an example
* are formations natural in all trend data or market specific?
* Why do some big companies deal in sub second trading?
* Can I buy a stock via one broker and sell it via another?
* Can a buy order be fufilled with multiple orders? i.e. 10 stocks purchased across 5 orders of 2 stocks a peice?
* Can stocks be traded across multiple exchanges?
* a way to see pending public buy or sell orders?
* determine stock demand and if someone will buy it
* risk of affecting price from buying or selling too many stocks
* what is a hedge fund?
* signs of a good broker?
* to short a stock, would the broker have to find some to bet against me that the stock would go down
* who calculates the price of a stock? is there a formula?
* is it harder to get a seller for a buy order with a big quantity
* what are pre-market trades? https://www.nasdaq.com/market-activity/stocks/aapl/pre-market-trades

# etrade questions
1. can I bulk import orders - yes
2. can I make an order that sets buy/sell limits with no expiration? No. only good until 60 days or good until date
3. can taxes automaticly be taken out or calcuated?
4. limit on $ of orders to submit
5. penalties or fees on unfufilled orders
6. competing trades? i.e. buy limit order at $10 at 40 units and another one at $20 at 20 units and if one execs, cancel the other
7. can a buy orders include sell conditions i.e. buy at one price and limit sell at another price

limit order = limit I will pay
spread = price between bid and ask prices
stop limit on quote = 
# etrade stuff
* order type
  - market order: I want to buy/sell a stock now no matter what the price
  - limit: I want to buy/sell the stock but I want to limit how much I'm willing to pay/sell it for
  - buy stop loss: highest price to buy stock at
  - sell stop loss: lowest price to sell at
  - buy stop limit: waiting for price to go up at one price, then goes down, then buy at that price
  - sell stop limit: I want to sell my stock if it dips below one price and then limit sell at another price
  - sell short
  - buy to cover
  - contingent order
* price type
  - Last price
  - Bid Price: what buyer is willing to buy for
  - Ask Price: what seller is willing to sell for
* price limit
  - market: what ever the price is at that time
  - limit
  - stop on quote
  - stop limit on quote: price of stock to sell at
  - trailing stop: stop loss line moves up as price goes up. But doesn't move down
  - trailing stop $: $ under current price
  - trailing stop %: % under current price
* limit price
* term / duration
  - GFD - good for day
  - GTC - good until canceled (60 days max): order is canceled after 60 days if not executed
  - GTD - good until date: order is canceled if not executed after specified date
  - fill or kill: order has to be exec in it's entierty or not at all
  - immediate or cancel
  - extended hours (good for day)
  - extended hours (immediate or cancel)

# data questions
1. how to compare prediction accuracy of multiple datasets



# array visualizer
https://stackoverflow.com/questions/23916976/python-array-visualizer-for-debugging

# AI videos
https://www.youtube.com/watch?v=F2DR4FGy0LY

https://tradinglab.ai/
https://polygon.io/
https://www.investopedia.com/simulator/

# AI training articles
https://medium.com/@zahmed333/stock-price-prediction-with-keras-df87b05e5906
https://towardsdatascience.com/predicting-stock-prices-using-a-keras-lstm-model-4225457f0233

python and jupyter notebook support
https://code.visualstudio.com/docs/languages/python

# api call to get a stocks history
https://api.nasdaq.com/api/quote/MSFT/historical?assetclass=stocks&fromdate=2014-01-10&limit=9999&todate=2024-01-10&random=8

https://dataondemand.nasdaq.com/docs/index.html

# list of nasdaq symbols
https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt


# processes
## data capture/forcasting
* stock filter: go through all stocks and determin which ones are candidates for trades
* stock forcaster: generates activity forcasts of a stock
  - can use multiple ways of forcasting stocks but picks one with best fit
* buy demand forcaster: data point timeseries
* sell demand forcaster: data point timeseries
* strategies: applies specific trading strategy to a stocks timeseries.
 - one for each type of trading strategy
 - determines success score if applied
* strength forcaster: data point timeseries
* Momentum forcaster: data point timeseries
* Volatility forcaster: data point timeseries

# theories
* use quantity in buy order to indicate confidence in stock turning a profit

# things to try
* use bigger dataset
* use higher resolution dataset i.e. activity per hour instead of day
* send generated predictions to stock analysis

## buy decision making
* pick what to buy (buy order at market price)
  - order ID (populated from broker)
  - created date
  - active date
  - stock symbol
  - quantity
  - market price (current price)
  - sell lower limit (lowest price to sell at)
  - buy limit (future price to sell at. not used by broker)
* mistake avoidance check: scrub potential future buys that are common mistakes
* exec buy orders: send buy orders to broker via API

# variables to figure out
min buy price
min sell price
trailing sell price $/% 

## stock monitoring
* When stocks price is >= desired price, submit market order

# support
* forums
* trader consultants
* stock simulators
* give sample forcasts to traders and get their optinions

# goals
1. forcast a stocks potential for going up and going down
2. estimate when to sell to maximize profit while reducing risk
 - vars: date, price, shares, risk

# timeseries goals after stock picked
1. optimize for best time / price to sell at

# possible gotchas
* too emotional
* puting in too much money
* buying what I personally like
* selling out of fear and not plan

# phase 1 - hello world
1. get tutorial working
2. use real data
3. compare prediction to market at different points in time
4. see how far in the future I can go before accuracy dips
5. tweak training over time to get higher accuracy for future forcasting

# phase 2 - manual order entry
1. make buy order for 3 suggested stocks
2. set quantity to 1
3. make sell orders for 60 days at small profit margin

# phase 3 - generate order CSV file and import into etrade
1. generate CSV file same 3 stocks
2. manually upload CSV file to etrade

# phase 4 - automate fetching symbol list
1. API call to get current list of symbols for an exchange
2. loop through list
3. fetch historical data for each

# phase 5 - automate fetching a symbols history
1. fetch symbol with different sources yahoo, nasdaq, etc etc
2. dump to csv file
3. custom output columns in csv 

# phase 6 - automate training
1. loop through each symbol
2. train a model for each symbol

# phase 4 - automate predictions
1. loop through each data model
2. generate predictions for next x days
3. collect in csv

# phase 6 - reduce extra values
1. loop through each row in csv
2. remove rows that aren't candidates
3. save csv



https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/6009dd9fa7bc363aa822d2c7/1611259312432/ISLR%2BSeventh%2BPrinting.pdf