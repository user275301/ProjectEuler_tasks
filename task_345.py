import numpy as np

arr =  [[  7,  53, 183, 439, 863],
        [497, 383, 563,  79, 973],
        [287,  63, 343, 169, 583],
        [627, 343, 773, 959, 943],
        [767, 473, 103, 699, 303]]

strings = set(range(5))
rows = set(range(5))

def max(arr, strings, rows):
    for i in strings:
        for j in rows:
            max  = arr[i][j]
            maxi = i
            maxj = j
            break

    for i in strings:
        for j in rows:
            if max<arr[i][j]:
                max = arr[i][j]
                maxi = i
                maxj = j
    strings.remove(maxi)
    rows.remove(maxj)
    return max

res = list(max(arr,strings,rows) for i in range(5))
print(res)
