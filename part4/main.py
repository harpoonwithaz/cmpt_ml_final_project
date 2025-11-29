# =====================================
# Author: Oliver Tadaniewicz, Laurenzo Maddatu
# Date: 11/24/2025
# Description: 
# =====================================

# Displays message to show progress in case loading modules take a while
print("Importing modules...")

# Library imports
import os
from sklearn.linear_model import LinearRegression
import csv

# Local module imports
from model_performance import calculate_model_performance, graph_error_percentage
from data_processing import create_training_set, train_test_partition

# Current working directory to ensure compatibility across devices
cwd = os.getcwd()
folder_path = f'{cwd}\\part4\\datafiles'

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def float_convertible(s: str) -> bool:
    '''Function to see if a str can be converted to a float. Returns bool: str can be converted to float.'''
    s = (s or "").strip()
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

def validate_user_input(prompt: str, min: int, max: int, breakout_condition: str = '') -> int:
    '''Function to obtain valid numeric based on constrains input from user
    
    Args:
        prompt (str): Message to display to user
        min (int): Smallest value user can enter
        max (int): Largest value user can enter
        breakout_condition (str): What user will type to exit the loop (Default "")

    Returns:
        user_input (int): User's numeric input | -1 when loop broken
    '''
    while True:
        user_choice = input(prompt)
        if breakout_condition and user_choice.lower() == breakout_condition:
            return -1
        elif user_choice.isnumeric():
            if int(user_choice) >= min and int(user_choice) <= max:
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

def main():
    # Obtains all files in specified directory and filters out non csv files
    #clear_console()
    print(f'Scanning for files in: {folder_path}')
    files = os.listdir(folder_path)
    csv_files = [
        f for f in files
        if f.lower().endswith('.csv')
    ]

    # Csv files are in directory
    if csv_files:
        # Prints available files, asks user for file to use
        print(f'{len(csv_files)} item(s) found.')
        print('Which file do you want to use for training?')
        print_table(csv_files, 'File Name')
        choice = validate_user_input('Enter number: ', 0, len(csv_files)-1)

        clear_console()
        file_choice = csv_files[choice]
        print(f'File choice ----> {file_choice.upper()}')
        training_file = f'{cwd}\\part4\\datafiles\\{file_choice}'

        # Opens file, reads header and first line into lists
        try:
            with open(training_file, 'r', encoding='utf-8') as file:
                # Read first 2 lines of file
                header = file.readline()
                row1 = file.readline()

                # Detects which separator is used by looking at the first row
                dialect = csv.Sniffer().sniff(row1)
                separator = dialect.delimiter
                
                # Puts header and sample line into list
                file_columns = header.split(str(separator))
                sample_row = row1.split(str(separator))
        except Exception as e:
            print(f'Error in opening file: {e}')
        
        # Prints table containing columns
        print('Which column do you want to use as output data for the model?')
        print_table(file_columns, 'Column Name')
        
        # Ask for index to include for output data
        while True:
            output_choice = validate_user_input('Enter number: ', 0, len(file_columns)-1)
            # Check to make sure the chosen column doesn't contain a str
            column_sample = sample_row[output_choice].strip('\n')
            if not float_convertible(column_sample):
                print('Error: The column must contain a numeric value')
                print(f'Column contains "{column_sample}", which is not a numeric value')
            else:
                output_column_choice = file_columns[output_choice].strip('\n').upper()
                clear_console()
                print(f'File choice ----> {file_choice}')
                print(f'Output row choice ----> {output_column_choice}')
                output_index = output_choice
                break

        # Ask for index to include for input data
        # Prints table containing columns
        print('Which column do you want to use as input data for the model?')
        print_table(file_columns, 'Column Name')
        attempts = len(file_columns) - 1
        input_indexes = []
        input_names = []
        while attempts >= 0:
            inputs_choice = validate_user_input('Enter number (Type "done" to stop): ', 0, len(file_columns)-1, breakout_condition='done')
            if inputs_choice == -1 and len(input_indexes) > 0: # When user typed done and at least 1 entry
                attempts = 0
                break
            elif inputs_choice == output_index or inputs_choice in input_indexes:
                print('Error: Choose a number that is not already used')
            else:
                column_sample = sample_row[inputs_choice].strip('\n')
                if not float_convertible(column_sample):
                    print('Error: The column must contain a numeric value')
                    print(f'Column contains "{column_sample}", which is not a numeric value')
                else:
                    input_indexes.append(inputs_choice)
                    input_names.append(file_columns[inputs_choice].strip('\n'))
                    attempts -= 1
        
        # Prints choices
        clear_console()
        print(f'File choice ----> {file_choice}')
        print(f'Output column choice ----> {output_column_choice}')
        print(f'Input column choice ----> ', end='')
        print(*input_names, sep=', ')

        # Process data from csv file, creating training set and partition into test and train data
        X, y = create_training_set(
            file_location=training_file,
            output_index=output_index,
            input_indexes=input_indexes,
            sep=separator
        )
        X_train, X_test = train_test_partition(X)
        y_train, y_test = train_test_partition(y)

        # Train model
        model = LinearRegression(n_jobs=-1)
        model.fit(X=X_train, y=y_train)

        # Make Prediction
        prediction = model.predict(X=X_test)

        # Output results/performance visually
        error_percentages = calculate_model_performance(actual_values=y_test, predicted_values=prediction)
        graph_error_percentage(error_percentages, f'Predictions Error Percentages for {file_choice}')
    else:
        print(f'No CSV files found in: {folder_path.upper()}')
        print('Put a CSV file in the listed directory above and run again.')
    
    run_again = input('Run again? (Y/N) ')
    if run_again.lower() == 'y':
        #turtle.done() # Kills turtle instance
        main()

# Initializes main loop when script is ran
if __name__ == '__main__':
    main()