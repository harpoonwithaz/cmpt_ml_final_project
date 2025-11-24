import pandas as pd
from sklearn.linear_model import LinearRegression
import os
import re

# Local module imports
from model_performance import calculate_model_performance, graph_error_percentage
from data_processing import create_training_set, train_test_partition

# Current working directory to ensure compatibility across devices
cwd = os.getcwd()
folder_path = f'{cwd}\\part4\\datafiles'

def looks_numeric_forgiving(s: str) -> bool:
    s = (s or "").strip()
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

def validate_user_input(prompt: str, min: int, max: int) -> int:
    '''Function to obtain valid numeric based on constrains input from user
    
    Args:
        prompt (str): Message to display to user
        min (int): Smallest value user can enter
        max (int): Largest value user can enter

    Returns:
        user_input (int): User's numeric input
    '''
    while True:
        user_choice = input(prompt)
        if user_choice.isnumeric():
            if int(user_choice) > min and int(user_choice) <= max:
                return int(user_choice)
            else:
                print('Error: Invalid Number')
        else:
            print('Error: Enter number')

def print_table(array: list, column_title: str, margin: int = 10):
    '''Function to print a organized table of values and their indexes with justification
    Args:
        array (list): Containing values to print
        column_title (str): Title of the column
        margin (int): Left justification amount (Default 10)
    '''
    print('Number'.ljust(margin), str(column_title))
    for index, item in enumerate(array):
        print(str(index).ljust(margin), str(item.strip('\n')))

# Obtains all files in specified directory
print(f'Scanning for files in: {folder_path}')
files = os.listdir(folder_path)
# Filters out unnecessary files
csv_files = [
    f for f in files
    if f.lower().endswith(".csv")
]

if csv_files: # Csv files are in directory
    # Prints available files
    print(f'{len(csv_files)} item(s) found.')
    print_table(csv_files, 'File Name')

    # Asks user for file to use
    print('Which file do you want to use for training?')
    choice = validate_user_input('Enter number: ', 0, len(csv_files)-1)
    print(f'----> {csv_files[choice].upper()}')
    training_file = f'{cwd}\\part4\\datafiles\\{csv_files[choice]}'

    # Opens
    try:
        with open(training_file, 'r', encoding='utf-8') as file:
            header = file.readline()
            file_columns = header.split(',')
            row1 = file.readline()
            sample_row = row1.split(',')
    except Exception as e:
        print(f'Error in opening file: {e}')
    
    # Prints table containing columns
    print_table(file_columns, 'Column Name')
    
    # Ask for index to include for output data
    print('Which column do you want to use as output data for the model?')
    while True:
        choice = validate_user_input('Enter number: ', 0, len(file_columns)-1)
        # Check to make sure the chosen column doesn't contain a str
        column_sample = sample_row[choice].strip('\n')
        print(f'CHOICE EXAMPLE "{column_sample}"')
        if not looks_numeric_forgiving(column_sample):
            print('Error: The row must contain a numeric value')
        else:
            print(f'----> {file_columns[choice].upper()}')
            output_index = choice
            break

    # Ask for index to include for input data
    attempts = len(file_columns) - 1
    while attempts:
        ## ENDED OFF HERE
        pass
    input_indexes = [2,3,4,5,6,7,8,9]
    # Stop when done

    # Process data from csv file
    #if training_file:
    X, y = create_training_set(
        file_location=training_file,
        output_index=output_index,
        input_indexes=input_indexes,
    )
    X_train, X_test = train_test_partition(X)
    y_train, y_test = train_test_partition(y)
    print(X_train[0])

    # Train model
    model = LinearRegression(n_jobs=-1)
    model.fit(X=X_train, y=y_train)

    # Make Prediction
    prediction = model.predict(X=X_test)
    #print(prediction[0])

    # Output results/performance visually
    error_percentages = calculate_model_performance(actual_values=y_test, predicted_values=prediction)
    graph_error_percentage(error_percentages, 'Predictions Error Percentages')
else:
    print(f'No CSV files found in: {folder_path.upper()}')
# Loop back to main
#if __name__ == '__main__':
    #main()