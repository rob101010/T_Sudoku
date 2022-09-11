
import pandas as pd
import numpy as np
import sys
from functions.parameters import convert_to_column_letter
from functions.parameters import empty_cells
from functions.function_multiple_choice import multiple_choice

sys.path.append('/home/rob/PycharmProjects/sudoku/functions')

while True:
    empty_cell = input('choose 1 in case you allow empty cells and 2 if program must fill all empty cells')
    if empty_cell not in empty_cells.keys():
        print('please select 1 if you allow empty cells or 2 if program must fill empty cells')
    else:
        break

multiple_choice()


file = empty_cell


if file == '1':
    print('\nit is allowed to have empty cells')
    column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
    df = df.iloc[:9, :9]
    df_show = df.copy()  # only to see Dataframe in PyCharm with rows index 1 to 9
    df_show.index += 1
    df.fillna(0, inplace=True)

else:
    print('empty cells are filled with all possible candidates')
    df = pd.read_excel(io='data/SDK_output_function_all_candidates.xlsx', sheet_name='python', index_col=False)
    df = df.iloc[:, 1:10]
    df_show = df.copy()  # only to see Dataframe in PyCharm with rows index 1 to 9
    df_show.index += 1




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

for q in range(1, 10):    # (1, 10) (7, 8)
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

    # X_WING

    # X-WING_ROW:
    # start with ROWS (and eliminate on columns)
    # start with identifying ROWS: check if there are 2 ROWS, where check_number is in
    # Then see if these cells are in 2 COLUMNS ==> ID SO : X-Wing
    # ACTION: ELIMINATE all check-number in COLUMNS that are not in 2 identified rows

    # Check if within a ROW, check_number is present 2.
    # if so, add COLUMN index for that row to x-wing_row list
    # So X-wing_row is list of list, where each list within list contains COLUMN index if of 2 entries in that row
    # to later identify ROW number in case of Swordfish, row numbers are added to [record row number] in case 2 entries

    xwing_row = []
    record_row_number = []
    if len(col_index_row_1) == 2:
        xwing_row.append(col_index_row_1)
        record_row_number.append('row 1')
    if len(col_index_row_2) == 2:
        xwing_row.append(col_index_row_2)
        record_row_number.append('row 2')
    if len(col_index_row_3) == 2:
        xwing_row.append(col_index_row_3)
        record_row_number.append('row 3')
    if len(col_index_row_4) == 2:
        xwing_row.append(col_index_row_4)
        record_row_number.append('row 4')
    if len(col_index_row_5) == 2:
        xwing_row.append(col_index_row_5)
        record_row_number.append('row 5')
    if len(col_index_row_6) == 2:
        xwing_row.append(col_index_row_6)
        record_row_number.append('row 6')
    if len(col_index_row_7) == 2:
        xwing_row.append(col_index_row_7)
        record_row_number.append('row 7')
    if len(col_index_row_8) == 2:
        xwing_row.append(col_index_row_8)
        record_row_number.append('row 8')
    if len(col_index_row_9) == 2:
        xwing_row.append(col_index_row_9)
        record_row_number.append('row 9')

    # List [xwing_row] contains list of column index for each row with 2 entries for check_number
    # List [xwing_row_comb_2] is temporary list of all possible combinations of 2 rows
    # This temporary list is used to check if XWING: if not true, create new tem list
    for i in range(len(xwing_row)):
        for j in range(i + 1, len(xwing_row)):
            xwing_row_comb_2 = [xwing_row[i]]
            xwing_row_comb_2 = xwing_row_comb_2 + [xwing_row[j]]
            xwing_flat = [item for sublist in xwing_row_comb_2 for item in sublist]
            xwing_number = len(set(xwing_flat))

            if xwing_number == 2:
                non_eliminate_list = []
                non_eliminate_list = [[int(record_row_number[i][-1])] + [int(record_row_number[j][-1])]]
                non_eliminate_list = [x for xs in non_eliminate_list for x in xs]

                columns_with_xwing = []
                for c in xwing_flat:
                    if c not in columns_with_xwing:
                        columns_with_xwing.append(c)

                columns_with_xwing.sort()
                """
                print('\nEliminate (in COLUMNS) number ' + check_number + ' in other rows in the columns:')
                for a in range(len(columns_with_xwing)):
                    print(convert_to_column_letter[columns_with_xwing[a]])
                """
                for y in columns_with_xwing:
                    eliminate_candidates = []
                    for r in range(9):
                        if df_sudoku.iloc[r, y - 1] == check_number_int:  # y-1 because column_with_swordfish has column B as 2
                            eliminate_candidates = eliminate_candidates + [r + 1]

                    delete_list_2 = []
                    for u in eliminate_candidates:
                        if u not in non_eliminate_list:
                            delete_list_2 = delete_list_2 + [u]

                    if len(delete_list_2) > 0:
                        print('\nX-WING_row detected for number ' + check_number)
                        print('in ' + str(record_row_number[i]) + ' ' + str(record_row_number[j]))
                        print('In column ' + str(convert_to_column_letter[y]) + ' delete row(s) ' + str(delete_list_2))


    # X_WINGS_COLUMNS:
    # start with COLUMNS (and eliminate on rows)
    # start with identifying COLUMNS: check if there are 2 COLUMNS, where check_number is in 2 cells
    # Then see if these cells are in 2 ROWS ==> ID SO : X-WING
    # ACTION: ELIMINATE all check-number in ROWS that are not in 2 identified columns


    # X-WING_columns: more detail
    # Check if within a COLUMN, check_number_1 is present 2 times.
    # if so, add ROW index for that column to xwing_column list
    # So xwing_column is list of list, where each list within list contains ROW index if 2 entries in that column
    # to later identify COLUMN number if X-WING, column numbers are added to [record column number] if 2 entries


    xwing_column = []
    record_column_number = []
    if len(row_index_column_1) == 2:
        xwing_column.append(row_index_column_1)
        record_column_number.append('column A')
    if len(row_index_column_2) == 2:
        xwing_column.append(row_index_column_2)
        record_column_number.append('column B')
    if len(row_index_column_3) == 2:
        xwing_column.append(row_index_column_3)
        record_column_number.append('column C')
    if len(row_index_column_4) == 2:
        xwing_column.append(row_index_column_4)
        record_column_number.append('column D')
    if len(row_index_column_5) == 2:
        xwing_column.append(row_index_column_5)
        record_column_number.append('column E')
    if len(row_index_column_6) == 2:
        xwing_column.append(row_index_column_6)
        record_column_number.append('column F')
    if len(row_index_column_7) == 2:
        xwing_column.append(row_index_column_7)
        record_column_number.append('column G')
    if len(row_index_column_8) == 2:
        xwing_column.append(row_index_column_8)
        record_column_number.append('column H')
    if len(row_index_column_9) == 2:
        xwing_column.append(row_index_column_9)
        record_column_number.append('column I')

    # List [xwing_column] contains list of row index for each column with 2 entries for check_number
    # List [xwing_column_comb_2] is temporary list of all possible combinations of 2 columns
    # This temporary list is used to check if Swordfish: if not true, create new tem list,
    for i in range(len(xwing_column)):
        for j in range(i + 1, len(xwing_column)):
            xwing_column_comb_2 = [xwing_column[i]]
            xwing_column_comb_2 = xwing_column_comb_2 + [xwing_column[j]]
            xwing_column_flat = [item for sublist in xwing_column_comb_2 for item in sublist]
            xwing_column_number = len(set(xwing_column_flat))

            if xwing_column_number == 2:
                non_eliminate_list_column = []
                non_eliminate_list_column = [[(record_column_number[i][-1])] + [(record_column_number[j][-1])]]
                non_eliminate_list_column = [x for xs in non_eliminate_list_column for x in xs]

                rows_with_xwing = []
                for c in xwing_column_flat:
                    if c not in rows_with_xwing:
                        rows_with_xwing.append(c)

                rows_with_xwing.sort()
                """
                print('\nEliminate (in ROWS) number ' + check_number + ' in other columns in the rows:')
                print(rows_with_xwing)
                print('\n')
                """

                for row in rows_with_xwing:
                    eliminate_candidates = []
                    for col in range(9):
                        if df_sudoku.iloc[row - 1, col] == check_number_int:  # CHECK NUMBER!!!!!
                            eliminate_candidates = eliminate_candidates + [col + 1]

                        eliminate_candidates_letter = []
                        for e in range(len(eliminate_candidates)):
                            eliminate_candidates_letter = eliminate_candidates_letter + [
                                convert_to_column_letter[eliminate_candidates[e]]]

                    delete_list = []
                    for u in eliminate_candidates_letter:
                        if u not in non_eliminate_list_column:
                            delete_list = delete_list + [u]
                    if len(delete_list) > 0:
                        print('\nX-WING_column detected for number ' + check_number)
                        print('in ' + str(record_column_number[i]) + ' ' + str(record_column_number[j]))
                        print('In row ' + str(row) + ' delete column(s) ' + str(delete_list))
