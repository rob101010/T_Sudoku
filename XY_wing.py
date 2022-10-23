import pandas as pd

column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
df = df.iloc[:9, :9]
df.index += 1
df = df.fillna(999999)  # to avoid nan,which makes string type impossible: must be 6'9', so exclude them from quintuplet
df_str = df.astype(str)   # str is used later to be able to separate 126 in a cell into '1', '2' and '6'


# next 3 rows ar not needed anymore I guess
# convert df to new df in which each BOX is added as a row
# df_box = df.astype(int)
# Create new DataFrame df_box, in which each box is converted to a row


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
for row_box in range(6, 9):
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


for row in range(6, 7):   # range  (6, 7)
    for column in range(6, 7):  # range  (6, 7)
        cell_start_row_column_index = str(row + 1) + str(column + 1)  # row_column cell is pot. XY ==> top buddy list
        cell_start_row_column = df_str.iloc[row, column]
        cell_start_row_column_sep = list(cell_start_row_column)
        buddy_series = pd.Series([cell_start_row_column_sep], index=[int(cell_start_row_column_index)])
        for i in range(9):
            cell_index = str(row + 1) + str(i + 1)
            cell = df_str.iloc[row, i]              # loop through each cell in column
            cell_sep = list(cell)                   # each double number as 2 separate numbers in string (26 = '2','6')
            series_temp = pd.Series([cell_sep], index=[int(cell_index)])
            buddy_series = buddy_series.append(series_temp)
        for j in range(9):
            cell_index = str(j + 1) + str(column + 1)
            cell = df_str.iloc[j, column]           # loop through each cell in row
            cell_sep = list(cell)
            series_temp = pd.Series([cell_sep], index=[int(cell_index)])
            buddy_series = buddy_series.append(series_temp)

        buddy_series = buddy_series.append(box_series_9)   # Add box to buddy_list.MAKE BOX VARIABLE FOR ROW AND COLUMN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        index = buddy_series.index
        buddy_series_unique = buddy_series[~index.duplicated(keep='first')]


        if len(buddy_series_unique.iloc[0]) == 2:
            x = buddy_series_unique.iloc[0][0]
            y = buddy_series_unique.iloc[0][1]
            xy_index = buddy_series_unique.index[0]
            print('\n\nx is: ' + str(x))
            print('y is: ' + str(y))
            print('xy_index is: ' + str(buddy_series_unique.index[0]))
            print('\n')
            z_list = []
            z_index_list = []
            z_both_numbers_list = []                                                                                           # this list is content of potential z_cells to check not same other z_cell
            for potential_Z in range(21):
                if len(buddy_series_unique.iloc[potential_Z]) == 2:                                                            # look for cell with 2 entries (potential z-Cell
                    if buddy_series_unique.iloc[potential_Z] != buddy_series_unique.iloc[0]:                        # exclude z-cell it's a pair with XY
                        if (x in buddy_series_unique.iloc[potential_Z]) or (y in buddy_series_unique.iloc[potential_Z]):       # check if X or Y in Z_cell
                            if xy_index != buddy_series_unique.index[[potential_Z]]:                                           # HOEFT TOCH NIET?? CHECK AL GEDAAN 2 REGELS BOVEN   Helaas ook als x en y erin zitten, dus je moet eigen index eruit halen
                                # print('\nx or y this cell')
                                # print('m for cell with x or y is ' + str(m))
                                print(buddy_series_unique.iloc[potential_Z])
                                z_temp = buddy_series_unique.iloc[potential_Z].copy()   # added copy(), so buddy_s_u not changed > remove
                                z_index_temp = [buddy_series_unique.index[potential_Z]]  # get cell index of z
                                z_concat = str(int(''.join(z_temp)))
                                z_both_numbers_list = z_both_numbers_list + [z_concat]                                        # Content Z_cell, as 1 number, so '7', '8' is now '78': all have 2 entries, with either X or Y and NOT pair with XY
                                # print('z_temp is ' + str(z_temp))
                                # print('z_index_temp is ' + str(z_index_temp))
                                # print('z_concat ' + str(z_concat))
                                if x in z_temp:
                                    # print('x is ' + str(x))
                                    # print('z is ' + str(z_temp))
                                    z_temp.remove(x)
                                    # print('z na remove x ' + str(z_temp))
                                if y in z_temp:
                                    # print('y is ' + str(y))
                                    # print('z is ' + str(z_temp))
                                    z_temp.remove(y)
                                    # print('z na remove y ' + str(z_temp))
                                z_list = z_list + z_temp                                                                    # adds Z- value of each cell. Of course this Z-value must be identical in both cells (to be checked later)
                                z_index_list = z_index_list + z_index_temp                                                  # add cell index of 2nd, third etc.  z-cell to cell index first z cell
                                print('z_list is ' + str(z_list))
                                print('z_index_list ' + str(z_index_list))
                                print('z_both_numbers_list ' + str(z_both_numbers_list))

            print('check on z_both_number_list for all combinations of 2 cells: both cells same Z_value, both buddy with XY and both Z_cells no buddy with each other ')

            number_candidates = len(z_both_numbers_list)                                                                    # determine number of potential Z_cells and then do check on all possible combinations of 2 cells
            for check_number_1 in range(number_candidates - 1):
                for check_number_2 in range(1, number_candidates):
                    if check_number_1 + check_number_2 <= len(z_both_numbers_list) - 1:
                        print('\n')
                        # print(len(z_both_numbers_list))
                        print('check_1 ' + str(check_number_1) + ' content  ' + str(z_both_numbers_list[check_number_1]) + ' in cell ' + str(z_index_list[check_number_1]))
                        print('check_2 ' + str(check_number_1 + check_number_2) + ' content  ' + str(z_both_numbers_list[check_number_1 + check_number_2]) + ' in cell ' + str(z_index_list[check_number_1 + check_number_2]))
                        total_number_of_cells_XY_wing = 0                                                                  # I GUESS THIS IS NO LONGER NEEDED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
                        if z_both_numbers_list[check_number_1] != z_both_numbers_list[check_number_1 + check_number_2]:    # check if 2 z_cells are not a pair
                            if z_list[check_number_1] == z_list[check_number_1 + check_number_2]:                                           # check if 2 potential Z_cells have indeed same z-value
                                xy_index_sep = list(str(xy_index))                                                         # On XY index determine the Row and Column (needed to do buddy check for each Z_cell with XY_cell)
                                z_index_list_first_entry_sep = list(
                                    str((z_index_list[check_number_1])))                                                   # index first cell z, as separate numbers
                                z_index_list_second_entry_sep = list(
                                    str((z_index_list[check_number_1 + check_number_2])))                                               # index second cell z, as separate numbers

                                if (((int(xy_index_sep[0])) - 1) // 3 == (                                                 # buddy check First Z_cell and XY (first check box, then rows, then column)
                                        (int(z_index_list_first_entry_sep[0])) - 1) // 3 and (
                                            (int(xy_index_sep[1])) - 1) // 3 == (
                                            (int(z_index_list_first_entry_sep[1])) - 1) // 3) or (
                                        xy_index_sep[0] == z_index_list_first_entry_sep[0]) or (
                                        xy_index_sep[1] == z_index_list_first_entry_sep[1]):
                                    print('FIRST ENTRY IS BUDDY WITH YX')
                                    total_number_of_cells_XY_wing = total_number_of_cells_XY_wing + 1

                                    if (((int(xy_index_sep[0])) - 1) // 3 == (                                                  # buddy check second Z_cell and XY
                                            (int(z_index_list_second_entry_sep[0])) - 1) // 3 and (
                                                (int(xy_index_sep[1])) - 1) // 3 == (
                                                (int(z_index_list_second_entry_sep[1])) - 1) // 3) or (
                                            xy_index_sep[0] == z_index_list_second_entry_sep[0]) or (
                                            xy_index_sep[1] == z_index_list_second_entry_sep[1]):
                                        print('SECOND ENTRY IS BUDDY WITH YX')
                                        total_number_of_cells_XY_wing = total_number_of_cells_XY_wing + 1

                                        if ((int(z_index_list_first_entry_sep[0])) - 1) // 3 != ((int(z_index_list_second_entry_sep[0])) - 1) // 3 or (((int(z_index_list_first_entry_sep[1])) - 1) // 3 != ((int(z_index_list_second_entry_sep[1])) - 1) // 3):
                                            print('box is different so still possible!')

                                            if (z_index_list_first_entry_sep[0] != z_index_list_second_entry_sep[0]):
                                                print('row is different')

                                                if (z_index_list_first_entry_sep[1] != z_index_list_second_entry_sep[1]):
                                                    print('column is different')
                                                    print('\nXY wing discovered')
                                                    print('xy index is: ' + str(xy_index) + '         with cell content ' + str(x) + str(y))
                                                    print('z1 index is: ' + str(z_index_list_first_entry_sep) + ' with cell content ' + str(z_both_numbers_list[check_number_1]))
                                                    print('z2 index is: ' + str(z_index_list_second_entry_sep) + ' with cell content ' + str(z_both_numbers_list[check_number_1 + check_number_2]))   # second Z is check nr 1 + 2
                                                    print('Remove Z_Value ' + str(z_list[check_number_1]) + ' in all buddy cells of Z1 and Z2')
                                                    print('\n')
