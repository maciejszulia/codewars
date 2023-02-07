def find_uniq(arr):
    arr.sort(reverse=True)
    unique_elem = arr[len(arr)-1]
    if arr[0] != arr[1]:
        unique_elem = arr[0]
    return unique_elem


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(len([ 1, 1, 1, 2, 1, 1 ]))