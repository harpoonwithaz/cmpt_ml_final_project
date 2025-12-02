# =====================================
# Author: Laurenzo Maddatu, Oliver Tadaniewicz
# Date: 11/24/2025
# Description: Module for processing the data from the csv file into a training set.
# =====================================

import os
from pathlib import Path
from typing import List, Tuple

def create_data_set() -> Tuple[List[List[float]], List[float]]:
    '''
    Function to read a csv file and create a data set for linear regression model. More info in the README file.
    Credit: UC Irvine
    Output data: Curricular units 2nd sem (grade)
    
    In the data processing file we excluded indexes:

    - 29 (2nd sem evaluations) - because you would only know how many exams they took after the semester is over
    - 30 (2nd sem approved) - because it tells the model the success/failure result, giving away the grade
    - 31 (2nd sem grade)- because this is the answer key
    - 32 (2nd sem without evaluations) - because this reveals the number of classes skipped or failed after the semester ends
    - 36 (Target - Future status) - because this leaks the future, whether they eventually graduate or dropout, after the 2nd semester grades are recorded

    Returns: A tuple containing:
        - input_data: 2d array containing float of metrics from students information file.
        - output_data: An array containing float of 2nd semester grades.
    '''
    # Ensures python can find the correct file location
    script_dir = Path(__file__).parent.absolute()
    file_location = os.path.join(script_dir, 'data', 'studentPerformance.csv')

    with open(file_location, "r" , encoding="utf-8") as file:

        # Csv file indexes to not include (refer to README.md for explanations)
        elements_to_skip = (29,30,31,32,36)

        output_data = []
        input_data = []

        header = file.readline()

        lines = file.readlines()
        for line in lines:
            information = line.strip("\n").split(";")
            
            # Getting the list of output data
            grade_value = float(information[31])
            output_data.append(grade_value)

            # Creating the list of lists for the input data
            row_inputs = []
            for i in range(len(information)):
                if i not in elements_to_skip:
                    row_inputs.append(float(information[i]))
            input_data.append(row_inputs)

    return input_data, output_data
def train_test_partition(data: list) -> Tuple[List, List]:
    '''Function to partition data into training data and test data

    Args:
        data (list): The data that will be partitioned
    
    Returns: A tuple containing:
        - training partition: List containing the first 80% of the data passed in
        - test partition: List containing the remaining 20% of the data
    '''
    partition_index = int(len(data) * 0.8) # 80% of the data given will be training data, remaining 20% is test data

    training_partition = data[:partition_index]
    test_partition = data[partition_index:]

    return training_partition, test_partition




