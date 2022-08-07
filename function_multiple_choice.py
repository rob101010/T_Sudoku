"""
Function derived from multiple_choice>_to_excel, ignore printing multiple candidates, use df_temp2
Write output to SDK_temp_all_candidates
"""


import pandas as pd
import numpy as np

def multiple_choice(x):
    df_temp2 = pd.read_excel(io='data/SDK.xlsx', sheet_name='python')

    all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    for i in range(9):
        for j in range(9):
            column_filled = []
            row_filled = []
            column_row_filled = []
            box_filled = []
            if pd.isnull(df_temp2.iloc[i, j]):
                column_filled = df_temp2.iloc[:, j]
                row_filled = df_temp2.iloc[i, :]
                if i // 3 == 0:
                    r_low = 0
                    r_high = 3
                if i // 3 == 1:
                    r_low = 3
                    r_high = 6
                if i // 3 == 2:
                    r_low = 6
                    r_high = 9

                if j // 3 == 0:
                    c_low = 0
                    c_high = 3
                if j // 3 == 1:
                    c_low = 3
                    c_high = 6
                if j // 3 == 2:
                    c_low = 6
                    c_high = 9

                for row_box in range(r_low, r_high):
                    for column_box in range(c_low, c_high):
                        box_filled = box_filled + [df_temp2.iloc[row_box, column_box]]

                for k in range(9):
                    column_row_filled = column_row_filled + [column_filled[k]] + [row_filled[k]]

                total_filled = [column_row_filled] + [box_filled]
                total_filled_flat = [item for sublist in total_filled for item in sublist]

                missing_numbers = []
                for m in all_numbers:
                    if m not in total_filled_flat:
                        missing_numbers = missing_numbers + [m]
                # put all individual digits in string, so 1, 7, 8 becomes '178' and then int 178
                missing_numbers_string = ''.join(str(e) for e in missing_numbers)
                missing_numbers_int = int(missing_numbers_string)

            if pd.isnull(df_temp2.iloc[i, j]):
                if len(missing_numbers) > 0:
                    df_temp2.iloc[i, j] = missing_numbers_int

    # convert DataFrame from float to integer
    for i in range(9):
        df_temp2.iloc[:, i] = df_temp2.iloc[:, i].apply(np.int64)

    # save to Excel
    writer = pd.ExcelWriter('/home/rob/PycharmProjects/sudoku/data/SDK_temp_all_candidates.xlsx')
    df_temp2.to_excel(writer, sheet_name='python', index=False)
    writer.save()
