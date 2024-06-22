https://autokeras.com/tutorial/image_classification/
https://autokeras.com/tutorial/image_regression/


https://autokeras.com/tutorial/text_regression/
regression vs classification
regression is whats the temperature tomorrow
classification is will it be hot or cold tomorrow


https://autokeras.com/tutorial/text_classification/

# Summary Sentence
Classifies sentimient in text to be either positive or negative

# TODO: coding tasks
* make model without auto-tuner
* replace sklearn.datasets.load_files with tf.keras.utils.text_dataset_from_directory
* identify/drop records that are too small i.e. text under 10 chars
  - done after cleaning




* make a nodebook for training a simple perceptrion
  - https://www.simplilearn.com/tutorials/deep-learning-tutorial/perceptron

* make binary classifier with only matching dataset and compare results
* identify/clean data for...
  - clutter chars not from humans i.e. html tags from bad screen scrape etc etc
    - list vals with non-alphanum chars
    - count of records affected
    - pct of total records affected
  - duplicate records/expected dependant vals i.e. same text / same y val (run first)
  - duplicate record/mismatched val i.e. same text / different y val (run second)
* append more training data
  - should be hotlinkable to reduce manual setup before run
* do prediction from text field in notebook and return results to page
* identify model auto tuner decided on and use that to speed up training time



# BDD statement
I want to categories unlabeled bodies of text based on general sentament in the text and not specific patterns of characters in text


# 'You Are Here' Map
(highlight what area of the tech this tutorial covers in a general graph of all the tech)
NLP -> (SA) Symantic Analasis -> Text Classifier -> multi-class classifier

# Pre observation notes about the tutorial
* the dataset is already labeled
* gives a more complex example
* includes colab example

# Pre-QnA: ask before tutorial, answer after tutorial
* why split data in X and Y when it should be train and test?
  - The X and Y thing is pretty much everywhere and I know it has to do with graphs but it would make everything a lot easier for beginners if they wouldn't include it
  - It's x is for dependant values. y is for independant values. train is for the x/y datasets that the model trains on (x for learning, y for testing). test is for testing the model after it's trained
* What is a trial and what does it have to do with training?
  - A trial is a different model it trains the data on
* is a trial a keras only thing?
  - It's a wrapper for the keras auto tuner. 
  - a way to try different model configs and pick the best one
* is it a binary classifier or a normal classifier?
* do trials in parallel?

# Post-QnA: ask/answer after tutorial
* one hot encoding labels
* model.predict? 
  - infer predictions on a trained model.
```python
model.predict(np.array(["my input data"]))
```
* what are blocks, nodes and edges
* model.fit?
  - actually trains the model
* model.evaluate?
  - returns loss and metrics values for model
* can module.evaluate return more info about the model?
* model.compile?
  - configures the model. sets up the NN and all the weights etc etc. auto keras does this on model init
* diff between training for just bad reviews vs training for bad/good reviews?
* What is the relationship between NLP, text classification, sentiment analysis, algorithms (logistic reg, k-nearest neighbor, decision trees) and all the classification models i.e. binary, multi-class, multi-label, imbalanced
https://machinelearningmastery.com/types-of-classification-in-machine-learning/
* relation between steps, batches, epochs and trials?


* Natural language processing
  * sentiment analysis
    * text classification
    * image classification

* AI
  * machine learning
    * deep learning
      * reinforcement learning
        * decision making
          * Q-learning
          * R learning
          * TD learning
      * unsupervised learning
        * clustering
          * k-means clustering
          * mean-shift clustering
          * DBSCAN clustering
          * agglomerative hierachical clustering
          * gaussian mixture
          * NN
      * supervised learning
        * regression
          * linear regression
          * neural network regression
          * support vector regression
          * decision tree regression
          * lasso regression
          * ridge regression
          * NN
        * classification
          * naive bayes classifier
          * decision trees
          * support vector machines
          * random forest
          * k - nearest neighbors
          * NN

# Ideas
* find or make diagram that shows the diff parts of split testing X/Y train/test
* make a benchmark chart about predict results showing match/mismatched results
  - group text blocks in some logical way. i.e. easy/medium/hard.  short/med
* write custom text to predic from
* an easy way to host a model on a site???
  - shows info about the model
  - tracks model versions
* easy way to hot link datasets to notebooks to reduce manual setup

```python
clf.predict(np.array([
    "that movie sucked. it didn't have enough special effects", #0
    "that movie was the best. I loved the acting", #1
    "it wasn't that good. i hated it totally. I liked some parts but I didn't like the rest", #0
    "it was a crappy movie by far. it was terrible" #0
]))
```

# secondary learning: extra stuff to study based on the article
* sentiment analysis
* different classification types


# Terms
* inference
* one hot encoder
* search space
* x = training dataset
* y = testing dataset
* steps: total number of batches of samples before declaring the prediction round finished
* epoch: An iteration over the entire train and test datasets
* batch size: Number of samples per gradient update. 
* gradient update: ?
* evaluation round: ?
* evaluate
* fit: train the model on the train and test datasets
* predict: make a prediction on a trained model
* trials: the different models it creates to train from
* accuracy
* loss
deterministic vs probabilistic model classes
 - ...




https://www.educba.com/keras-binary-classification/
https://blog.purestorage.com/purely-informational/deep-learning-vs-neural-networks/
https://www.frontiersin.org/articles/10.3389/fninf.2021.748370/full

# binary encodings
* Floating number
* Vector of integers
* One hot encoding

# activation functions
* Sigmoid of logistic activation functions
* Softmax function

# loss funcs for class tasks
* Binary cross entropy
* Sparse categorical cross entropy
* Categorical cross entropy

# classifications
Binary classification
Multi label classification
Multi class classification

# TODO: coding tasks
* use a hotlinked dataset for training data
* find better way of stabalizing model input shape
* split data using something else
* reduce use of non-keras libs if possible
* train on only 1 class

# TODO: learning tasks
* np.reshape() - np-reshape.ipynb
 - use examples from this tutorial and the other one
 - some advanced examples
 - use case examples if possible
 - negative numbers
 - all vals have to fit in new array
 
* tf.keras.metics.Accuracy() - keras-metrics-accuracy.ipynb
 - use examples 
* a breakdown of model anatomy - modelexample.ipynb
  - understand "metrics"
  - make the smallest model to train data on with the smallest dataset to show a result
  - how is "total params" calculated
  - what is "trainable parms"
  - what is "non-trainable params"
  - re-create common issues
    - input shape error
    - ...
  - understand input shape for model and how to fix mis-shape issues i.e..
    -  y_train = np.asarray([1,0]).astype('float32').reshape((-1,1))
  - understand model.summary()
  - make a model based on trials output from other tutorial
* sklearn.model_selection.train_test_split - train_test_split.ipynb

# 'You Are Here' Map
NLP -> (SA) Symantic Analasis -> Text Classifier -> binary classifier

# Pre observation notes about the tutorial
* uses more libs then what I'm comfortable with. Would be nice if it only used keras
* no link to complete tutorial so I can do a test to see if it works
* no link to dataset
* references things outside of the tutorial like other classifiers
* the example output looks like the code and the example code looks very simplistic

# Pre-QnA: ask before tutorial, answer after tutorial
* has errors

# Post-QnA: ask/answer after tutorial

# Ideas

# secondary learning: extra stuff to study based on the article

# Terms
