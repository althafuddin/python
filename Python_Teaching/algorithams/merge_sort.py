def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = int(len(array)/2)
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]