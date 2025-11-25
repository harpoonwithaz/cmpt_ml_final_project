# CMPT 120 Machine Learning Final Project

Our task is to create 4 different machine learning models using the Scikit-Learn package in python.
This project was made using visual studio code. To test this project in the way it was intended, run each file using VSCODE's builtin terminal.

**Python Version:**
3.13.3
**Scikit Learn version:**
1.7.2

## Installation

Recommended for full compatibility

```bash
pip install -U scikit-learn
```

## Part 1: Building our first machine learning model

Linear regression model to predict the coefficients based on 2d array of 3 random integers from 0 to 1000.

### model.py

`create_inputs()`:
Creates a 2d array of 100 lists of 3 random integers from 0 to 1000.
Returns a list of lists containing integers used as training input.

`create_outputs()`:
Creates a list of 100 integers by summing each integer in a list multiplied by the weights given.
Returns a list of integers used as training output.

**Model:**
Using the scikit learn linear regression model, we use the *fit* function to train the model. We use the training input as the training data for the model. The training output is used as the target values for the model.

**Prediction:**
We use the *predict* function from scikit learn to predict the outcome based on a test array of 3 random integers. We print out the coefficients from the prediction to see if it matches the weights we used to create the outputs.

## Part 2

Predicts the amount of bikes rented in an hour.
File used: `SeoulBikeData.csv`

### data_processing.py

File that 

## Part 3

## Part 4

### data_processing.py

**create_training_set()**:
This function handles the creation of the training set from the data in the csv file
