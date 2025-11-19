# =====================================
# Author(s): Oliver Tadaniewicz, Enzo 
# Date: 11/18/2025
# Description: 
# =====================================



import os
from typing import List, Tuple

# --- Important columns (number represents the index) --- 

# Output data (This data is fed to model):
# 1: Rented Bike Count

# Input data:
# 2: Hour
# 3: Temperature (Degrees Celsius)
# 4: Humidity (%)
# 5: Wind speed (m/s)
# 6: Visibility (10m)
# 7: Dew point temperature (Degrees Celsius)
# 8: Solar Radiation (MJ/m2)
# 9: Rainfall (mm)
# 10: Snowfall (cm)
# 11: Seasons (str)
# 12: Holiday (No Holiday/Holiday)
# 13: Functioning day (Yes/No)

def create_data_set() -> Tuple[List[float], List[List[float]]]:
    '''Function to read CSV file data and returns list of input data and list of output data.
    
    Returns: A tuple containing:
        - output_data: List containing rented bike count in hour.
        - input_data: List of lists containing float of metrics from bike rental in hour:
            - index 0: Hour
            - index 1: Temperature (degrees celsius)
            - index 2: Humidity (%)
            - index 3: Wind speed (m/s)
            - index 4: Visibility (10m)
            - index 5: Dew point temperature (degrees celsius)
            - index 6: Solar radiation (MJ/m2)
            - index 7: Rainfall (mm)
            - index 8: Snowfall (cm)
            - index 9: Seasons (Represented by float):
                - Winter = 0.0
                - Spring = 1.0
                - Summer = 2.0
                - Autumn = 3.0
            - index 10: Holiday (Represented by float):
                - No Holiday = 0.0
                - Holiday = 1.0
    '''

    cwd = os.getcwd()
    file_location = f'{cwd}\\part2\\dataset\\SeoulBikeData.csv'

    # Number corresponding to season
    season_map = {
        'Winter': 0.0,
        'Spring': 1.0,
        'Summer': 2.0,
        'Autumn': 3.0
    }

    output_data = []
    input_data = []

    with open(file_location, 'r', encoding='utf-8') as file:
        header = file.readline() # Removes header from file

        for line in file:
            
            # Removes newline escape character and creates a list containing each element
            line_list = line.strip('\n').split(',')

            # Checks if it was a date of operation
            if line_list[13].lower() == 'yes':
                # Adds rented bike count to output list
                output_data.append(float(line_list[1]))


                # Uses list comprehension to add the elements we need to the list, then appends it to input_data
                input_data.append([
                    (
                        # Adds season element using float from seasons map
                        season_map[x] if i == 11 else
                        
                        # Adds holiday element
                        1.0 if i == 12 and x.lower() == 'holiday' else
                        0.0 if i == 12 and x.lower() == 'no holiday' else
                        float(x) # Adds the element from line_list
                    )
                    for i, x in enumerate(line_list)
                    if i not in (0, 1, 13) # Skips the elements we don't need (Date, Rented bike count, Functioning day)
                    ])

    return output_data, input_data

def partition_data(data: list) -> Tuple[List, List]:
    '''Function to partition data into training data and test data
    
    Returns:
    '''
    partition_index = int(len(data) * 0.8) # 80% of the data given will be training data, remaining 20% is test data

    training_partition = data[:partition_index]
    test_partition = data[partition_index:]

    return training_partition, test_partition

# For testing purposes
if __name__ == '__main__':
    out, i = create_data_set()
    print(i[0])
    print(len(out))
    print(len(i))

    train, test = partition_data(out)
    print(len(train))
    print(len(test))