# =====================================
# Author: Oliver Tadaniewicz, Laurenzo Maddatu
# Date: 11/24/2025
# Description: Module to process data from csv file into a format usable
# by the linear regression model.
# =====================================

from typing import Tuple, List

def create_training_set(
        file_location: str, 
        output_index: int, 
        input_indexes: list[int], 
        sep: str = ','
    ) -> Tuple[List[List[int]], List[int]]:
    '''Function to create training set from data in csv.
    
    Args:
        file_location (str): Path to the csv file to create training set.
        output_index (int): Index for column to be used as output data.
        input_indexes (list[int]): Indexes of columns to be used for input data.
        sep (str): Separator used in csv file to separate elements. (Default: ",")

    Returns: A tuple containing:
        - input_data (list[list]): 2d array containing all input features.
        - output-data (list[int]): List of all output features.
    '''

    output_data = []
    input_data = []

    with open(file_location, 'r', encoding='utf-8') as datafile:
        header = datafile.readline()

        # Iterates over every line in file and adds data we want
        for line in datafile:

            # Removes newline escape character and creates a list containing each element
            line_list = line.strip('\n').split(sep)

            # Checks if row contains empty element
            if '' in line_list:
                continue
            else:
                # Adds output data from list 
                output_data.append(float(line_list[output_index]))

                # Adds every element
                input_data.append([float(line_list[index]) for index in input_indexes])
    
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