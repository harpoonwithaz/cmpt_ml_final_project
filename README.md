**4 DIFFERENT ZIP FILES FOR EACH PART**

# CMPT 120 Machine Learning Final Project

Our task is to create 4 different machine learning models using the Scikit-Learn package in python.
This project was built using visual studio code. To test this project in the way it was intended, run each file using VSCODE's builtin terminal.
Each part of this project has their respective folder containing all the files. To test the model for each part, run the `model.py` file in the subsequent folder.

## How to run program

To correctly run our programs, we recommend using VSCODE's built in terminal. If you want to run it from IDLE or Mac Terminal or Windows Command prompt, make sure to CD to the folder containing the .py before executing the `model.py` script. Then, in the execution statement, specify python and the file you want to execute

### Example

Windows command prompt:

```batch
cd C:\Users\{your file directory}\{folder containing model.py file}
python3 model.py
```

## Environment dependency versions

**Python Version:**
`3.13.3`
**Scikit Learn Version:**
`1.7.2`

## Installation

Required to run our models.

```bash
pip install -U scikit-learn
```

## Part 1: Building our first machine learning model

Linear regression model to predict a numeric value based on 2d array of 3 random integers from 0 to 1000.

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
File used: `SeoulBikeData.csv` from [UC Irvine](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand).
Obtains data from `SeoulBikeData.csv` and removes the features we don't need and converts features containing a string to floats to further improve model performance. We then partition the input and output date in to 80% for training and 20% for testing to see accuracy.
Model performance is calculated by subtracting the actual value by the predicting value, then divided by the actual value to get the error percentage for how accurate the predictions were. We then visualize the performance by creating a bar graph of how many predictions were in a certain error percentage range using pythons built in turtle module.

In the data processing file we excluded index:

- 0 (date) - too difficult to process into a value ML model can train on
- 1 (rented bike count) - this is what we are predicting
- 13 (functioning date) - we are removing the rows when it isn't a functioning date anyways so we don't need this column

Reference: Original Dataset Columns:

1. Rented Bike Count
2. Hour
3. Temperature (Degrees Celsius)
4. Humidity (%)
5. Wind speed (m/s)
6. Visibility (10m)
7. Dew point temperature (Degrees Celsius)
8. Solar Radiation (MJ/m2)
9. Rainfall (mm)
10. Snowfall (cm)
11. Seasons (str)
12. Holiday (No Holiday/Holiday)
13. Functioning day (Yes/No)

## Part 3: Building Another Model for Different Data

We predicted the curricular units 2nd sem (grade) (index 31)

In the data processing file we excluded indexes:

- 29 (2nd sem evaluations) - because you would only know how many exams they took after the semester is over
- 30 (2nd sem approved) - because it tells the model the success/failure result, giving away the grade
- 31 (2nd sem grade)- because this is the answer key
- 32 (2nd sem without evaluations) - because this reveals the number of classes skipped or failed after the semester ends
- 36 (Target - Future status) - because this leaks the future, whether they eventually graduate or dropout, after the 2nd semester grades are recorded

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

## Part 4

### data_processing.py

**create_training_set()**:
This function handles the creation of the training set from the data in the csv file
