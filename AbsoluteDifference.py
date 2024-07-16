def solution(arr):
    n=len(arr)
    total_sum=0
    left_sum=0
    b=[]
    for i in arr:
        total_sum += i
    for i in range(n):
        right_sum=total_sum - left_sum - arr[i]
        b.append(abs(left_sum-right_sum))
        left_sum+=arr[i]
        
    return b

a=[10,4,8,3]
print(solution(a))