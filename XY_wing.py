"""
XY wing and XYZ wing


For each cell, check if it can be XY. Create buddy_list for each cell, with potential XY_cell always first entry in BL
Buddy_list (BL) is potential XY cell, then same row, then same column, then same box (all 9 boxes are first created).
As you first add rows, then columns, then box you get double entries where they overlap. Double entries are removed

In buddy_list, check if potential XY_cell has 2 entries, i.e. 2 potential numbers for that cell.
If so, create Z_List, which includes all other cells with:
- 2 entries
- not a pair with XY_cell (so can not contain X & Y)
- contain either X value or Y value

create lists:
z_list:              for potential Z_cells includes the Z-value (i.e. content minus either X or Y value
z_index_list         for z_list itt gives the index of the cells
z_both_numbers_list  is content of potential Z_cells, given as 1 number, so '7' '8' becomes 78

Finally, check if potential XY and Z1 and Z2 indeed XY_wing.
For each possible combinations of Z1 and Z2 in the list do following checks:
- Z_1 and Z_2 are NOT a pair and indeed share the sane Z-value
-  Z_1 and Z_2 are NOT buddies of each other, because then no XY_wing!!)


XYZ wing
For each cell create buddy list
Check if this cell has indeed 3 entries
If so, add all entries in buddy list
check for cells in buddy list with 2 entries
For each potential Z cells do some checks:
For each combi check if their 2 entries are in common with XYZ
make sure Z1 and Z2 are not a pair
If so, the common entry in Z1 and Z2 is the Z_value


"""

import pandas as pd

column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
df = df.iloc[:9, :9]
df.index += 1
df = df.fillna(999999)  # string type requires non NAN: must be 6 times '9', to exclude them from quintuplet
df = df.astype(int)

df_str = df.astype(str)  # str is used later to be able to separate 126 in a cell into '1', '2' and '6'

# box 1
box_series_1 = pd.Series([''], index=[0])
for row_box in range(3):
    for column_box in range(3):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_1 = box_series_1.append(series_temp)
box_series_1 = box_series_1.drop(labels=[0])

# box 2
box_series_2 = pd.Series([''], index=[0])
for row_box in range(3):
    for column_box in range(3, 6):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_2 = box_series_2.append(series_temp)
box_series_2 = box_series_2.drop(labels=[0])

# box 3
box_series_3 = pd.Series([''], index=[0])
for row_box in range(3):
    for column_box in range(6, 9):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_3 = box_series_3.append(series_temp)
box_series_3 = box_series_3.drop(labels=[0])

# box 4
box_series_4 = pd.Series([''], index=[0])
for row_box in range(3, 6):
    for column_box in range(3):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_4 = box_series_4.append(series_temp)
box_series_4 = box_series_4.drop(labels=[0])

# box 5
box_series_5 = pd.Series([''], index=[0])
for row_box in range(3, 6):
    for column_box in range(3, 6):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_5 = box_series_5.append(series_temp)
box_series_5 = box_series_5.drop(labels=[0])

# box 6
box_series_6 = pd.Series([''], index=[0])
for row_box in range(3, 6):
    for column_box in range(6, 9):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_6 = box_series_6.append(series_temp)
box_series_6 = box_series_6.drop(labels=[0])

# box 7
box_series_7 = pd.Series([''], index=[0])
for row_box in range(6, 9):
    for column_box in range(3):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_7 = box_series_7.append(series_temp)
box_series_7 = box_series_7.drop(labels=[0])

# box 8
box_series_8 = pd.Series([''], index=[0])
for row_box in range(6, 9):
    for column_box in range(3, 6):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_8 = box_series_8.append(series_temp)
box_series_8 = box_series_8.drop(labels=[0])

# box 9
box_series_9 = pd.Series([''], index=[0])
for row_box in range(6, 9):
    for column_box in range(6, 9):
        cell_index = str(row_box + 1) + str(column_box + 1)
        cell = df_str.iloc[row_box, column_box]
        cell_sep = list(cell)
        series_temp = pd.Series([cell_sep], index=[int(cell_index)])
        box_series_9 = box_series_9.append(series_temp)
box_series_9 = box_series_9.drop(labels=[0])

# here loop starts for every cell to do the analysis on
for row in range(9):  # for each cell create buddy_list. First add this cell as first entry in BL, then row, col, box
    for column in range(9):
        cell_start_row_column_index = str(row + 1) + str(column + 1)  # row_column cell is pot. XY ==> top buddy list
        cell_start_row_column = df_str.iloc[row, column]
        cell_start_row_column_sep = list(cell_start_row_column)  # each double number as 2 sep # in string(26 = '2','6')
        buddy_series = pd.Series([cell_start_row_column_sep], index=[int(cell_start_row_column_index)])
        for i in range(9):  # add the row to buddy_list
            cell_index = str(row + 1) + str(i + 1)
            cell = df_str.iloc[row, i]  # loop through each cell in column
            cell_sep = list(cell)  # each double number as 2 separate numbers in string (26 = '2','6')
            series_temp = pd.Series([cell_sep], index=[int(cell_index)])
            buddy_series = buddy_series.append(series_temp)
        for j in range(9):  # add the column to buddy_list
            cell_index = str(j + 1) + str(column + 1)
            cell = df_str.iloc[j, column]  # loop through each cell in row
            cell_sep = list(cell)
            series_temp = pd.Series([cell_sep], index=[int(cell_index)])
            buddy_series = buddy_series.append(series_temp)

        # determine correct box to add to buddy_list, based on row and column in the loop
        if row // 3 == 0 and column // 3 == 0:
            correct_box = box_series_1
        if row // 3 == 0 and column // 3 == 1:
            correct_box = box_series_2
        if row // 3 == 0 and column // 3 == 2:
            correct_box = box_series_3
        if row // 3 == 1 and column // 3 == 0:
            correct_box = box_series_4
        if row // 3 == 1 and column // 3 == 1:
            correct_box = box_series_5
        if row // 3 == 1 and column // 3 == 2:
            correct_box = box_series_6
        if row // 3 == 2 and column // 3 == 0:
            correct_box = box_series_7
        if row // 3 == 2 and column // 3 == 1:
            correct_box = box_series_8
        if row // 3 == 2 and column // 3 == 2:
            correct_box = box_series_9

        buddy_series = buddy_series.append(correct_box)  # add correct box to buddy_list
        index = buddy_series.index  # as you add row,col,box ==> double entries: remove double entries
        buddy_series_unique = buddy_series[~index.duplicated(keep='first')]

        # XY WING

        # if XY indeed 2 entries,  make list of all potential Z_cells in this buddy_list
        if len(buddy_series_unique.iloc[0]) == 2:
            x = buddy_series_unique.iloc[0][0]
            y = buddy_series_unique.iloc[0][1]
            xy_index = buddy_series_unique.index[0]
            z_list = []
            z_index_list = []
            z_both_numbers_list = []
            # for all potential Z_cells in list (not first entry, because that is XY_cell, so range (1 to 21)
            for potential_Z in range(1, 21):
                if len(buddy_series_unique.iloc[potential_Z]) == 2:  # check _cells has 2 entries
                    if buddy_series_unique.iloc[potential_Z] != buddy_series_unique.iloc[0]:  # exclude if pair with XY
                        if (x in buddy_series_unique.iloc[potential_Z]) or (y in buddy_series_unique.iloc[potential_Z]):
                            # make copy of buddy_series_unique, so buddy_s_u not changed if you remove X and Y
                            z_temp = buddy_series_unique.iloc[potential_Z].copy()
                            z_index_temp = [buddy_series_unique.index[potential_Z]]  # get cell index of z
                            z_concat = str(int(''.join(z_temp)))
                            z_both_numbers_list = z_both_numbers_list + [z_concat]  # concat to make '7' '8' ==> 78
                            if x in z_temp:
                                z_temp.remove(x)
                            if y in z_temp:
                                z_temp.remove(y)
                            z_list = z_list + z_temp
                            z_index_list = z_index_list + z_index_temp

            # for all possible combination of 2 Z_cells do the XY wing check
            # first check if 2 Z_cells are NOT a pair and have same Z_value
            # then check that Z_1 and Z_2 are NOT buddies of each other (because then not a XY Wing!!)

            number_candidates = len(z_both_numbers_list)  # make all possible combinations of 2 Z_cells
            if len(z_both_numbers_list) > 1:
                for check_number_1 in range(number_candidates - 1):
                    for check_number_2 in range(1, number_candidates):
                        if check_number_1 + check_number_2 <= len(z_both_numbers_list) - 1:
                            if z_both_numbers_list[check_number_1] != z_both_numbers_list[
                                check_number_1 + check_number_2]:
                                if z_list[check_number_1] == z_list[check_number_1 + check_number_2]:  # check same z_
                                    # On XY index get the Row and Column (needed for buddy check each Z_cell & XY_cell)
                                    xy_index_sep = list(str(xy_index))
                                    # Index Z_1 and Z_2, as separate numbers
                                    z_index_list_first_entry_sep = list(str((z_index_list[check_number_1])))
                                    z_index_list_second_entry_sep = list(
                                        str((z_index_list[check_number_1 + check_number_2])))

                                    # Check needed to make sure Z_1 and Z_2 are NOT buddies
                                    if ((int(z_index_list_first_entry_sep[0])) - 1) // 3 != \
                                            ((int(z_index_list_second_entry_sep[0])) - 1) // 3 or \
                                            (((int(z_index_list_first_entry_sep[1])) - 1) // 3 !=
                                             ((int(z_index_list_second_entry_sep[1])) - 1) // 3):

                                        if z_index_list_first_entry_sep[0] != z_index_list_second_entry_sep[0]:

                                            if z_index_list_first_entry_sep[1] != z_index_list_second_entry_sep[1]:
                                                print('\nXY wing discovered')
                                                print('xy index is ' + str(xy_index) + ', cell content ' + str(x) + str(
                                                    y))

                                                print('Z1 index is ' + str(int(''.join(z_index_list_first_entry_sep)))
                                                      + ', cell content ' + str(
                                                    z_both_numbers_list[check_number_1]))
                                                print('Z2 index is ' + str(int(''.join(
                                                    z_index_list_second_entry_sep))) + ', cell content ' + str(
                                                    z_both_numbers_list[check_number_1 + check_number_2]))
                                                print('Eliminate Z_Value ' + str(z_list[check_number_1]) +
                                                      ' in all buddy cells to both Z1 and Z2')

        #  START ON XYZ WING
        # all variables now have CAPITALS
        # if first cell indeed has 3 entries, it can be X, Y, Z: you don't know which one is Z till check on Z1 and Z2
        if len(buddy_series_unique.iloc[0]) == 3:
            first_number = buddy_series_unique.iloc[0][0]
            second_number = buddy_series_unique.iloc[0][1]
            third_number = buddy_series_unique.iloc[0][2]
            XYZ_index = buddy_series_unique.index[0]
            Z_list = []  # Z_cell, don't know yet which (Z) in other Z_cell, so both nrs added in separate
            Z_index_list = []

            # for all potential Z_cells in list (not first entry, because that is XYZ_cell, so range (1 to 21)
            for potential_Z in range(1, 21):
                if len(buddy_series_unique.iloc[potential_Z]) == 2:  # check _cells has 2 entries
                    if (first_number in buddy_series_unique.iloc[potential_Z]) and (
                            second_number in buddy_series_unique.iloc[potential_Z]) \
                            or (first_number in buddy_series_unique.iloc[potential_Z]) and (
                            third_number in buddy_series_unique.iloc[potential_Z]) \
                            or (second_number in buddy_series_unique.iloc[potential_Z]) and (
                            third_number in buddy_series_unique.iloc[potential_Z]):
                        # make copy of buddy_series_unique, so buddy_s_u not changed if you remove X and Y
                        Z_temp = buddy_series_unique.iloc[potential_Z].copy()
                        Z_list = Z_list + [Z_temp]  # still separated '7' '8' to do check
                        Z_index_temp = [buddy_series_unique.index[potential_Z]]  # get cell index of z
                        Z_index_list = Z_index_list + Z_index_temp

            # MAKE ALL POSSIBLE COMBINATIONS OF Z POTENTIALS
            number_candidates_XYZ = len(Z_list)
            if len(Z_list) > 1:  # make sure at least 2 Z_candidates
                for check_number_1 in range(number_candidates_XYZ - 1):
                    for check_number_2 in range(1, number_candidates_XYZ):
                        if check_number_1 + check_number_2 <= number_candidates_XYZ - 1:
                            if Z_list[check_number_1] != Z_list[check_number_1 + check_number_2]:
                                print(' z list')
                                print(Z_list[check_number_1])
                                print(Z_list[check_number_1 + check_number_2])
                                if (Z_list[0][0]) in Z_list[1]:
                                    print("\nZYZ wing discovered")
                                    print('XYZ index is ' + str(XYZ_index) + ', cell content ' + str(
                                        list(first_number + second_number + third_number)))
                                    print('Z_1 index is ' + str(Z_index_list[0]) + ', cell content ' + str(Z_list[0]))
                                    print('Z_2 index is ' + str(Z_index_list[1]) + ', cell content ' + str(Z_list[1]))
                                    print('Eliminate ' + str(Z_list[0][0]) + ' in all buddy cells to both Z_1 and Z_2')
                                else:
                                    print("\nXYZ wing discovered")
                                    print('XYZ index is ' + str(XYZ_index) + ', cell content ' + str(
                                        list(first_number + second_number + third_number)))
                                    print('Z_1 index is ' + str(Z_index_list[0]) + ' cell content ' + str(Z_list[0]))
                                    print('Z_2 index is ' + str(Z_index_list[1]) + ' cell content ' + str(Z_list[1]))
                                    print('Eliminate ' + str(Z_list[0][1]) + ' in all buddy cells to both Z_1 and Z_2')
