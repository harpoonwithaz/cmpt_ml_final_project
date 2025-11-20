# =====================================
# Author: Oliver Tadaniewicz
# Date: 11/18/2025
# Description: 
# =====================================

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Local module imports
from data_processing import create_data_set
from model_performance import calculate_model_performance, graph_error_percentage

# Obtain appropriate data that will be fed to model
print('Creating data set...')
X, y = create_data_set()
print('Partitioning Data...')
X_train, X_test, y_train, y_test = train_test_split(X, y)
print(f'Training length x: {len(X_train)}')
print(f'Test length x: {len(X_test)}')

# Training the model
print('Training model...')
model = LinearRegression()
model.fit(X=X_train, y=y_train)

# Prediction
print('Creating prediction...')
prediction = model.predict(X=X_test)

# Model performance
print('Calculating model performance')
error_percentages = calculate_model_performance(y_test, prediction)
print('Graphing error percentage...')
graph_error_percentage(error_percentages, 'Predictions Error Percentages')


