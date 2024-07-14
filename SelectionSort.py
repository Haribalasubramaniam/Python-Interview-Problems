def selection_sort(arr):
    for s in range(len(arr)):
        min_index = s
        for i in range(s+1,len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[s],arr[min_index] = arr[min_index],arr[s]
    return arr        
arr = [7,2,1,6]
print(selection_sort(arr))