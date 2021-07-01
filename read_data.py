import pandas as pd
import numpy as np

PATH='susenas12/sn12_ki.csv'

kolom=['URUT', 'NART','B1R1', 'B1R2',
        'B1R5', 'UMUR', 'HB', 'JK', 'KWN',
        'B5R17', 'B5R32', 'B5R33', 'B5R18A',
        'B5R19A', 'B5R19B', 'B5R19C', 'B5R20',
        'EXP_CAP', 'WEIND']

ubah_kolom={'URUT':'identifier_rt',
        'NART': 'individu',
        'B1R1': 'provinsi',
        'B1R2': 'kab_kota',
        'B1R5': 'desa_kota',
        'UMUR': 'umur',
        'HB': 'hubkel',
        'JK': 'jenis_kelamin',
        'KWN': 'status_perkawinan',
        'B5R17': 'ijazah',
        'B5R32': 'umur_kawin',
        'B5R33': 'jml_tahun_kawin',
        'B5R18A': 'pend_3bulan',
        'B5R19A': 'bacatulis_Latin',
        'B5R19B': 'bacatulis_Arab',
        'B5R19C': 'bacatulis_Lainnya',
        'B5R20': 'internet',
        'EXP_CAP': 'exp_cap',
        'WEIND': 'weight'}

# read data function
def read_data(file_directory):
    '''
        file directory: string
        csv file location
    '''
    data = pd.read_csv(file_directory).copy()

    return data

# select relevant variables
def select_columns(dataset,list_columns):
    '''
        list_columns: list
    '''
    data = dataset[list_columns].copy()
    return data

# renaming column name to make more sense to the dataset
def change_columns(dataset,dict_column):
    '''
        dict_column: dictionary
    '''
    data = dataset.rename(columns=dict_column).copy()
    return data