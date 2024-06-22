https://robjhyndman.com/uwafiles/fpp-notes.pdf
https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Bootstrapping[1].pdf
https://cloud.r-project.org/web/packages/forecast/forecast.pdf
https://dokumen.pub/qdownload/forecasting-principles-and-practice-2e.html
https://www.forecastr.co/blog/time-series-forecasting-model
https://www.geeksforgeeks.org/multivariate-time-series-forecasting-with-grus/

Univariate Forecast vs multivariate forcast
Multivariate Time Series Models
non-stationary data
Static Forecasts vs. Dynamic Forecasts

https://medium.com/analytics-vidhya/time-series-forecasting-a-complete-guide-d963142da33f


# Linear regression
## KWs
* dependent variable: what changes in response to the independed variable
* independent variable: what you change
* outlier
* mean line
* data points
* line of best fit
* scatter plot
* R2
* residual = e^ or u^
* slope
y(b) = mean of all y values
y(h) = b0 + b1x
x(b)
# QnA
best fit line vs trend line
decomposition?
recomposition?
noise?
linear regression? What makes it a linear regression?

# types
metric: Measurements gathered at regular time intervals
event: Measurements gathered at irregular time intervals

# types
- Qualitative forcasting
  * results depend on expert opinions
  * chance for bias since humans are involved
- Quantitative forcasting
  * data comes from patterns
  * no humans involved so no bias

https://www.timescale.com/blog/what-is-time-series-forecasting/
https://medium.com/analytics-vidhya/time-series-forecasting-a-complete-guide-d963142da33f

https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tvTYtytPt9AK0HuZQ3u8HA.png
* orig TS data
* trend component
* sesonality component
* Noise or residue

* level: baseline of a timeseries
* trend: if the TS increased or decreases over time
* seasonality: patterns that repeat over a peiod of time
* cyclicity: pattern that repeats aperiodically. Doesn't repeat after fixed interval
* noise: after everything is extracted, whats left is random fluxuations in data

"decomposing a timeseries"
additive seasonal decomposition: components of TS add up to original series
multiplicative seasonal decomposition: components have to be multipled to make TS
* using one type over the other should have residue that doesn't have any pattern

RMSE: Root Mean Squared Error: Root of MSE. How forcasted values differ from actual values

MAPE: Mean Absolute Percentage Error: Measures how accurate forcast sys is. accuracy as a percentage. 

Granularity rule: the more aggregate your forcasts, the more accurate your predictions. aggregated data has lesser variance hence, lesser noise

Frequency rule: update data frequently in order to capture any new info. Forcasts will be more accurate

Horizon rule: avoid making predictions too much into the future. Too much into the future will give less accurate foracasts



# data quality
- complete
- not duplicated or redundant
- collected in a timely and consistent manner,
- in a standard and valid format
- accurate for what it is measuring
- is uniform across sets

# types of time series forcasting models
- Exponential smoothing
- Moving average
- Autoregressive moving average
- Autoregression
- ARIMA

- Deep learning models
- Linear model
- SARIMA
- Seasonal decomposition

SARIMAX: Seasonal Autoregressive Integrated Moving Average + exogenous variables

# timeseries moving average (MA)
https://otexts.com/fpp2/moving-averages.html

# ARMA
# AR (Autoregressive)
# I (Integrated)
# MA (Moving Average)
# ARIMA: Autoregressive Integrated Moving Average

p = 5: lags for autoregression (AR)
d = 1: 1st order differencing (I)
q = 0: No moving average term (MA)
https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
https://machinelearningmastery.com/grid-search-arima-hyperparameters-with-python/


coefficients integral
coefficients
integral