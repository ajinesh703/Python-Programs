def shell_sort_advanced(arr, gap_sequence):
    n = len(arr)
    
    for gap in gap_sequence:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

# Custom gap sequence (Using Sedgewick's gaps for instance)
gap_sequence = [57, 23, 10, 4, 1]

# Example usage
arr = [12, 34, 54, 2, 3]
shell_sort_advanced(arr, gap_sequence)
print("Sorted array:", arr)
