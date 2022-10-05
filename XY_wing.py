#  in printing change column 2 to column B (e.g.)
import pandas as pd

column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False, names=column_names)
df = df.iloc[:9, :9]
df.index += 1
df = df.fillna(999999)  # to avoid nan,which makes string type impossible: must be 6'9', so exclude them from quintuplet
df_str = df.astype(str)   # str is used later to be able to separate 126 in a cell into '1', '2' and '6'

# convert df to new df in which each BOX is added as a row
df_box = df.astype(int)

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


for row in range(1):
    for column in range(1):
        buddy_series = pd.Series(['1'], index=[0])    # make sure to delete this first entry in Series
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

        buddy_series = buddy_series.append(box_series_1)
        buddy_series = buddy_series.drop(labels=[0])
        index = buddy_series.index
        buddy_series_unique = buddy_series[~index.duplicated(keep='first')]
