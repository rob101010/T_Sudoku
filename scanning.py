
import sys
import pandas as pd
from functions.parameters import convert_to_column_letter
sys.path.append('/home/rob/PycharmProjects/sudoku/functions')

column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
df = df.fillna(99999)
df = df.astype(int)


# # ignore multiple candidates in cell
df.loc[df['A'] > 9, 'A'] = 99999
df.loc[df['B'] > 9, 'B'] = 99999
df.loc[df['C'] > 9, 'C'] = 99999
df.loc[df['D'] > 9, 'D'] = 99999
df.loc[df['E'] > 9, 'E'] = 99999
df.loc[df['F'] > 9, 'F'] = 99999
df.loc[df['G'] > 9, 'G'] = 99999
df.loc[df['H'] > 9, 'H'] = 99999
df.loc[df['I'] > 9, 'I'] = 99999


# create 9 boxes lists
box_1 = []
for row_box in range(3):
    for col_box in range(0, 3):
        box_1 = box_1 + [df.iloc[row_box, col_box]]

box_2 = []
for row_box in range(3):
    for col_box in range(3, 6):
        box_2 = box_2 + [df.iloc[row_box, col_box]]

box_3 = []
for row_box in range(3):
    for col_box in range(6, 9):
        box_3 = box_3 + [df.iloc[row_box, col_box]]

box_4 = []
for row_box in range(3, 6):
    for col_box in range(0, 3):
        box_4 = box_4 + [df.iloc[row_box, col_box]]

box_5 = []
for row_box in range(3, 6):
    for col_box in range(3, 6):
        box_5 = box_5 + [df.iloc[row_box, col_box]]

box_6 = []
for row_box in range(3, 6):
    for col_box in range(6, 9):
        box_6 = box_6 + [df.iloc[row_box, col_box]]

box_7 = []
for row_box in range(6, 9):
    for col_box in range(0, 3):
        box_7 = box_7 + [df.iloc[row_box, col_box]]

box_8 = []
for row_box in range(6, 9):
    for col_box in range(3, 6):
        box_8 = box_8 + [df.iloc[row_box, col_box]]

box_9 = []
for row_box in range(6, 9):
    for col_box in range(6, 9):
        box_9 = box_9 + [df.iloc[row_box, col_box]]


# START SCANNING PER BOX

# Scanning on Box I
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(3):
        for column in range(3):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_1:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_1:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr I in cell number ' + str(cell))


# Scanning on Box II
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(3):
        for column in range(3, 6):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_2:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_2:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr II in cell number ' + str(cell))


# Scanning on Box III
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(3):
        for column in range(6, 9):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_3:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_3:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr III in cell number ' + str(cell))


# Scanning on Box IV
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []
    for row in range(3, 6):
        for column in range(3):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_4:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_4:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr IV in cell number ' + str(cell))


# Scanning on Box V
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(3, 6):
        for column in range(3, 6):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_5:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_5:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr V in cell number ' + str(cell))


# Scanning on Box VI
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(3, 6):
        for column in range(6, 9):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_6:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_6:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr VI in cell number ' + str(cell))


# Scanning on Box VII
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(6, 9):
        for column in range(3):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_7:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_7:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr VII in cell number ' + str(cell))


# Scanning on Box VIII
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(6, 9):
        for column in range(3, 6):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_8:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_8:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr VIII in cell number ' + str(cell))


# Scanning on Box IX
for q in range(1, 10):  # (1, 10) (4, 5)
    check_number = q

    candidate_scanning = []
    candidate_lost = []
    cell = []

    for row in range(6, 9):
        for column in range(6, 9):

            if df.iloc[row, column] == 99999 and check_number not in df.iloc[row, :].values.tolist() and check_number not in df.iloc[:, column].values.tolist() and check_number not in box_9:
                candidate_scanning = candidate_scanning + [[row, column]]
                cell = (row + 1, column + 1)
            if df.iloc[row, column] < 10 or check_number in df.iloc[row, :].values.tolist() or check_number in df.iloc[:, column].values.tolist() or check_number in box_9:
                candidate_lost = candidate_lost + [[row, column]]

    if len(candidate_scanning) == 1:
        print('For check_number ' + str(check_number) + ' a scanning result found in box nr IX in cell number ' + str(cell))
