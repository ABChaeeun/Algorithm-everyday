def solution(arr):
    
    if len(arr) != 1:
        del arr[arr.index(min(arr))]
    else:
        arr = [-1]
    
    return arr
