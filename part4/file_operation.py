import os
import sys

cwd = os.getcwd()
folder_path = f'{cwd}\\part4\\datafiles'

def get_files():
    contents = os.listdir(folder_path)

    if not contents:
        print(f'No files found in "{folder_path.upper()}"')
        return None
    return contents

def get_columns(file_path, sep: str = ','):
    '''Function to print column names of csv file
    Args:
        file_path (str): Containing full path to csv file
    '''
    margin = 10
    with open(file_path, 'r', encoding='utf-8') as file:
        header = file.readline()
        header_list = header.split(sep)

    return header_list

def validate_feature_choice(file, index):
    pass