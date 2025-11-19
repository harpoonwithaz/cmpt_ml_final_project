import random
from typing import List # For type hinting

def create_inputs() -> List[List[int]]:
    '''
    Creates a list of 100 lists containing 3 random integers from 0 to 1000
    
    Returns:
        2D array; A list of 100 lists, where each sublist contains 3 integers from 0 to 1000.
        Example structure: [[837, 700, 970], [350, 935, 610], ... ]
    '''
    inputs = [[]]
    return inputs

def create_outputs(inputs, weight_a, weight_b, weight_c) -> List[int]:
    '''
    Creates a list of 100 outputs by adding each input multiplied by its weight
    
    Args:
        inputs (List[List[int]]): list of lists containing 3 integers
        weight_a (int): The product for the first index in the sublist
        weight_b (int): The product for the second index in the sublist
        weight_c (int): The product for the third index in the sublist

    Returns:
        outputs (List[int]): 
    '''
    return []


