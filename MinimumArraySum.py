def minimumArraySum(n,arr):
    arr.sort()
    avg=(arr[n-1]+arr[n-2])/2
    res=0
    for i in arr:
        if i>=avg:
            res+=i
    return res
arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
print(minimumArraySum(n,arr))