arr = [2, 56, 34, 7, 33, 12, 89, 32]
def bubble_sort(array):
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            for count in range(len(arr)-1):
                if arr[count] >= arr[count+1]:
                    arr[count], arr[count+1] = arr[count+1], arr[count]
    return arr
print bubble_sort(arr)
