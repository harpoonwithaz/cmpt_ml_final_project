import random
from typing import List # For type hinting

from sklearn.linear_model import LinearRegression

def create_inputs() -> List[List[int]]:
    '''
    Creates a list of 100 lists containing 3 random integers from 0 to 1000
    
    Returns:
        2D array; A list of 100 lists, where each sublist contains 3 integers from 0 to 1000.
        Example structure: [[837, 700, 970], [350, 935, 610], ... ]
    '''
    list_of_list = []
    inList = []

    for i in range(100):
        inList = []
        for i in range(3):
            random_int = random.randint(0,1000)
            inList.append(random_int)
        list_of_list.append(inList)

    return list_of_list

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
    output_list = []
    for row in inputs:
        value_1 = row[0]*weight_a
        value_2 = row[1]*weight_b
        value_3 = row[2]*weight_c

        total = value_1 + value_2 + value_3
        output_list.append(total)

            
    #print(f"Original list: {inputs} \n\n\n")

    return output_list

#print(create_outputs(create_inputs(),1,2,3))

# Create training set for prediction
train_input = create_inputs()
train_output = create_outputs(train_input,1,2,3)

# Prediction
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)


# Prediction Test
X_test = [[10,20,30]]
outcome = predictor.predict(X=X_test)
coefficients = predictor.coef_
print("Prediction: " + str(outcome))
print("Coefficients: " + str(coefficients))
