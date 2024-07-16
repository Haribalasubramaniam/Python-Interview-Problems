def binary_search(arr,start,end,x):
    if end>=start:
        mid=(start+end)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            end=mid-1
            return binary_search(arr,start,end,x)
        else:
            start=mid+1
            return binary_search(arr,start,end,x)
    else:
        return -1
    
arr = [1,2,3,4,5,6,7,8,9]
start = 0
end = len(arr)-1
x = int(input("Enter the Number to be found : "))
print(binary_search(arr,start,end,x))