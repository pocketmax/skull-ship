### cleanup VAERS dataset
* figure out how to fetch dataset automatically
  - host on github in a dataset repo
* drop records with incomplete fields
* identify people who took covid vaccines
* parse pre-existing conditions

### COVID dataset for infection prediction
* location (zip/city/state)
* age
* gender
* blood type
* ethnicity
* vaccine taken by maker
* med conditions (MED_*)
  ...
* infected count

### COVID dataset for deadly prediction
* location (zip/city/state)
* age
* gender
* blood type
* ethnicity
* med conditions
  ...
* symptoms (SYM_)
  ...
* death count

### try to fix this h5 bug
https://colab.research.google.com/drive/1WFGjA6qiCaZHRz6Ty8ssmjJYzOXx-5rK?usp=sharing

## Audio Emotion Recognition

## get used to playing with TF models

### code review this (ASK QUESTIONS!)
https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_object_detection.ipynb#scrollTo=zl3qdtR1OvM_
* reproduce in a different file
* strip out extra stuff
* use a different image
* update terms list

### questions
* what is a "model"?
### transfer learning
training an existing model on new data thats relative to the original data. i.e. training a model about cars with truck data.
reduces training time and data requirements

* deploy a model to TF hub like github?
* use tf hub models directly?
* what is "mobilenet"?
* R-CNN?
* Resnet v2?
* COCO 2017 dataset?
* dilated convolutions
* imagenet
* dictionary
* a way to submit a patch to a model in tfhub?
* 

### upload that handwritting model to tf hub (ASK QUESTIONS!)
* add demo support
* upload different formats of the model

### run models in python
* find a few model repo sites
  tfhub.dev
  
### example TF hub models
https://tfhub.dev/tensorflow/faster_rcnn/inception_resnet_v2_640x640/1
https://tfhub.dev/google/aiy/vision/classifier/food_V1/1
https://tfhub.dev/agripredict/disease-classification/1


### run models in different model formats
### run models in 
## make models...
### go through that list of types of ML trainings and make plain english versions of them

### things to help get started on an ML project
* make a list of possible domains to do a project on
    * how susceptible you are to getting COVID?
        - age
        - race
        - city/state
        - pre-existing health conditions
        - vaccinated / pharma comp
    * as an infected person, how susceptible are you are to dying from COVID
    * How much money will my house be worth at a future date
    * given an image, is Nicholas Cage in it
    * given 2 selected teams, which one will win?
    * Based on their current stats, given 2 pokemon, which one will win in a battle?

* define the problem
  
* prepare the data
* train model
* improve results
  <img alt="" src="https://i.imgur.com/hyTiHIH.png">

### generate an image from random data using tf.random.normal
### extract each color channel from an image into 3 separate images of each channel
### make a really lower resolution image
### make an image with the same resolution but with bigger pixels so it appears to look low res
### make a few convolutions that show the points of interest like edges

### SVD & PCA: These are methods used in machine learning for data projection, data reduction, and feature selection type tasks

### research Conv2D layer
layers that extract summarized data from previous features to detect things like edges
<img src="https://i.imgur.com/whph8fN.png" alt="">

### what are receptive fields?
### diff between max pooling and pooling
* max pooling takes the max val in the kernel
* pooling is just the general term

### diff between convolution and pooling
NEED HELP ON THIS ONE
* pooling layer doesn't learn anything, it just runs a calculation from the input data
<img alt="" src="https://i.imgur.com/pk3nccI.png">

### research GlobalAveragePooling2D layer

### when does the tensor shape get checked by the layers?
when fitting i.e. training

### pooling
progressively reduce the spatial size of the represented data
* increases speed at the expense of input quality
* max pooling uses biggest pixel in the kernel
* min pooling uses smallest pixel in the kernel
* avg pooling uses an avg of the pixels in the kernel
<img alt="" src="https://i.imgur.com/mVpKSgr.png">

# TINY TASKS

### diff between evaluate() and predict()
evaluate() returns prediction and computes metrics
predict() returns prediction

### kernel

### make changes to image classifier
* reduce epochs
* reduce layers
* only use some of the images
* refactor model building to not be a function
* Add a third class to the pets datasets
 1. grab a bunch of images
 1. rename them to match the others
 1. put them somewhere public in a zip with the name of the pet in a sub dir

### Activation layer
* examples using different configs
### Rescaling layer
* adjusts the values in the tensor to something else
* doesn't change the shape of the tensor
* examples using different configs
* rescale a given image
### RandomFlip layer
* examples using different configs
* flip a given image
### RandomRotation layer
* examples using different configs
* rotate a given image
### BatchNormalization layer
way too hard to understand. Expert level!
* examples using different configs

### Conv2D layer
* examples using different configs
### SeparableConv2D layer
* examples using different configs
### MaxPooling2D layer
* progressivly reduce spatial size of data
* generates lower resolution summary of original tensor
* expects 3d tensor
* examples using different configs

### reduce layers in NN and see how it affects the final result

## what does tf.expand_dims do? why have it's own method for such a simple basic task
https://www.tensorflow.org/api_docs/python/tf/expand_dims

## what does adding a "batch dimension" to a tensor do?

### Diagram of a NN with code examples
* Weights
* Layers
* Neurons
* Input Layer

### Diagram states of NN along with code examples
* Defined
* Compiled
* Trained
* inferred

Depict an epoch, batch, etc etc

### modify an image
* resize smaller
* convert to grayscale
* rotate it
* flip it

# QUESTIONS

### when training, under each epoch is a num/num counter i.e. 140/170 ... what is that?
### what does freezing a model mean?

### What is transfer learning?
Freezing the bottom layers in a model and only training the top layers


### what is the output shape given the current model?
```python
model = keras.Sequential()
model.add(keras.Input(shape=(250, 250, 3)))  # 250x250 RGB images
model.add(layers.Conv2D(32, 5, strides=2, activation="relu"))
model.add(layers.Conv2D(32, 3, activation="relu"))
model.add(layers.MaxPooling2D(3))
model.summary()
```

### What are the demonstratable differences between Functional and Sequential models? They both look like a stack of layers that transforms data as it passes through
### `The Functional API also makes it easy to build models that have multiple inputs`? I thought all models have multiple inputs since each input is a feature i.e. each pixel is an input

### when can you run model.summary()?
after weights are added by either building the model or after the model sees input data for the first time

### what is the shape of a layers inputs?
### when are a layers weights created?
when it's first called on an input

### a quick way of generating data to pass into a model for training?

### when should you __not__ use a sequential model?
    * Your model has multiple inputs or multiple outputs
    * Any of your layers has multiple inputs or multiple outputs
    * You need to do layer sharing
    * You want non-linear topology (e.g. a residual connection, a multi-branch model)


### what is a 'plain stack of layers'? All layers have 1 input tensor and 1 output tensor
### what is cifar10 data?
### Is there a diff between an Input layer and the inputs of a model?
The Inputs layer defines the shape of the inputs into the model. Can also be added to the first layer with input_dim=1 as an arg
## Based by the model structure, can you determine...
### if it's functional or sequential?
### what type of NN it is?
### What is a sigmoid neuron?
A perceptron that outputs a value between 0 and 1 instead of a 0 or 1


## General

1. **What branch of math does someone have to know to do machine learning? i.e. algebra, calculus**
1. **What is a good online source for learning ML for a beginner?**
1. **Any difference between training tensorflow model locally or in cloud besides performance?**
   From what I can tell, training locally involves a lot of complicated setup and messing with hardware.
1. **Are there any examples problems you can give that tensor cores take advantage of that GPU cores don’t?**
   There aren't. Tensor cores are just a better way of doing what GPUs can do
1. **What are some of the common mistakes people make when trying to learn ML?**
1. **What is the general difference between machine learning and deep learning?**
1. **Can the tensorflowjs lib support local GPUs for acceleration if it’s ran server side with node?**
   Yes
1. **If tensorflowjs is run client side via a browser, is it possible to prevent someone from downloading the data model?**
   No
1. What are some use cases for AI?
1. What are some use cases to not use AI?

# STATEMENTS



# CONCEPTS

## Structure of a model

### Example model structures
<img alt="" src="https://i.imgur.com/p4LtPqM.png">
<img alt="" src="https://i.imgur.com/4hNiFiu.png">
<img alt="" src="https://i.imgur.com/PM0Pakd.png">
<img alt="" src="https://i.imgur.com/EIyin91.png">

### a neuron
### a weight
### transfer learning
### bias

### a perceptron
Takes multiple inputs and produces 1 binary output.
The output is determined if the total sum of all the inputs is greater than a threshold value



### Dense Layer vs Convolutional Layer
### Exploration vs Exploitation
### Supervised vs Unsupervised Learning
The data has Labels. Only used in classification
### Deep Learning vs Machine Learning
### why standardize the data?
specific coeficients will be penalized more than others

### Vectorized & Standardized data
Source data

# TERMS

### same term & another term
this is the description of the term. **this** is a reference to a dependant term
* this is a question about the term
  * this is a sub question
* this is another question about the term? `this is an answer to the question`

### Causal Inference
### Inference
Querying a model with unknown data for a result i.e. executing

### Dropout
turns off random neurons
* reduces over fitting
* increased accuracy without adding more samples

### Batch normalization
normalizes inputs to the next layer

### training a network
finding the best set of weights to map inputs to outputs in our dataset.

### Optimizer
* Search through different weights for the network and any optional metrics we would like to collect and report during training

### Dense Layer
### Zero-Mean
### Unit-Variance
### Recurrent Layer
### regularization
### eager execution
code you write is the code thats executed instead of the built in functions. Model trains slower
`model.compile(optimizer='adam', loss='mse', run_eagerly=True)`
### Feature Map

### Hyperparameters
### gradient boosting


### Features
data points used to train a model. Like number of bedrooms for a mortgage model or the pixels for an image
### Variable Length Features
### One Hot Encoding
### nonlinearities (activation functions)
### Fold Functions
### Ridge Functions
### Radial Functions
### binary cross entropy
### Loss Function - Error Function
evaluates a set of weights

### Random Forest
Uses many trees, and it makes a prediction by averaging the predictions of each component tree
### Decision Trees
### Binary Classification
### standardize data
### Gradient Decent
### Normal Distribution - bell curve
### Machine Learning
uses algorithms to parse data, learn from that data, and make informed decisions based on what it has learned
### Neural Networks
### DFFNN - Deep Feed Forward Neural Networks
### DRNN - Deep Recurrent Neural Networks
### Supervised Machine Learning
* classification: organizing labeled data
* regression: predicting trends using previous label data
### Deep Learning - Deep Structured Learning - Hierarchical Learning
subset of machine learning and structures algorithms in layers to create an “artificial neural network” that can learn and make intelligent decisions on its own
### Monotonic Function

### Iterations

### Epoch
when an entire dataset is passed forward and backward through the NN only once

### Batch Size
Total number of training examples present in a single batch

### Number of Batches - sets - parts
divided parts of a dataset

### async preprocessing
preprocess data on CPU for the next batch while the current batch is being trained on the GPU

### predicting a model
returns predictions of an array of datasets

### GAN training loop

### Compiling the model
* have to specify an optimizer and a loss function
* uses efficient numerical libs under the hood i.e. theano or tensorflow


### performance metrics
classification accuracy, precision, recall, AUC, etc.

### Checkpointing
saving your training progress at regular intervals
```callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath='path/to/my/model_{epoch}',
        save_freq='epoch')
]
model.fit(dataset, epochs=2, callbacks=callbacks)
```

### evaluate a model
returns loss and accuracy of a dataset on model

### Binary Functions
### Sigmoid Binary Function
### Skip Connections
### n-gram
### out-of-vocabulary token
### multi-hot - TF-IDF
### Binary Cross Entropy
### Unsupervised Learning
* uses unlabeled data
* we know little to no info about the data
* finds useful data in unknown data
* fewer tests
* fewer models
* less controllable outcome since algorithms are being created for you
* clustering: finding patterns and groupings from unlabeled data
### rmsprop optimizer
### Accuracy Metrics
### LR - Linear Regression
### Fit Generator Function
### bootstrap sampling generator
* alternative to shuffling
### Embedding Layer
maps categories to vector of weights
### NN - Neural Network
### CNN - Convolution Neural Network
### GAN - Generative Adversarial Network
### ANN - Artificial Neural Network
### RNN - Recurrent neural Networks
### FNN - Feedforward Neural Networks
### TDNN - Time Delay Neural Network
### LR - Linear Regression
### MVR - Multi-variant Regression
* LR but with multiple variables
### ordinal categorical variables
### non-ordinal categorical variables
### high cardinality categorical variable
a lot of categories like a zipcode
### GlobalMax - AveragePool
### Global Context
### SST
### SSE
### SSR
### Slope
### Correlation
### Intercept
### R-Squared
### SE - Standard Error



* uses labeled data
testing
## learning types

### Semi-Supervised
* large amount of unlabeled data
* small amount of labeled data
### Assumption types
* continuity assumption
* cluster assumption
* manifold assumption



CNN -
### supervised

### self-training - self-learning - self-labeling

### situated AI
### computational intelligence
### statistical AI
### natural language processing: read and understand human language


### sub-symbolic reasoning
indirect knowledge derived from experience i.e. an expert artist that knows a statue is fake at first glance

### automated reasoning
### automated theorem proving
### automated proof checking

### Bias-Variance Tradeoff
Exploration/exploitation
Bayesian models
Instance based learning
Association learning

Zero-shot algorithm
GANs
Few-shot learning
Self-supervised techniques

MAE: Mean absolute error

Validation data: data to evaluate a models predictions that it hasn’t seen before

LR app dependency notes
Slope: ??
Correlation: ??
Intercept
* Depends on slope
  R-Squared: ???
  Standard Error: ???
  SST
  SSE
  SSR
  yHat
  yBar
  xBar


# RESOURCES

## online books
a little too math heavy but totally something to read
http://neuralnetworksanddeeplearning.com/

great for developers learning AI
https://www.fast.ai/

## user groups
https://groups.google.com/forum/#!forum/keras-users
https://discuss.tensorflow.org/
https://kerasteam.slack.com/
Use this link to join slack-> https://keras-slack-autojoin.herokuapp.com/

## YouTube Playlists

## YouTube Videos

## Tutorial Pages

https://www.digitaltrends.com/cool-tech/deep-learning-vs-machine-learning-explained/2/
https://www.zendesk.com/blog/machine-learning-and-deep-learning/

## Tutorial docs
EXPERT LEVEL!!!
https://distill.pub/2019/computing-receptive-fields/

hello world!
http://keras.dhpit.com/


https://keras.io/getting_started/intro_to_keras_for_researchers/
https://keras.io/getting_started/ecosystem/
https://keras.io/getting_started/faq/
https://keras.io/guides/functional_api/
https://keras.io/guides/sequential_model/
https://keras.io/guides/making_new_layers_and_models_via_subclassing/
https://keras.io/guides/training_with_built_in_methods/
https://keras.io/guides/customizing_what_happens_in_fit/
https://keras.io/guides/writing_a_training_loop_from_scratch/
https://keras.io/guides/serialization_and_saving/
https://keras.io/guides/writing_your_own_callbacks/
https://keras.io/guides/preprocessing_layers/
https://keras.io/guides/working_with_rnns/
https://keras.io/guides/understanding_masking_and_padding/
https://keras.io/guides/distributed_training/
https://keras.io/guides/transfer_learning/
https://keras.io/guides/training_keras_models_on_cloud/
https://keras.io/guides/keras_tuner/
https://keras.io/examples/

http://neuralnetworksanddeeplearning.com/chap1.html

### NN diagram
https://github.com/HarisIqbal88/PlotNeuralNet

## Datasets

### cats and dogs
https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip

### pima diabetes
https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv