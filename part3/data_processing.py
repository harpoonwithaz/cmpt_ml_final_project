# Part 3 
# Author Laurenzo Maddatu
# November 24, 2025
import os
from typing import List, Tuple

# Predicting a students second semester grades


def create_data_set() -> Tuple[List[List[int]], List[int]]:

    # Ensures python can find the correct file location
    cwd = os.getcwd()
    file_location = f'{cwd}\\part3\\data\\studentPerformance.csv'

    with open(file_location, "r" , encoding="utf-8") as file:

        # Csv file indexes to not include in input data, 31 is the answer and 30 is the approved list, which would make the prediction too easy 
        elements_to_skip = (30,31)

        output_data = []
        input_data = []

        # Number corresponding to graduate, enrolled, or dropout
        enrollment = {
            "Graduate": 1.0,
            "Enrolled": 2.0,
            "Dropout" : 3.0
        }

        #for line in file.readlines():
        #  print line
        header = file.readline()

        lines = file.readlines()
        for line in lines:
            information = line.strip("\n").split(";")
            
            grade_value = float(information[31])
            output_data.append(grade_value)
        
            row_inputs = []
            for i in range(len(information)):
                if i not in elements_to_skip:
                    # Checking this index specifically because it contains strings, need these lines to use the dictionary from earlier
                    if i == 36:
                        status = information[i].strip()
                        if status in enrollment:
                            row_inputs.append(enrollment[status])
                    else:
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




