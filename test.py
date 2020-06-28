arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len_arr = len(arr)

for i in range(0, len_arr):
    for j in range(i, len_arr):
        print(f"{arr[i]} - {arr[j]}")
