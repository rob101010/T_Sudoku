
import pandas as pd

df = pd.read_excel(io='data/SDK.xlsx', sheet_name='python', header=None, index_col=False)
df = df.iloc[:9, :9]
df = df.fillna(999999)  # to avoid nan,which makes string type impossible: must be 6, so exclude them from quintuplet
df_str = df.astype(str)   # str is used later to be able to separate 126 in a cell into '1', '2' and '6'

# convert df to new df in which each BOX is added as a row
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


# For each row create set9_list (list of list) which contains for each cell an inner list with [['1', '2', '6'], [] ]
# for pairs: make set9_list_compare which only include from set9_list cells that have 2 possible candidates
# for triplets include cells with 2 and three candidates, for quadruplets 2, 3 or 4 candidates
# in for final loop: pairs: for each possible combination of 2 cells check if they have only 2 unique candidates
# for triplets use all possible combinations of 3 cells and see if they have 3 unique numbers, etc.


# PAIRS
# Rows
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            x_cells = []
            x_cells = set9_list_compare[i] + set9_list_compare[j]
            unique_candidates = []
            for c in x_cells:
                if c not in unique_candidates:
                    unique_candidates.append(c)
            if len(unique_candidates) == 2:
                # unique_candidates = [int(i) for i in unique_candidates]
                print('in row ' + str(row + 1) + ' pair with numbers ' + str(unique_candidates))

# Pairs columns
for col in range(9):   # row or col
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[i, col]  # (row, col)
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            x_cells = []
            x_cells = set9_list_compare[i] + set9_list_compare[j]
            unique_candidates = []
            for c in x_cells:
                if c not in unique_candidates:
                    unique_candidates.append(c)
            if len(unique_candidates) == 2:
                # unique_candidates = [int(i) for i in unique_candidates]
                print('in column ' + str(col + 1) + ' pair with numbers ' + str(unique_candidates))  # 2x aanpassen

# Pairs boxes
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_box_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            x_cells = []
            x_cells = set9_list_compare[i] + set9_list_compare[j]
            unique_candidates = []
            for c in x_cells:
                if c not in unique_candidates:
                    unique_candidates.append(c)
            if len(unique_candidates) == 2:
                # unique_candidates = [int(i) for i in unique_candidates]
                print('in BOX ' + str(row + 1) + ' pair with numbers ' + str(unique_candidates))


# TRIPLETS
# row
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                x_cells = []
                x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k]
                unique_candidates = []
                for c in x_cells:
                    if c not in unique_candidates:
                        unique_candidates.append(c)
                if len(unique_candidates) == 3:
                    # unique_candidates = [int(i) for i in unique_candidates]
                    print('in row ' + str(row + 1) + ' triplet with numbers ' + str(unique_candidates))

# Triplet column
for col in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[i, col]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                x_cells = []
                x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k]
                unique_candidates = []
                for c in x_cells:
                    if c not in unique_candidates:
                        unique_candidates.append(c)
                if len(unique_candidates) == 3:
                    # unique_candidates = [int(i) for i in unique_candidates]
                    print('in column ' + str(col + 1) + ' triplet with numbers ' + str(unique_candidates))

# Triplets box
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_box_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                x_cells = []
                x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k]
                unique_candidates = []
                for c in x_cells:
                    if c not in unique_candidates:
                        unique_candidates.append(c)
                if len(unique_candidates) == 3:
                    # unique_candidates = [int(i) for i in unique_candidates]
                    print('in BOX ' + str(row + 1) + ' triplet with numbers ' + str(unique_candidates))


# QUADRUPLETS
# rows
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3 or len(set9_list[q]) == 4:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                for l in range(k + 1, len(set9_list_compare)):
                    x_cells = []
                    x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k] + set9_list_compare[l]
                    unique_candidates = []
                    for c in x_cells:
                        if c not in unique_candidates:
                            unique_candidates.append(c)
                    if len(unique_candidates) == 4:
                        # unique_candidates = [int(i) for i in unique_candidates]
                        print('in row ' + str(row + 1) + ' quadruplet with numbers ' + str(unique_candidates))

# Quadruplet columns
for col in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[i, col]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3 or len(set9_list[q]) == 4:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                for l in range(k + 1, len(set9_list_compare)):
                    x_cells = []
                    x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k] + set9_list_compare[l]
                    unique_candidates = []
                    for c in x_cells:
                        if c not in unique_candidates:
                            unique_candidates.append(c)
                    if len(unique_candidates) == 4:
                        # unique_candidates = [int(i) for i in unique_candidates]
                        print('in column ' + str(col + 1) + ' quadruplet with numbers ' + str(unique_candidates))

# Quadruplet box
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_box_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3 or len(set9_list[q]) == 4:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                for l in range(k + 1, len(set9_list_compare)):
                    x_cells = []
                    x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k] + set9_list_compare[l]
                    unique_candidates = []
                    for c in x_cells:
                        if c not in unique_candidates:
                            unique_candidates.append(c)
                    if len(unique_candidates) == 4:
                        # unique_candidates = [int(i) for i in unique_candidates]
                        print('in BOX ' + str(row + 1) + ' quadruplet with numbers ' + str(unique_candidates))


# QUINTUPLETS
# Row
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3 or len(set9_list[q]) == 4 or len(set9_list[q]) == 5:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                for l in range(k + 1, len(set9_list_compare)):
                    for m in range(l + 1, len(set9_list_compare)):
                        x_cells = []
                        x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k] + \
                                  set9_list_compare[l] + set9_list_compare[m]
                        unique_candidates = []
                        for c in x_cells:
                            if c not in unique_candidates:
                                unique_candidates.append(c)
                        if len(unique_candidates) == 5:
                            # unique_candidates = [int(i) for i in unique_candidates]
                            print('in row ' + str(row + 1) + ' quintuplet with numbers ' + str(unique_candidates))

# Quintuplet columns
for col in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_str.iloc[i, col]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3 or len(set9_list[q]) == 4 or len(set9_list[q]) == 5:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                for l in range(k + 1, len(set9_list_compare)):
                    for m in range(l + 1, len(set9_list_compare)):
                        x_cells = []
                        x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k] + \
                                  set9_list_compare[l] + set9_list_compare[m]
                        unique_candidates = []
                        for c in x_cells:
                            if c not in unique_candidates:
                                unique_candidates.append(c)
                        if len(unique_candidates) == 5:
                            # unique_candidates = [int(i) for i in unique_candidates]
                            print('in column ' + str(col + 1) + ' quintuplet with numbers ' + str(unique_candidates))

# Quintuplet box
for row in range(9):
    set9_list = []
    set9_list_compare = []
    for i in range(9):
        cell = df_box_str.iloc[row, i]
        cell_sep = list(cell)
        set9_list = set9_list + [cell_sep]
    for q in range(9):
        if len(set9_list[q]) == 2 or len(set9_list[q]) == 3 or len(set9_list[q]) == 4 or len(set9_list[q]) == 5:
            set9_list_compare = set9_list_compare + [set9_list[q]]

    for i in range(len(set9_list_compare)):
        for j in range(i + 1, len(set9_list_compare)):
            for k in range(j + 1, len(set9_list_compare)):
                for l in range(k + 1, len(set9_list_compare)):
                    for m in range(l + 1, len(set9_list_compare)):
                        x_cells = []
                        x_cells = set9_list_compare[i] + set9_list_compare[j] + set9_list_compare[k] + \
                                  set9_list_compare[l] + set9_list_compare[m]
                        unique_candidates = []
                        for c in x_cells:
                            if c not in unique_candidates:
                                unique_candidates.append(c)
                        if len(unique_candidates) == 5:
                            # unique_candidates = [int(i) for i in unique_candidates]
                            print('in BOX ' + str(row + 1) + ' quintuplet with numbers ' + str(unique_candidates))
