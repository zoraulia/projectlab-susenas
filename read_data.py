import pandas as pd
import numpy as np
import joblib

PATH='susenas12/sn12_ki.csv'

# read data function
def read_data(file_directory):
    '''
        file directory: string
        csv file location
    '''
    data = pd.read_csv(file_directory).copy()
    
    joblib.dump(data,
                "./output/sus12_ki.pkl")
    
    print("-----------------DONE read data-----------------")   

if __name__ == '__main__':
    read_data(PATH)