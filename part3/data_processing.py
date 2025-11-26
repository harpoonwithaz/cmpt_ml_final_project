# =====================================
# Author: Laurenzo Maddatu
# Date: 11/24/2025
# Description: Module for processing the data from the csv file into a training set.
# =====================================

import os
from typing import List, Tuple

# Predicting a students second semester grades

def create_data_set() -> Tuple[List[List[float]], List[float]]:

    # Ensures python can find the correct file location
    cwd = os.getcwd()
    file_location = os.path.join(cwd, 'part3', 'data', 'studentPerformance.csv')

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




