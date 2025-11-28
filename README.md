# CMPT 120 Machine Learning Final Project

Our task is to create 4 different machine learning models using the Scikit-Learn package in python.
This project was built using visual studio code. To test this project in the way it was intended, run each file using VSCODE's builtin terminal.

**Python Version:**
`3.13.3`
**Scikit Learn Version:**
`1.7.2`

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

## Part 2: Building a Model Using Real Data

Linear regression model to predict the count of bikes rented in an hour based on metric using real bike sharing data for the city Seoul from 2017-2018.
File used: `SeoulBikeData.csv` from [UC Irvine](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand)

### data_processing.py

File that 

## Part 3

We predicted the curricular units 2nd sem (grade) (index 31)

In the data processing file we excluded indexes:
29 (2nd sem evaluations)
    - because you would only know how many exams they took after the semester is over
30 (2nd sem approved)
    - because it tells the model the success/failure result, giving away the grade
31 (2nd sem grade)
    - because this is the answer key
32 (2nd sem without evaluations)
    - because this reveals the number of classes skipped or failed after the semester ends
36 (Target - Future status)
    - because this leaks the future, whether they eventually graduate or dropout, after the 2nd semester grades are recorded
  
Reference: Original Dataset Columns:
0. Marital status
1. Application mode
2. Application order
3. Course
4. Daytime/evening attendance
5. Previous qualification
6. Previous qualification (grade)
7. Nationality
8. Mother's qualification
9. Father's qualification
10. Mother's occupation
11. Father's occupation
12. Admission grade
13. Displaced
14. Educational special needs
15. Debtor
16. Tuition fees up to date
17. Gender
18. Scholarship holder
19. Age at enrollment
20. International
21. Curricular units 1st sem (credited)
22. Curricular units 1st sem (enrolled)
23. Curricular units 1st sem (evaluations)
24. Curricular units 1st sem (approved)
25. Curricular units 1st sem (grade)
26. Curricular units 1st sem (without evaluations)
27. Curricular units 2nd sem (credited)
28. Curricular units 2nd sem (enrolled)
29. Curricular units 2nd sem (evaluations)
30. Curricular units 2nd sem (approved)
31. Curricular units 2nd sem (grade)
32. Curricular units 2nd sem (without evaluations)
33. Unemployment rate
34. Inflation rate
35. GDP
36. Target (shows if graduated, enrolled, or dropout)

### studentPerformance.csv

### data_processing.py

Helper module to collect the data from the csv file and process it to a format we can use in our linear regression model.

### model_performance.py

### model.py

## Part 4

### data_processing.py

**create_training_set()**:
This function handles the creation of the training set from the data in the csv file
