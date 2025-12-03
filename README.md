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
File used: `studentPerformance.csv` from [UC Irvine](https://archive.ics.uci.edu/dataset/320/student+performance).

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

**Features:**

- **Color-Coded Error Visualization:** Bar graph uses a gradient from green (excellent predictions, 0-10% error) through yellow (moderate errors, 30-50%) to red (poor predictions, 90-100%+ error)
- **Accuracy Threshold Analysis:** Automatically calculates what percentage of predictions fall within 10%, 20%, and 30% error ranges
- **Mean Error Estimation:** Computes a weighted average error across all predictions to give an overall performance score
- **Prediction Bias Detection:** Identifies whether the model tends to over-predict or under-predict values
- **Detailed Statistical Summary:** Shows average and maximum prediction errors in both directions
- **Visual Console Output:** Includes ASCII bar charts for quick at-a-glance performance assessment
- **Handles Edge Cases:** Automatically skips predictions where actual values are zero (to avoid division errors)

---

**calculate_accuracy_metrics()**:
Calculates comprehensive accuracy statistics from the error percentage distribution.

**Args:**
- `percentages` (dict): Dictionary mapping error ranges to prediction counts

**Returns:**
- Dictionary containing total predictions, accuracy at various thresholds (10%, 20%, 30%), and estimated mean error percentage

**print_performance_summary()**
Displays a formatted summary of model performance in the console with visual elements.

**Args:**
- `percentages` (dict): Error percentage distribution
- `metrics` (dict): Pre-calculated accuracy metrics

**Outputs:**
- Total number of predictions analyzed
- Estimated mean error percentage
- Number and percentage of predictions within each accuracy threshold
- Clean, formatted table with separators for easy reading

**compare_prediction_ranges()**:
Analyzes the directional accuracy of predictions by comparing predicted values to actual values.

**Args:**
- `actual_values` (list): Ground truth values from test set
- `predicted_values` (list): Model's predicted values

**Returns:**
- Dictionary containing counts of over-predictions, under-predictions, and exact matches, plus average and maximum error amounts in each direction

---

**print_prediction_bias()**:
Displays analysis of whether the model systematically over-predicts or under-predicts values.

**Args:**
- `comparison` (dict): Statistics from `compare_prediction_ranges()`
- `total` (int): Total number of predictions

**Outputs:**
- Breakdown of over-predictions vs under-predictions with percentages
- Average amount by which predictions are off in each direction
- Maximum error encountered in each direction
- Warning message if model shows significant bias (>10% difference)
- Confirmation message if predictions are balanced

**graph_error_side_by_side()**:
Creates a turtle graphics bar chart and cumulative line graph with dynamic color coding based on error severity.

**Color Scheme:**
- **0-10% error:** Bright green (0, 255, 0) — Excellent predictions
- **10-30% error:** Green to yellow gradient — Good predictions
- **30-50% error:** Yellow (255, 255, 0) — Acceptable predictions
- **50-70% error:** Orange tones — Concerning predictions
- **70-90% error:** Orange-red — Poor predictions
- **90-100% error:** Red — Very poor predictions
- **100%+ error:** Bright red (255, 0, 0) — Worst predictions

The gradient smoothly transitions through the color spectrum, making it immediately obvious which error ranges contain the most predictions. Green bars indicate success, while red bars highlight areas where the model struggles.

## Part 4: Interactive Model Building

This part creates an interactive linear regression model that allows users to provide their own CSV file and dynamically select which columns to use for training and prediction. The program guides users through file selection, column selection, and displays model performance visually.

**Features:**

- Automatically detects CSV files in the `data/` directory
- Allows user to select which column to predict (output)
- Allows user to select multiple input columns for the model
- Automatically detects the CSV separator (comma, semicolon, etc.)
- Validates that selected columns contain numeric data
- Partitions data into 80% training and 20% testing sets
- Trains a linear regression model using scikit-learn
- Calculates and visualizes prediction error percentages
- Allows the user to run multiple models without restarting

**create_training_set()**:
Creates a training set from CSV data by reading the specified file and extracting columns at the given indexes.

Args:

- `file_location` (str): Path to the CSV file
- `output_index` (int): Index of the column to predict
- `input_indexes` (list[int]): Indexes of columns to use as features
- `sep` (str): CSV separator character (auto-detected, default: ",")

Returns:

- Tuple containing input data (2D list) and output data (list)

**train_test_partition()**:
Splits data into 80% training and 20% testing sets.

Args:

- `data` (list): The data to partition

Returns:

- Tuple containing training data and testing data

**validate_user_input()**:
Validates numeric input from the user within specified constraints.

Args:

- `prompt` (str): Message to display to user
- `min` (int): Minimum allowed value
- `max` (int): Maximum allowed value
- `breakout_condition` (str): Optional string to allow user to exit (default: "")

Returns:

- Integer value entered by user, or -1 if breakout condition is met

**Model Performance:**
Performance is calculated using the same error percentage method as Part 2 and 3, comparing actual values to predicted values. Results are visualized using a bar graph showing the distribution of prediction error percentages.
