import os
from typing import Tuple, List

def create_training_set(file_location:str, output_index: int, input_indexes: list, sep: str = ','):
    '''
    
    '''

    output_data = []
    input_data = []

    with open(file_location, 'r', encoding='utf-8') as datafile:
        header = datafile.readline()
        header_list = header.split(sep)

        # Iterates over every line in file and adds data we want
        for line in datafile:

            # Removes newline escape character and creates a list containing each element
            line_list = line.strip('\n').split(sep)

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

if __name__ == '__main__':
    #cwd = 
    test_location = f'{os.getcwd()}\\part4\\datafiles\\SeoulBikeData.csv'
    X, y = create_training_set(
        file_location=test_location, 
        output_index=1, 
        input_indexes=[2,3],
        sep=','
        )
    
    print(X[0])
    print(y[0])
