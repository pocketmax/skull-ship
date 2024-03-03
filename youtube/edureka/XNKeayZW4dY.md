https://www.youtube.com/watch?v=XNKeayZW4dY

## Sequential Model
* Linear stack of layers
* Useful for building simple models
*   simple classification network
*   Encoder - decoder models
* The model we all know and love!
* treat each layer as object that feeds into the next

```python
import keras
from keras import layers
model = keras.Sequential()
model.add(layers.Dense(20, activation='relu', input_shape=(10,)))
model.add(layers.Dense(20, activation='relu'))
model.add(layers.Dense(20, activation='softmax'))
model.fit(x, y, epochs=10, batch_size=32)
```

## Functional Model
* Like playing with lego bricks
* Good for 95% of use cases

```python
import keras
from keras import layers
inputs = keras.Input(shape=(10,))
x = layers.Dense(20, activation='relu')(x)
x = layers.Dense(20, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)

model = keras.Model(inputs, outputs)
model.fit(x, y, epochs=10, batch_size=32)
```

### Domain Adaption
* Train on domain A and test on domain B
results in poor performance on test set
*

### Two types of execution

Deferred (symbolic)
* python to build a computation graph first
* compiled graph then gets executed later

Eager (imperative)
* python runtime is the execution runtime
* similar to execution with numpy

* symbolic tensors don't have a value in the python code (yet)
* Eager tensors have a value in the python code
* with eager execution, value-dependent dynamic topologies (tree-RNNs) can be used

## implementing a neural network

1. Prep Input
   * preparing the input and specify the input dimensions (size)
   * images, videos, tet and audio

2. define the AAN Model
   * define the model architecture and build the computational graph
   * Sequential or Functional style
   * MLP, CNN, RNN

3. Optimizers
   * Specify the optimizer and configure the learning process
   * SGD, RMSprop, Adam

4. Loss Function
   * Specify the input, outputs of the computational graph (model) and the loss function
   * MSE, Cross Entropy, Hinge
5. Train and Evaluate Model
   * Train the model based on the training data
   * Test the model on the dataset with the testing data

## Use case - problem statement

`Predicting the price of wine with the Keras Functional API and TF`

Building a wide and deep network using Keras to predict the price of wine from its description

* This problem is well suited for wide & deep learning
* it involves text input and there isn't any correlation between a wine's description and it's price


ANN: artificial neural network
MLP
CSS
RNN

SGD
RMSprop
Adam
MSE
Cross Entropy
Hinge

