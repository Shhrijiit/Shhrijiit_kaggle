# Digit Recognizer Using CNN

* Importing All Necessary Libraries

* Loading the Train & Test Dataset from Kaggle

* Checking for Null and Duplicate Values

## Data Visualization:

  i. Using a pie chart to visualize the percentage distribution of handwritten digits
 ii. Using a bar graph to display the count distribution of handwritten digits
iii. Visualizing a specific digit using its pixel features
 iv. Analyzing the pixel intensity of a particular digit with a bar graph

## Data Preprocessing

  i. Splitting Data into X and y:
 ii. Normalizing the data
iii. Splitting the data into TrainTestSplit with 20% reserved for validation.

## CNN Model Building:
### Model 1 with Tanh as Activation Function

  i. The model uses 3 convolution layers with input size 28x28. Each layer has 32, 64, and 64 neurons with padding respectively.
 ii. The activation function applied is tanh to detect non-linear patterns in the data with l2 regularization with 0.02 penalty.
iii. MaxPooling2D with a pool size of 2x2 is applied.
 iv. Batch normalization has been added after each layer.
  v. After the convolutional layers, a Flatten layer is used to convert the multidimensional output into a one-dimensional vector.
 vi. A fully connected dense layer with 128 nodes and the relu activation function is added and a dropout layer with rate 0.2 is added after
vii. As there are 10 classes, the final output layer has 10 nodes for classification using the softmax function for multiclass classification.

### Model Compilation:

The model is compiled using the Adam optimizer, categorical_crossentropy loss function, and accuracy as the evaluation metric.

### Training the Model:

The model was trained for 15 epochs with a batch size of 32.
Training Dataset Results:
Accuracy: 0.97
Categorical Crossentropy Loss: 0.1673
Validation Dataset Results:
Accuracy: 0.96
Categorical Crossentropy Loss: 0.2121


### Model 2 with Relu as Activation Function

The model was retrained for 15 epochs with a batch size of 64.
Training Dataset Results:
Accuracy: 0.9843
Categorical Crossentropy Loss: 0.1218
Validation Dataset Results:
Accuracy: 0.9810
Categorical Crossentropy Loss: 0.1358


## Final Results:
```
1. Final validation accuracy: 0.9843
2. Final categorical crossentropy loss: 0.9810
```
