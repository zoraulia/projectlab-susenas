import pandas as pd
import numpy as np

PATH='susenas12/sn12_ki.csv'

# read data function
def read_data(file_directory):
    '''
        file directory: string
        csv file location
    '''
    data = pd.read_csv(file_directory).copy()

    return data