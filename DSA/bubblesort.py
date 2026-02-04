def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr

print(bubble_sort([2, 0, 1, 0, 2, 1, 3, 2, 3]))
