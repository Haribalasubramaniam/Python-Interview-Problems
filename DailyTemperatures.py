def daily_temperatures(arr):
    stack = []
    ans = [0]*len(arr)
    for i,t in enumerate(arr):
        while stack and arr[stack[-1]]<t:
            j = stack.pop()
            ans[j] = i-j
        stack.append(i)
    return ans
    
    
arr = [73,74,75,71,69,72,76,73]
print(daily_temperatures(arr))
arr1 = [30,40,50,60]
print(daily_temperatures(arr1))