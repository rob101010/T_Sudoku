
import numpy as np
import pandas as pd
from parameters import *

# numbers you want to do analysis on
check_number_1 = '6'
check_number_2 = ''
check_number_3 = ''
check_number_4 = ''

# make also a check_number as an integer, used later in df
if len(check_number_1) > 0:
    check_number_1_int = int(check_number_1)
else:
    check_number_1_int = 99

if len(check_number_2) > 0:
    check_number_2_int = int(check_number_2)
else:
    check_number_2_int = 99

if len(check_number_3) > 0:
    check_number_3_int = int(check_number_3)
else:
    check_number_3_int = 99

if len(check_number_4) > 0:
    check_number_24int = int(check_number_4)
else:
    check_number_4_int = 99


# df_all = pd.read_excel(io='/media/rob/Shared/SDK.xlsx', sheet_name='python')
df_all = pd.read_excel(io='data/SDK_shared.xlsx', sheet_name='python')

# Dataframe, which only shows cell with multiple possible entries. This df is used in most analysis
# df = pd.read_excel(io='/data/SDK.xlsx', sheet_name='python')
df = pd.read_excel(io='data/SDK_shared.xlsx', sheet_name='python')
df.fillna(0, inplace=True)
df[df < 10] = 0


def mlist(n):
    for _ in range(n):
        yield []


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print((bo[i][j]) + " ", end="")


# create single list with all 81 entries
list_81 = []
for r in range(9):
    for c in range(9):
        my_number = (df.iloc[r, c])
        list_81.append(my_number)

# create list of list, so each cell has its own list with either 1 number or multiple numbers.
# this is necessary if you split later multiple numbers that belong to same cell
list_of_lists_81 = []

for var_ in list_81:
    result = [var_]
    list_of_lists_81.append(result)


# Show output in sudoku graph (sudoku_pattern) in console with only the check_number visible
# check if specific number is in cell with multiple entries
# use cell_ in {} to do analysis on cell_1, cell_2 etc.
# outcomes in list of 81 cells (so no list of list)
cell_ = {}
sdk = list(mlist(81))

i = 0
for k in range(81):
    i += 1
    cell_[i] = list(str(int(list_of_lists_81[i - 1][[0][0]])))

    if check_number_1 in cell_[i] and check_number_2 not in cell_[i] and check_number_3 not in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_1) + '.' + '.' + '.'
    if check_number_1 in cell_[i] and check_number_2 in cell_[i] and check_number_3 not in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_1) + str(check_number_2) + '.' + '.'
    if check_number_1 in cell_[i] and check_number_2 not in cell_[i] and check_number_3 in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_1) + str(check_number_3) + '.' + '.'
    if check_number_1 in cell_[i] and check_number_2 not in cell_[i] and check_number_3 not in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_1) + str(check_number_4) + '.' + '.'
    if check_number_1 in cell_[i] and check_number_2 in cell_[i] and check_number_3 in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_1) + str(check_number_2) + str(check_number_3) + '.'
    if check_number_1 in cell_[i] and check_number_2 in cell_[i] and check_number_3 not in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_1) + str(check_number_2) + str(check_number_4) + '.'
    if check_number_1 in cell_[i] and check_number_2 not in cell_[i] and check_number_3 in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_1) + str(check_number_3) + str(check_number_4) + '.'
    if check_number_1 in cell_[i] and check_number_2 in cell_[i] and check_number_3 in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_1) + str(check_number_2) + str(check_number_3) + str(check_number_4)
    if check_number_1 not in cell_[i] and check_number_2 in cell_[i] and check_number_3 not in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_2) + '.' + '.' + '.'
    if check_number_1 not in cell_[i] and check_number_2 in cell_[i] and check_number_3 in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_2) + str(check_number_3) + '.' + '.'
    if check_number_1 not in cell_[i] and check_number_2 in cell_[i] and check_number_3 not in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_2) + str(check_number_4) + '.' + '.'
    if check_number_1 not in cell_[i] and check_number_2 in cell_[i] and check_number_3 in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_2) + str(check_number_3) + str(check_number_4) + '.'
    if check_number_1 not in cell_[i] and check_number_2 not in cell_[i] and check_number_3 in cell_[i] and check_number_4 not in cell_[i]:
        result = str(check_number_3) + '.' + '.' + '.'
    if check_number_1 not in cell_[i] and check_number_2 not in cell_[i] and check_number_3 in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_3) + str(check_number_4) + '.' + '.'
    if check_number_1 not in cell_[i] and check_number_2 not in cell_[i] and check_number_3 not in cell_[i] and check_number_4 in cell_[i]:
        result = str(check_number_4) + '.' + '.' + '.'
    if check_number_1 not in cell_[i] and check_number_2 not in cell_[i] and check_number_3 not in cell_[i] and check_number_4 not in cell_[i]:
        result = '.' + '.' + '.' + '.'
    sdk[i - 1].append(result)

# convert to list of list, with each ROW in a list within the list
sudoku_pattern = list(mlist(9))
sudoku_pattern[0] = sdk[0] + sdk[1] + sdk[2] + sdk[3] + sdk[4] + sdk[5] + sdk[6] + sdk[7] + sdk[8]
sudoku_pattern[1] = sdk[9] + sdk[10] + sdk[11] + sdk[12] + sdk[13] + sdk[14] + sdk[15] + sdk[16] + sdk[17]
sudoku_pattern[2] = sdk[18] + sdk[19] + sdk[20] + sdk[21] + sdk[22] + sdk[23] + sdk[24] + sdk[25] + sdk[26]
sudoku_pattern[3] = sdk[27] + sdk[28] + sdk[29] + sdk[30] + sdk[31] + sdk[32] + sdk[33] + sdk[34] + sdk[35]
sudoku_pattern[4] = sdk[36] + sdk[37] + sdk[38] + sdk[39] + sdk[40] + sdk[41] + sdk[42] + sdk[43] + sdk[44]
sudoku_pattern[5] = sdk[45] + sdk[46] + sdk[47] + sdk[48] + sdk[49] + sdk[50] + sdk[51] + sdk[52] + sdk[53]
sudoku_pattern[6] = sdk[54] + sdk[55] + sdk[56] + sdk[57] + sdk[58] + sdk[59] + sdk[60] + sdk[61] + sdk[62]
sudoku_pattern[7] = sdk[63] + sdk[64] + sdk[65] + sdk[66] + sdk[67] + sdk[68] + sdk[69] + sdk[70] + sdk[71]
sudoku_pattern[8] = sdk[72] + sdk[73] + sdk[74] + sdk[75] + sdk[76] + sdk[77] + sdk[78] + sdk[79] + sdk[80]

# If in first column '....', then only  '.' is shown, breaking the symmetry in the console
for i in range(len(sudoku_pattern)):
    if sudoku_pattern[i][0] == '....':
        sudoku_pattern[i][0] = ',...'

print_board(sudoku_pattern)


# start code to get pattern into integers and into DataFrame
# first in a list of 81 cells
# may be multiple numbers to combine, so first combine strings and then make integer
cell_int_ = {}
sdk_int = list(mlist(81))

i = 0
for k in range(81):
    i += 1
    cell_int_[i] = list(str(int(list_of_lists_81[i - 1][[0][0]])))

    if check_number_1 in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_1
        result = int(result_str)
    if check_number_1 in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_1 + check_number_2
        result = int(result_str)
    if check_number_1 in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_1 + check_number_3
        result = int(result_str)
    if check_number_1 in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_1 + check_number_4
        result = int(result_str)
    if check_number_1 in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 in cell_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_1 + check_number_2 + check_number_3
        result = int(result_str)
    if check_number_1 in cell_[i] and check_number_2 in cell_[i] and check_number_3 not in cell_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_1 + check_number_2 + check_number_4
        result = int(result_str)
    if check_number_1 in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_1 + check_number_3 + check_number_4
        result = int(result_str)
    if check_number_1 in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_1 + check_number_2 + check_number_3 + check_number_4
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_2
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_2 + check_number_3
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_2 + check_number_4
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_2 + check_number_3 + check_number_4
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result_str = check_number_3
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_3 + check_number_4
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 in cell_int_[i]:
        result_str = check_number_4
        result = int(result_str)
    if check_number_1 not in cell_int_[i] and check_number_2 not in cell_int_[i] and check_number_3 not in cell_int_[i] and check_number_4 not in cell_int_[i]:
        result = ""
    sdk_int[i - 1].append(result)


# convert to list of list, with each ROW in a list within the list
sudoku_pattern_int = list(mlist(9))
sudoku_pattern_int[0] = sdk_int[0] + sdk_int[1] + sdk_int[2] + sdk_int[3] + sdk_int[4] + sdk_int[5] + sdk_int[6] + sdk_int[7] + sdk_int[8]
sudoku_pattern_int[1] = sdk_int[9] + sdk_int[10] + sdk_int[11] + sdk_int[12] + sdk_int[13] + sdk_int[14] + sdk_int[15] + sdk_int[16] + sdk_int[17]
sudoku_pattern_int[2] = sdk_int[18] + sdk_int[19] + sdk_int[20] + sdk_int[21] + sdk_int[22] + sdk_int[23] + sdk_int[24] + sdk_int[25] + sdk_int[26]
sudoku_pattern_int[3] = sdk_int[27] + sdk_int[28] + sdk_int[29] + sdk_int[30] + sdk_int[31] + sdk_int[32] + sdk_int[33] + sdk_int[34] + sdk_int[35]
sudoku_pattern_int[4] = sdk_int[36] + sdk_int[37] + sdk_int[38] + sdk_int[39] + sdk_int[40] + sdk_int[41] + sdk_int[42] + sdk_int[43] + sdk_int[44]
sudoku_pattern_int[5] = sdk_int[45] + sdk_int[46] + sdk_int[47] + sdk_int[48] + sdk_int[49] + sdk_int[50] + sdk_int[51] + sdk_int[52] + sdk_int[53]
sudoku_pattern_int[6] = sdk_int[54] + sdk_int[55] + sdk_int[56] + sdk_int[57] + sdk_int[58] + sdk_int[59] + sdk_int[60] + sdk_int[61] + sdk_int[62]
sudoku_pattern_int[7] = sdk_int[63] + sdk_int[64] + sdk_int[65] + sdk_int[66] + sdk_int[67] + sdk_int[68] + sdk_int[69] + sdk_int[70] + sdk_int[71]
sudoku_pattern_int[8] = sdk_int[72] + sdk_int[73] + sdk_int[74] + sdk_int[75] + sdk_int[76] + sdk_int[77] + sdk_int[78] + sdk_int[79] + sdk_int[80]


# Create Dataframe, similar to sudoku in console. In dataframe analysis for patterns with only check_numbers shown
df_sudoku = pd.DataFrame(sudoku_pattern_int, index=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
df_sudoku.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
