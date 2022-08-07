
import numpy as np
import pandas as pd
import sys
from parameters import *
from function_multiple_choice import *

# import SDK with empty cells, call function to fill in with all possible candidates and then import this Excel sheet
df_temp = pd.read_excel(io='data/SDK.xlsx', sheet_name='python')

multiple_choice(df_temp)

df = pd.read_excel(io='data/SDK_temp_all_candidates.xlsx', sheet_name='python')


# Squirmbag requires all cells be filled with final numbers or all possible candidates
check_nan_in_df = df.isnull().values.any()
if check_nan_in_df:
    print('sorry, not all cells contain a number or candidates')
    sys.exit()
else:
    print('All cells contain either a number or candidates')


# # Dataframe, which only shows cell with multiple possible entries.
# df[df < 10] = 0


def mlist(n):
    for _ in range(n):
        yield []


def print_board(bo):
    print('         A B C    D E F    G H I')
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j == 0:
                print('row ' + str(i + 1) + '    ', end="")

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

for q in range(1, 10):     # (6, 7) (1, 10)
    check_number = str(q)
    check_number_int = q

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

        if check_number in cell_[i]:
            result = str(check_number)
        else:
            result = '.'
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

    # # If in first column '....', then only  '.' is shown, breaking the symmetry in the console
    # for i in range(len(sudoku_pattern)):
    #     if sudoku_pattern[i][0] == '....':
    #         sudoku_pattern[i][0] = ',...'
    print('\n')
    print_board(sudoku_pattern)
    # print('\n')

    # start code to get pattern into integers and into DataFrame
    # first in a list of 81 cells
    # may be multiple numbers to combine, so first combine strings and then make integer
    cell_int_ = {}
    sdk_int = list(mlist(81))

    i = 0
    for k in range(81):
        i += 1
        cell_int_[i] = list(str(int(list_of_lists_81[i - 1][[0][0]])))

        if check_number in cell_int_[i]:
            result_str = check_number
            result = int(result_str)
        else:
            result = ""
        sdk_int[i - 1].append(result)

    # convert to list of list, with each ROW in a list within the list
    sudoku_pattern_int = list(mlist(9))
    sudoku_pattern_int[0] = sdk_int[0] + sdk_int[1] + sdk_int[2] + sdk_int[3] + sdk_int[4] + sdk_int[5] + sdk_int[6] + \
                            sdk_int[7] + sdk_int[8]
    sudoku_pattern_int[1] = sdk_int[9] + sdk_int[10] + sdk_int[11] + sdk_int[12] + sdk_int[13] + sdk_int[14] + sdk_int[15] + \
                            sdk_int[16] + sdk_int[17]
    sudoku_pattern_int[2] = sdk_int[18] + sdk_int[19] + sdk_int[20] + sdk_int[21] + sdk_int[22] + sdk_int[23] + sdk_int[
        24] + sdk_int[25] + sdk_int[26]
    sudoku_pattern_int[3] = sdk_int[27] + sdk_int[28] + sdk_int[29] + sdk_int[30] + sdk_int[31] + sdk_int[32] + sdk_int[
        33] + sdk_int[34] + sdk_int[35]
    sudoku_pattern_int[4] = sdk_int[36] + sdk_int[37] + sdk_int[38] + sdk_int[39] + sdk_int[40] + sdk_int[41] + sdk_int[
        42] + sdk_int[43] + sdk_int[44]
    sudoku_pattern_int[5] = sdk_int[45] + sdk_int[46] + sdk_int[47] + sdk_int[48] + sdk_int[49] + sdk_int[50] + sdk_int[
        51] + sdk_int[52] + sdk_int[53]
    sudoku_pattern_int[6] = sdk_int[54] + sdk_int[55] + sdk_int[56] + sdk_int[57] + sdk_int[58] + sdk_int[59] + sdk_int[
        60] + sdk_int[61] + sdk_int[62]
    sudoku_pattern_int[7] = sdk_int[63] + sdk_int[64] + sdk_int[65] + sdk_int[66] + sdk_int[67] + sdk_int[68] + sdk_int[
        69] + sdk_int[70] + sdk_int[71]
    sudoku_pattern_int[8] = sdk_int[72] + sdk_int[73] + sdk_int[74] + sdk_int[75] + sdk_int[76] + sdk_int[77] + sdk_int[
        78] + sdk_int[79] + sdk_int[80]

    # Create Dataframe, similar to sudoku in console. In dataframe analysis for patterns with only check_numbers shown
    df_sudoku = pd.DataFrame(sudoku_pattern_int, index=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    df_sudoku.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    # START PATTERN ANALYSIS

    # Use only cells with multiple entries that include check_number
    # if cell only contains check_number, then cell is already completed with final number, so further analysis needed

    # Create list with for each ROW find the COLUMN index for entry of check_number (with cells with multiple entries)
    col_index_row_1 = (np.where(df_sudoku.iloc[0].eq(check_number_int))[0] + 1).tolist()
    col_index_row_2 = (np.where(df_sudoku.iloc[1].eq(check_number_int))[0] + 1).tolist()
    col_index_row_3 = (np.where(df_sudoku.iloc[2].eq(check_number_int))[0] + 1).tolist()
    col_index_row_4 = (np.where(df_sudoku.iloc[3].eq(check_number_int))[0] + 1).tolist()
    col_index_row_5 = (np.where(df_sudoku.iloc[4].eq(check_number_int))[0] + 1).tolist()
    col_index_row_6 = (np.where(df_sudoku.iloc[5].eq(check_number_int))[0] + 1).tolist()
    col_index_row_7 = (np.where(df_sudoku.iloc[6].eq(check_number_int))[0] + 1).tolist()
    col_index_row_8 = (np.where(df_sudoku.iloc[7].eq(check_number_int))[0] + 1).tolist()
    col_index_row_9 = (np.where(df_sudoku.iloc[8].eq(check_number_int))[0] + 1).tolist()

    # Create list with for each COLUMN find the ROW index for entry of check_number (with cells with multiple entries)
    row_index_column_1 = (np.where(df_sudoku.loc[:, 'A'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_2 = (np.where(df_sudoku.loc[:, 'B'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_3 = (np.where(df_sudoku.loc[:, 'C'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_4 = (np.where(df_sudoku.loc[:, 'D'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_5 = (np.where(df_sudoku.loc[:, 'E'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_6 = (np.where(df_sudoku.loc[:, 'F'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_7 = (np.where(df_sudoku.loc[:, 'G'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_8 = (np.where(df_sudoku.loc[:, 'H'].eq(check_number_int))[0] + 1).tolist()
    row_index_column_9 = (np.where(df_sudoku.loc[:, 'I'].eq(check_number_int))[0] + 1).tolist()

    # SQUIRMBAG

    # SQUIRMBAG_ROW:
    # start with ROWS (and eliminate on columns)
    # start with identifying ROWS: check if there are 5 ROWS, where check_number is in max 5 cells (often 2/3/4 per row)
    # Then see if these cells are in 5 COLUMNS ==> ID SO : SQUIRMABG
    # ACTION: ELIMINATE all check-number in COLUMNS that are not in 5 identified rows

    # Check if within a ROW, check_number_1 is present 2, 3, 4 or 5 times.
    # if so, add COLUMN index for that row to squirmbag_row list
    # So squirmbag_row is list of list, where each list within list contains COLUMN index if 2,3,4,5 entries in that row
    # to later identify ROW number in case of Squirmbag, row numbers are added to [record row number] if 2,3,4,5 entries

    squirmbag_row = []
    record_row_number = []
    if len(col_index_row_1) == 1 or len(col_index_row_1) == 2 or len(col_index_row_1) == 3 or len(col_index_row_1) == 4 or len(col_index_row_1) == 5:
        squirmbag_row.append(col_index_row_1)
        record_row_number.append('row 1')
    if len(col_index_row_2) == 1 or len(col_index_row_2) == 2 or len(col_index_row_2) == 3 or len(col_index_row_2) == 4 or len(col_index_row_2) == 5:
        squirmbag_row.append(col_index_row_2)
        record_row_number.append('row 2')
    if len(col_index_row_3) == 1 or len(col_index_row_3) == 2 or len(col_index_row_3) == 3 or len(col_index_row_3) == 4 or len(col_index_row_3) == 5:
        squirmbag_row.append(col_index_row_3)
        record_row_number.append('row 3')
    if len(col_index_row_4) == 1 or len(col_index_row_4) == 2 or len(col_index_row_4) == 3 or len(col_index_row_4) == 4 or len(col_index_row_4) == 5:
        squirmbag_row.append(col_index_row_4)
        record_row_number.append('row 4')
    if len(col_index_row_5) == 1 or len(col_index_row_5) == 2 or len(col_index_row_5) == 3 or len(col_index_row_5) == 4 or len(col_index_row_5) == 5:
        squirmbag_row.append(col_index_row_5)
        record_row_number.append('row 5')
    if len(col_index_row_6) == 1 or len(col_index_row_6) == 2 or len(col_index_row_6) == 3 or len(col_index_row_6) == 4 or len(col_index_row_6) == 5:
        squirmbag_row.append(col_index_row_6)
        record_row_number.append('row 6')
    if len(col_index_row_7) == 1 or len(col_index_row_7) == 2 or len(col_index_row_7) == 3 or len(col_index_row_7) == 4 or len(col_index_row_7) == 5:
        squirmbag_row.append(col_index_row_7)
        record_row_number.append('row 7')
    if len(col_index_row_8) == 1 or len(col_index_row_8) == 2 or len(col_index_row_8) == 3 or len(col_index_row_8) == 4 or len(col_index_row_8) == 5:
        squirmbag_row.append(col_index_row_8)
        record_row_number.append('row 8')
    if len(col_index_row_9) == 1 or len(col_index_row_9) == 2 or len(col_index_row_9) == 3 or len(col_index_row_9) == 4 or len(col_index_row_9) == 5:
        squirmbag_row.append(col_index_row_9)
        record_row_number.append('row 9')

    # List [squirmbag_row] contains list of column index for each row with 2, 3, 4 entries for check_number
    # List [swordfish_row_comb_4] is temporary list of all possible combinations of 4 rows
    # This temporary list is used to check if Swordfish: if not true, create new tem list
    for i in range(len(squirmbag_row)):
        for j in range(i + 1, len(squirmbag_row)):
            for k in range(j + 1, len(squirmbag_row)):
                for l in range(k + 1, len(squirmbag_row)):
                    for m in range(l + 1, len(squirmbag_row)):
                        squirmbag_row_comb_5 = [squirmbag_row[i]]
                        squirmbag_row_comb_5 = squirmbag_row_comb_5 + [squirmbag_row[j]]
                        squirmbag_row_comb_5 = squirmbag_row_comb_5 + [squirmbag_row[k]]
                        squirmbag_row_comb_5 = squirmbag_row_comb_5 + [squirmbag_row[l]]
                        squirmbag_row_comb_5 = squirmbag_row_comb_5 + [squirmbag_row[m]]
                        squirmbag_flat = [item for sublist in squirmbag_row_comb_5 for item in sublist]
                        squirmbag_number = len(set(squirmbag_flat))

                        if squirmbag_number == 5:
                            print('\nSQUIRMBAG_row detected for number ' + check_number)
                            print('in ' + str(record_row_number[i]) + ', ' + str(record_row_number[j]) + ', ' + str(
                                record_row_number[k]) + ', ' + str(record_row_number[l]) + ', ' +
                                  str(record_row_number[m]))
                            non_eliminate_list = []
                            non_eliminate_list = [[int(record_row_number[i][-1])] + [int(record_row_number[j][-1])] +
                                                  [int(record_row_number[k][-1])] + [int(record_row_number[l][-1])] +
                                                  [int(record_row_number[m][-1])]]
                            non_eliminate_list = [x for xs in non_eliminate_list for x in xs]

                            columns_with_squirmbag = []
                            for c in squirmbag_flat:
                                if c not in columns_with_squirmbag:
                                    columns_with_squirmbag.append(c)

                            columns_with_squirmbag.sort()
                            """
                            print('Eliminate (in COLUMNS) number ' + check_number + ' in other rows in the columns:')
                            for a in range(len(columns_with_squirmbag)):
                                print(convert_to_column_letter[columns_with_squirmbag[a]])
                            """

                            for y in columns_with_squirmbag:
                                eliminate_candidates = []
                                for r in range(9):
                                    # if df_sudoku['B'].iloc[r] == 6:
                                    if df_sudoku.iloc[r, y - 1] == check_number_int:
                                        eliminate_candidates = eliminate_candidates + [r + 1]

                                delete_list = []
                                for u in eliminate_candidates:
                                    if u not in non_eliminate_list:
                                        delete_list = delete_list + [u]

                                if len(delete_list) > 0:
                                    print('In column ' + str(convert_to_column_letter[y]) + ' delete row(s) ' + str(delete_list))


    # SQUIRMBAG_COLUMNS:
    # start with COLUMNS (and eliminate on rows)
    # start with identifying COLUMNS: check if there are 5 COLUMNS, where check_number is in max 5 cells(often just 3,4)
    # Then see if these cells are in 5 ROWS ==> ID SO : SQUIRMBAG
    # ACTION: ELIMINATE all check-number in ROWS that are not in 5 identified columns


    # SQUIRMBAG_columns: more detail
    # Check if within a COLUMN, check_number_1 is present 2, 3, 4 or 5 times.
    # if so, add ROW index for that column to squirmbag_column list
    # So squirmbag_column is list of list, where each list within list contains ROW index if 2,3,4,5 entries in column
    # to later identify COLUMN number if Squirmbag, column numbers are added to [record column number]if 2/3/4/5 entries

    squirmbag_column = []
    record_column_number = []
    if len(row_index_column_1) == 1 or len(row_index_column_1) == 2 or len(row_index_column_1) == 3 or len(row_index_column_1) == 4 or len(row_index_column_1) == 5:
        squirmbag_column.append(row_index_column_1)
        record_column_number.append('column A')
    if len(row_index_column_2) == 1 or len(row_index_column_2) == 2 or len(row_index_column_2) == 3 or len(row_index_column_2) == 4 or len(row_index_column_2) == 5:
        squirmbag_column.append(row_index_column_2)
        record_column_number.append('column B')
    if len(row_index_column_3) == 1 or len(row_index_column_3) == 2 or len(row_index_column_3) == 3 or len(row_index_column_3) == 4 or len(row_index_column_3) == 5:
        squirmbag_column.append(row_index_column_3)
        record_column_number.append('column C')
    if len(row_index_column_4) == 1 or len(row_index_column_4) == 2 or len(row_index_column_4) == 3 or len(row_index_column_4) == 4 or len(row_index_column_4) == 5:
        squirmbag_column.append(row_index_column_4)
        record_column_number.append('column D')
    if len(row_index_column_5) == 1 or len(row_index_column_5) == 2 or len(row_index_column_5) == 3 or len(row_index_column_5) == 4 or len(row_index_column_5) == 5:
        squirmbag_column.append(row_index_column_5)
        record_column_number.append('column E')
    if len(row_index_column_6) == 1 or len(row_index_column_6) == 2 or len(row_index_column_6) == 3 or len(row_index_column_6) == 4 or len(row_index_column_6) == 5:
        squirmbag_column.append(row_index_column_6)
        record_column_number.append('column F')
    if len(row_index_column_7) == 1 or len(row_index_column_7) == 2 or len(row_index_column_7) == 3 or len(row_index_column_7) == 4 or len(row_index_column_7) == 5:
        squirmbag_column.append(row_index_column_7)
        record_column_number.append('column G')
    if len(row_index_column_8) == 1 or len(row_index_column_8) == 2 or len(row_index_column_8) == 3 or len(row_index_column_8) == 4 or len(row_index_column_8) == 5:
        squirmbag_column.append(row_index_column_8)
        record_column_number.append('column H')
    if len(row_index_column_9) == 1 or len(row_index_column_9) == 2 or len(row_index_column_9) == 3 or len(row_index_column_9) == 4 or len(row_index_column_9) == 5:
        squirmbag_column.append(row_index_column_9)
        record_column_number.append('column I')

    # List [squirmbag_column] contains list of row index for each column with 2,3, 4, 5 entries for check_number
    # List [squirmbag_column_comb_5] is temporary list of all possible combinations of 5 columns
    # This temporary list is used to check if Squirmbag: if not true, create new tem list,
    for i in range(len(squirmbag_column)):
        for j in range(i + 1, len(squirmbag_column)):
            for k in range(j + 1, len(squirmbag_column)):
                for l in range(k + 1, len(squirmbag_column)):
                    for m in range(l + 1, len(squirmbag_column)):
                        squirmbag_column_comb_5 = [squirmbag_column[i]]
                        squirmbag_column_comb_5 = squirmbag_column_comb_5 + [squirmbag_column[j]]
                        squirmbag_column_comb_5 = squirmbag_column_comb_5 + [squirmbag_column[k]]
                        squirmbag_column_comb_5 = squirmbag_column_comb_5 + [squirmbag_column[l]]
                        squirmbag_column_comb_5 = squirmbag_column_comb_5 + [squirmbag_column[m]]
                        squirmbag_column_flat = [item for sublist in squirmbag_column_comb_5 for item in sublist]
                        squirmbag_column_number = len(set(squirmbag_column_flat))

                        if squirmbag_column_number == 5:
                            print('\nSQUIRMBAG_column detected for number ' + check_number)
                            print('in ' + str(record_column_number[i]) + ', ' + str(record_column_number[j]) + ', '
                                  + str(record_column_number[k]) + ', ' + str(record_column_number[l]) + ', ' +
                                  str(record_column_number[m]))
                            non_eliminate_list_column = []
                            non_eliminate_list_column = [[(record_column_number[i][-1])] + [(record_column_number[j][-1])] +
                                                         [(record_column_number[k][-1])] + [(record_column_number[l][-1])]
                                                         + [(record_column_number[m][-1])]]
                            non_eliminate_list_column = [x for xs in non_eliminate_list_column for x in xs]

                            rows_with_squirmbag = []
                            for c in squirmbag_column_flat:
                                if c not in rows_with_squirmbag:
                                    rows_with_squirmbag.append(c)

                            rows_with_squirmbag.sort()
                            """
                            print('Eliminate (in ROWS) number ' + check_number + ' in other columns in the rows:')
                            print(rows_with_squirmbag)
                            print('\n')
                            """

                            for row in rows_with_squirmbag:
                                eliminate_candidates = []
                                for col in range(9):
                                    # if df_sudoku['B'].iloc[r] == 6:
                                    if df_sudoku.iloc[row - 1, col] == check_number_int:
                                        eliminate_candidates = eliminate_candidates + [col + 1]

                                    eliminate_candidates_letter = []
                                    for e in range(len(eliminate_candidates)):
                                        eliminate_candidates_letter = eliminate_candidates_letter + [convert_to_column_letter[eliminate_candidates[e]]]

                                delete_list = []
                                for u in eliminate_candidates_letter:
                                    if u not in non_eliminate_list_column:
                                        delete_list = delete_list + [u]

                                if len(delete_list) > 0:
                                    print('In row ' + str(row) + ' delete column(s) ' + str(delete_list))
