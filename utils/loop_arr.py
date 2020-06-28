arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
len_arr = len(arr)

# loop 1 array twice
for i in range(0, len_arr):
    for j in range(i, len_arr):
        print(f"{arr[i]} - {arr[j]}")


# loop 1 array
for val in arr:
    print(val)

# loop index, val
for index, val in enumerate(arr):
    print(index, val)
