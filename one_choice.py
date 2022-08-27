"""
For every empty cell make list of all numbers in the column, row & box
Check if in total list (sum of col, row & box) just 1 unique number missing ==> one_choice
"""


import pandas as pd

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False)
df = df.iloc[:9, :9]
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    for j in range(9):
        column_filled = []
        row_filled = []
        column_row_filled = []
        box_filled = []
        if pd.isnull(df.iloc[i, j]):
            column_filled = df.iloc[:, j]
            row_filled = df.iloc[i, :]
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
                    box_filled = box_filled + [df.iloc[row_box, column_box]]

            for k in range(9):
                column_row_filled = column_row_filled + [column_filled[k]] + [row_filled[k]]

            total_filled = [column_row_filled] + [box_filled]
            total_filled_flat = [item for sublist in total_filled for item in sublist]

            missing_numbers = []
            for m in all_numbers:
                if m not in total_filled_flat:
                    missing_numbers = missing_numbers + [m]

        if pd.isnull(df.iloc[i, j]):
            if len(missing_numbers) < 2:
                print('one_choice fill in cell ' + str(i + 1) + str(j + 1) + ' fill in ' + str(missing_numbers))
