# =====================================
# Author: Oliver Tadaniewicz
# Date: 11/18/2025
# Description: 
# =====================================

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# Local module imports
from data_processing import create_data_set

# Obtain appropriate data that will be fed to model
output_data, input_data = create_data_set()
training_input, test_input, training_output, test_output = train_test_split(input_data, output_data)


# Training the model
model = LinearRegression(n_jobs=-1)
model.fit(X=training_input, y=training_output)

# Prediction
prediction = model.predict(X=test_input)
coefficients = 

#print(input_data[0])

if __name__ == '__main__':
    print(len(training_input))
    print(len(test_input))
    print(len(training_output))
    print(len(test_output))

    '''plt.scatter(input_data, output_data, c='r')
    plt.plot(input_data, output_data, c='b')
    plt.show()'''