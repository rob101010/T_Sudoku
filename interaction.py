"""
All cells must be filled, therefore check on empty cells
The check_number must appear exactly twice in the row, col or box where you do initial check

"""

import pandas as pd
import sys

column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
df = df.iloc[:9, :9]
df.index += 1


df_str = df.astype(str)  # str is used later to be able to separate 126 in a cell into '1', '2' and '6'

check_nan_in_df = df.isnull().values.any()
if check_nan_in_df:
    print('\nsorry, not all cells contain a number or candidates')
    sys.exit()
else:
    print('\nAll cells contain either a number or candidates\n')



for row in range(9):
    row_list = []
    for i in range(9):
        row_list_temp = df_str.iloc[row, i]
        row_list_temp = list(row_list_temp)
        row_list = row_list + [row_list_temp]

    col_index = []
    for check_number in range(7, 8):
        for j in range(9):
            if str(check_number) in row_list[j]:
                col_index = col_index + [j]
        if len(col_index) == 2:
            if col_index[0] // 3 == col_index[1] // 3:
                cell_index = [row] + [col_index[0]]
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 0:
                    box = 'I'
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 1:
                    box = 'II'
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 2:
                    box = 'III'
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 0:
                    box = 'IV'
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 1:
                    box = 'V'
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 2:
                    box = 'VI'
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 0:
                    box = 'VII'
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 1:
                    box = 'VIII'
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 2:
                    box = 'IX'

                print('Interaction! eliminate check_number ' + str(check_number) + ' in box ' + box + ' except in row ' + str(row + 1))




        # cell_start_row_column_index = str(row + 1) + str(column + 1)  # row_column cell is pot. XY ==> top buddy list
        # cell_start_row_column = df_str.iloc[row, column]
        # cell_start_row_column_sep = list(cell_start_row_column)
        # buddy_series = pd.Series([cell_start_row_column_sep], index=[int(cell_start_row_column_index)])