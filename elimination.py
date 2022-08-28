"""
Elimination method requires that all cells are filled with all possible candidates.
Therefore, if there are empty cells, code will break
Otherwise,  it checks in each row, column and box if there is a unique number
In this code not a reference to function to fill empty cells with all candidates
"""

import pandas as pd
import sys
from itertools import chain
from functions.parameters import convert_to_column_letter
sys.path.append('/home/rob/PycharmProjects/sudoku/functions')


column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
df = df.iloc[:9, :9]

df_show = df.copy()   # only to see Dataframe in PyCharm with rows index 1 to 9
df_show.index += 1

check_nan_in_df = df.isnull().values.any()
if check_nan_in_df:
    print('sorry, not all cells contain a number or candidates')
    sys.exit()
else:
    print('All cells contain either a number or candidates')

df = df.astype(int)
df_str = df.astype(str)


def occurs_once_row(a, item):
    temp_list = []
    for q in range(9):
        temp_list = temp_list + [df.iloc[row, q]]
        # print(temp_list)

    if item not in temp_list:
        if a.count(item) == 1:
            print('elimination requires all cells are filled in with all possible candidates')
            print('In row ' + str(row + 1) + ' unique value is: ' + str(item))


def occurs_once_col(a, item):
    temp_list = []
    for q in range(9):
        temp_list = temp_list + [df.iloc[q, col]]

    if item not in temp_list:
        if a.count(item) == 1:
            print('elimination requires all cells are filled in with all possible candidates')
            print('In col ' + str(convert_to_column_letter[col + 1]) + ' unique value is: ' + str(item))


for row in range(9):
    row_list_int = []
    row_list = []
    for i in range(9):
        cell = df_str.iloc[row, i]
        cell_sep = list(cell)
        row_list = row_list + [cell_sep]

    row_list_int = list(map(int, chain.from_iterable(row_list)))

    for item in range(1, 10):
        occurs_once_row(row_list_int, item)


for col in range(9):
    col_list_int = []
    col_list = []
    for i in range(9):
        cell = df_str.iloc[i, col]
        cell_sep = list(cell)
        col_list = col_list + [cell_sep]

    col_list_int = list(map(int, chain.from_iterable(col_list)))

    for item in range(1, 10):
        occurs_once_col(col_list_int, item)


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(3):
    for column_box in range(3):
        box = 'I'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(3):
    for column_box in range(3, 6):
        box = 'II'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(3):
    for column_box in range(6, 9):
        box = 'III'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(3, 6):
    for column_box in range(3):
        box = 'IV'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(3, 6):
    for column_box in range(3, 6):
        box = 'V'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(3, 6):
    for column_box in range(6, 9):
        box = 'VI'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(6, 9):
    for column_box in range(3):
        box = 'VII'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(6, 9):
    for column_box in range(3, 6):
        box = 'VIII'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))


box_list = []
box_list_int = []
box_list_numbers = []
for row_box in range(6, 9):
    for column_box in range(6, 9):
        box = 'IX'
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        box_list = box_list + [cell_sep]

        box_list_numbers = box_list_numbers + [df.iloc[row_box, column_box]]

box_list_int = list(map(int, chain.from_iterable(box_list)))

for item in range(1, 10):
    if item not in box_list_numbers:
        if box_list_int.count(item) == 1:
            print('In box ' + box + ' unique value is: ' + str(item))
