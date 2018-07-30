# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0

    # use dictionary (hash table) to store index locations for O(1) lookup time.
    indices_lookup = {}
    for index, value in enumerate(arr):
        indices_lookup[value] = index

    # create a sorted copy of the array
    sorted_arr = sorted(arr)

    for index, value in enumerate(arr):
        if value != sorted_arr[index]:
            swap_value = sorted_arr[index]
            swap_index = indices_lookup[swap_value]

            arr[index], arr[swap_index] = arr[swap_index], arr[index]
            indices_lookup[value], indices_lookup[swap_value] = indices_lookup[swap_value], indices_lookup[value]

            swap_count += 1

    return swap_count


arr = [1, 3, 5, 2, 4, 6, 8]
print(minimumSwaps(arr))
