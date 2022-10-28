"""
Row Interaction: if number can only be in exactly 2 cells in row: if cells in same box=> eliminate number in rest of box
Col Interaction: if number can only be in exactly 2 cells in col: if cells in same box=> eliminate number in rest of box
Box Interaction: if number can only be in exactly 2 cells in box: if cells in same row=> eliminate number in rest of row
Box Interaction: if number can only be in exactly 2 cells in box: if cells in same col=> eliminate number in rest of col

Interaction only works if all cells are filled with all possible candidates ==> therefore check on empty cells

Code for Row and column interaction:
create df_box in which each box is converted tro a row.
Analyze each row in df separately. Each row in row_list. Then check for each check_number if in row. If so, add
column number (is in this case col_index in the loop from 1 to 9) to col_index_list.
Check if check_number can only be in exactly 2 cells in the row. If so, check if these 2 cells are in same box.
If so, you know you can delete check_number for all other cells in the same box.
To avoid too many print warnings where there is Row_interaction, but no check_numbers to be deleted, check if
check_number is indeed in box. Count number of times check_number is in box. Must of course at least be twice, so only
if more than 2 times, yoi know there are cells to delete the check_number. Only then print statement

Box_interaction
Easier to find boxes with 2 possible places for a check>_number. More complex is to find if these two cells are in same
row or column. Only if in same row (column), check if check_number also in same row (column) outside the box.
If so, you can delete them in same row (column) outside the box
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


# Create new DataFrame df_box, in which each box is converted to a row

# make copy of df, so df_box has right dimensions
df_box = df.astype(int)


# box 1
i = -1
for row_box in range(3):
    for column_box in range(3):
        i += 1
        df_box.iloc[0, i] = df.iloc[row_box, column_box]

# box 2
i = -1
for row_box in range(3):
    for column_box in range(3, 6):
        i += 1
        df_box.iloc[1, i] = df.iloc[row_box, column_box]

# box 3
i = -1
for row_box in range(3):
    for column_box in range(6, 9):
        i += 1
        df_box.iloc[2, i] = df.iloc[row_box, column_box]

# box 4
i = -1
for row_box in range(3, 6):
    for column_box in range(3):
        i += 1
        df_box.iloc[3, i] = df.iloc[row_box, column_box]

# box 5
i = -1
for row_box in range(3, 6):
    for column_box in range(3, 6):
        i += 1
        df_box.iloc[4, i] = df.iloc[row_box, column_box]

# box 6
i = -1
for row_box in range(3, 6):
    for column_box in range(6, 9):
        i += 1
        df_box.iloc[5, i] = df.iloc[row_box, column_box]

# box 7
i = -1
for row_box in range(6, 9):
    for column_box in range(3):
        i += 1
        df_box.iloc[6, i] = df.iloc[row_box, column_box]

# box 8
i = -1
for row_box in range(6, 9):
    for column_box in range(3, 6):
        i += 1
        df_box.iloc[7, i] = df.iloc[row_box, column_box]

# box 9
i = -1
for row_box in range(6, 9):
    for column_box in range(6, 9):
        i += 1
        df_box.iloc[8, i] = df.iloc[row_box, column_box]

df_box_str = df_box.astype(str)

# df_box_index is only needed for BOX_interaction.
# each number is index number in original df (which is SDK-file), but in order as in df_box
# create DataFrame with index numbers to original df (=SDK-file) of all cells in DataFrame df_box
# so, if you take index of a cell in df_box and use same index in df_box_index, you know which cell in df the number is
data = [[11, 12, 13, 21, 22, 23, 31, 32, 33],
        [14, 15, 16, 24, 25, 26, 34, 35, 36],
        [17, 18, 19, 27, 28, 29, 37, 38, 39],
        [41, 42, 43, 51, 52, 53, 61, 62, 63],
        [44, 45, 46, 54, 55, 56, 64, 65, 66],
        [47, 48, 49, 57, 58, 59, 67, 68, 69],
        [71, 72, 73, 81, 82, 83, 91, 92, 93],
        [74, 75, 76, 84, 85, 86, 94, 95, 96],
        [77, 78, 79, 87, 88, 89, 97, 98, 99]
        ]

df_box_index = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
df_box_index.index += 1


# CHECK FOR INTERACTION ACROSS ROWS

# add row to list (via loop ensure every row is analysed)
for row in range(9):
    row_list = []
    for i in range(9):
        row_list_temp = df_str.iloc[row, i]
        row_list_temp = list(row_list_temp)
        row_list = row_list + [row_list_temp]

    # in row_list check if a check_number occurs exactly twice
    for check_number in range(9):
        col_index_list = []    # to contain column index of check_number
        for col_index in range(9):
            if str(check_number) in row_list[col_index]:
                col_index_list = col_index_list + [col_index]
        if len(col_index_list) == 2:    # check if check_number exactly twice in a row
            if col_index_list[0] // 3 == col_index_list[1] // 3:  # check if both cells are in same box
                cell_index = [row] + [col_index_list[0]]  # pick first cell to find box number (is same for 2nd cell!!)
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 0:
                    box = 'I'   # used for print statement
                    box_nr = 1  # used as index in df_box to find all entries in this box
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 1:
                    box = 'II'
                    box_nr = 2
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 2:
                    box = 'III'
                    box_nr = 3
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 0:
                    box = 'IV'
                    box_nr = 4
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 1:
                    box = 'V'
                    box_nr = 5
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 2:
                    box = 'VI'
                    box_nr = 6
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 0:
                    box = 'VII'
                    box_nr = 7
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 1:
                    box = 'VIII'
                    box_nr = 8
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 2:
                    box = 'IX'
                    box_nr = 9

                elimination_list = []  # contains all entries in the box in which the 2 cells are discovered
                for q in range(9):
                    cell = df_box_str.iloc[box_nr - 1, q]
                    cell_sep = list(cell)
                    elimination_list = elimination_list + [cell_sep]

                # look for nr of times check_number in box. If nr> 2 (i.e. the 2 cells) ==> can eliminate in other cells
                elimination_potential = 0
                for p in range(9):
                    if str(check_number) in elimination_list[p]:
                        elimination_potential += 1
                if elimination_potential > 2:
                    print('ROW_Interaction in row ' + str(row + 1) + ' for number ' + str(
                        check_number) + ' : eliminate number ' + str(
                        check_number) + ' in box ' + box + ' except in row ' + str(row + 1))

# CHECK FOR INTERACTION ACROSS COLUMNS

# add column to list (via loop ensure every column is analysed)
for column in range(9):
    column_list = []
    for i in range(9):
        column_list_temp = df_str.iloc[i, column]
        column_list_temp = list(column_list_temp)
        column_list = column_list + [column_list_temp]

        # in column_list check if a check_number occurs exactly twice
    for check_number in range(9):
        row_index_list = []  # to contain row index of check_number
        for row_index in range(9):
            if str(check_number) in column_list[row_index]:
                row_index_list = row_index_list + [row_index]
        if len(row_index_list) == 2:  # check if check_number exactly twice in a column
            if row_index_list[0] // 3 == row_index_list[1] // 3:  # check if both cells are in same BIG ROW (i.e. same box)
                cell_index = [row_index_list[0]] + [column]  # pick first cell to find box number (is same for 2nd cell!!)   !!!!!!!!!!!!!!!!!
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 0:
                    box = 'I'  # used for print statement
                    box_nr = 1  # used as index in df_box to find all entries in this box
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 1:
                    box = 'II'
                    box_nr = 2
                if cell_index[0] // 3 == 0 and cell_index[1] // 3 == 2:
                    box = 'III'
                    box_nr = 3
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 0:
                    box = 'IV'
                    box_nr = 4
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 1:
                    box = 'V'
                    box_nr = 5
                if cell_index[0] // 3 == 1 and cell_index[1] // 3 == 2:
                    box = 'VI'
                    box_nr = 6
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 0:
                    box = 'VII'
                    box_nr = 7
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 1:
                    box = 'VIII'
                    box_nr = 8
                if cell_index[0] // 3 == 2 and cell_index[1] // 3 == 2:
                    box = 'IX'
                    box_nr = 9

                elimination_list = []  # contains all entries in the box in which the 2 cells are discovered
                for q in range(9):
                    cell = df_box_str.iloc[box_nr - 1, q]   # in df_box each box is a row, so first box_nr - 1
                    cell_sep = list(cell)
                    elimination_list = elimination_list + [cell_sep]

                # look for nr of times check_number in box. If nr> 2 (i.e. the 2 cells) ==> can eliminate in other cells
                elimination_potential = 0
                for p in range(9):
                    if str(check_number) in elimination_list[p]:
                        elimination_potential += 1
                if elimination_potential > 2:
                    print('COL_Interaction in col ' + str(column + 1) + ' for number ' + str(
                        check_number) + ' : eliminate number ' + str(
                        check_number) + ' in box ' + box + ' except in column ' + str(column + 1))

# CHECK FOR INTERACTION ACROSS BOXES

# add box to list (via loop ensure every box is analysed)
for box in range(9):
    box_list = []
    for i in range(9):
        box_list_temp = df_box_str.iloc[box, i]
        box_list_temp = list(box_list_temp)
        box_list = box_list + [box_list_temp]

    # in box_list check if a check_number occurs exactly twice
    for check_number in range(9):
        box_index_list = []    # to contain row-column index of check_number (e.g. 21 is row 2, column 1
        for box_index in range(9):
            if str(check_number) in box_list[box_index]:
                box_index_temp = str(df_box_index.iloc[box, box_index])  # box gives row number in df_box_index!!!!!!!
                box_index_temp = list(box_index_temp)                    # box_index gives column number in df_box_index
                box_index_list = box_index_list + [box_index_temp]

        if len(box_index_list) == 2:
            column_interaction_first_cell = box_index_list[0][1]   # for first cell get column index in df!!!!
            column_interaction_second_cell = box_index_list[1][1]  # for second cell get column index in fd

            row_interaction_first_cell = box_index_list[0][0]
            row_interaction_second_cell = box_index_list[1][0]

            elimination_in_column = 0
            if column_interaction_first_cell == column_interaction_second_cell:   # check if 2 cells are in same column
                for w in range(9):  # if 2 cells in same column,m check if check_numbers also other cells same column
                    if str(check_number) in df_str.iloc[w, int(column_interaction_first_cell) - 1]:
                        elimination_in_column += 1
                if elimination_in_column > 2:  # if check_number more than twice in column ==> cells to be deleted
                    print('BOX_Interaction in box ' + str(box + 1) + ' for number ' + str(
                            check_number) + ' : eliminate number ' + str(check_number) + ' in column ' + str(
                            column_interaction_first_cell) + ' except in rows ' + str(
                            row_interaction_first_cell) + ' and ' + str(row_interaction_second_cell))

            elimination_in_row = 0
            if row_interaction_first_cell == row_interaction_second_cell:
                for w in range(9):
                    if str(check_number) in df_str.iloc[int(row_interaction_first_cell) - 1, w]:
                        elimination_in_row += 1
                if elimination_in_row > 2:
                    print('BOX_Interaction in box ' + str(box + 1) + ' for number ' + str(
                            check_number) + ' : eliminate number ' + str(check_number) + ' in row ' + str(
                            row_interaction_first_cell) + ' except in columns ' + str(
                            column_interaction_first_cell) + ' and ' + str(column_interaction_second_cell))
