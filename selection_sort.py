def selection_sort(arr, reverse=False):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    if arr != sorted(arr):
        selection_sort(arr, reverse)

    if reverse:
        arr.reverse()


    
lst = [1, 5, 2, 8, 2, 5, 7, 6, 4, 3]
selection_sort(lst, True)
print(lst)
            