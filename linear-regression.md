linear regression

y = B* x + A

Math bar symbol aka macron
The mean of a set of numbers

https://mathworld.wolfram.com/Bar.html

* Determines the relationship between 2 sets of data points if any. There could be cases where there is no relationship
* the practice of statistically calculating a straight line that demonstrated a relationship between two different items
* Only capable of capturing linear relationships
* Only capable of handling relationships between two variables
* If more than 2 variables, use multiple regression instead
* Assumes a direct correlation between two variables that can be represented by a straight line


Use cases
Mouse weight to mouse size
Tricker treaters to local school enrollment
Height to weight
How much to loan someone based on credit score

YT PlayList
https://www.youtube.com/playlist?list=PL14Xm0gTaoI1OjlGzI5J9O7nBG3KwpgKY

Links
https://www.investopedia.com/terms/l/least-squares-method.asp
https://365datascience.com/tutorials/statistics-tutorials/sum-squares/
http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm
http://www.stat.yale.edu/Courses/1997-98/101/correl.htm
https://blog.minitab.com/en/adventures-in-statistics-2/regression-analysis-how-to-interpret-the-constant-y-intercept
https://www.tensorflow.org/tutorials/keras/regression

Terms
Slope: How much Y will change as X changes
* The units of the Y var per units of the X var
* Rise over Run
  <img alt="my image" src="https://i.imgur.com/zvgSSC7.png" />
  ￼

Y axis:
* Explanatory variable
  X axis:
* Dependent variable

Classifier for two groups of data with with 2 Vals
Perceptron Algorithm

X (hat): avg of all the x values
ŷ (y hat): prediction of Y for a given value of X
* A spot on the dotted line i.e.

Y-Intercept: how high the line hits the Y axis
ȳ (y bar):
R²: a way of testing the model (SSR / SST)
* How well the regression line predicts values
* Also known as the coefficient of determination
* Ranges from 0 to 1. Greater is better
* r² = 1 — SSE / TSS
* TSS = Sum(y_i — mean(y))²
* SSE = sum((Actual — Prediction)²)

Coefficient: the number in front of a variable. If just a variable, then it’s 1
Dependent variable (Y): Side axis, can change
* Assumes it’s a direct result of the independent variable
  Independent variable (X): Bottom axis, doesn’t change
* Can behave however it likes and doesn’t depend on the other variable
  Negative relationship: Line tilts backward
  Positive relationship: Line tilts forward
  Correlation: Strength of relationship between the two data sets

Square Error: Calculates how off a prediction is.
* Error = (Actual — Prediction)²
  Observations: data points
  Regression Line: a.k.a. ŷ
  TSS (total sum of squares)
  ESS (explained sum of squares)
  RSS (residual sum of squares)
  SSR (sum of squares due to regression)
  SSE (sum of squares due to error)
  SEE (standard error of the estimate)
  SST (sum of squares total) SSR + SSE
  TE (total errors)
  TES (total errors squared)
  MSE (mean squared error)
* TES / Row count
  LSM (Least Squared Method)
  LSS (Least Squared Solution)
  MLE (Maximum Likelihood Estimation)
  GLM (General Linear Model)
  KNN (K-Nearest-Neighbours)
  SVM (Support Vector Machines)
  Estimated Value
  Error
  Actual Value: data point


QnA
1. What does the “Linear” part mean?
2. What does the “regression” part mean?
3. What use cases does this satisfy?
4. What use cases does it not satisfy?
5. How do you know your model is right?
6. What is the diff between this and logistic regression?

Practice
Make a linear regression in excel
Make a linear regression in JS as a showcase app

<img alt="" src="https://i.imgur.com/Rt4icnJ.png">
