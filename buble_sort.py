def buble_sort(arr, reverse=False):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if arr != sorted(arr):
        buble_sort(arr, reverse)
    if reverse:
        arr.reverse()

lst = [1, 5, 2, 8, 2, 5, 7, 6, 4, 3]
buble_sort(lst, reverse=True)
print(lst)