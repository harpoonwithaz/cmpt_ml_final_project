import pandas as pd
from sklearn.linear_model import LinearRegression
import os

# Local module imports
import file_operation
from model_performance import calculate_model_performance, graph_error_percentage
from data_processing import create_training_set, train_test_partition

cwd = os.getcwd()

def validate_user_input(prompt, min, max):
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
    '''Function to print a nice table of values and their indexes
    Args:
        array (list): Containing values to print
        column_title (str): Title of the column
        margin (int): Left justification amount (Default 10)
    '''
    print('Number'.ljust(margin), str(column_title))
    for index, item in enumerate(array):
        print(str(index).ljust(margin), str(item))

# Ask user which file to use
# Prints the available files in the dedicated folder
files = file_operation.get_files()
if files:
    # Prints available files
    print(f'{len(files)} item(s) found.')
    print_table(files, 'File Name')

    # Asks user for file to use
    print('Which file do you want to use for training?')
    choice = validate_user_input('Enter number: ', 0, len(files)-1)
    training_file = f'{cwd}\\part4\\datafiles\\{files[choice]}'

    # Ask for columns to be used in training and for testing
    # Print out columns
    file_columns = file_operation.get_columns(training_file)
    print_table(file_columns, 'Column Name')
    
    # Ask for index to include for output data
    attempts = 1
    while attempts >= 0:
        print('Which column do you want to use as output data for the model?')
        choice = validate_user_input('Enter number:', 0, len(file_columns)-1)
        output_index = 1
        # I ENDED HERE. MAKE A CHECK FOR IF THE FEATURE CONTAINS A STR

    # Ask for indexes to include for input data
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

# Loop back to main
#if __name__ == '__main__':
    #main()