def push_front(arr):
    arr.append("floople")
    print arr
    for count in range(len(arr)-1):
        print len(arr)
        print count
        arr[len(arr)-1-count], arr[len(arr)-2-count] = arr[len(arr)-2-count], arr[len(arr)-1-count]
    return arr
print push_front([2, 15, "ghad", 382, 39, "woei"])
