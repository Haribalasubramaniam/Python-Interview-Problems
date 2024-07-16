def solution(arr):
    dict={}
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    result=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        while stack and dict[stack[-1]] <= dict[arr[i]]:
            stack.pop()
        if stack:
            result[i]=stack[-1]
        stack.append(arr[i])
    return result
    
    
    
    
arr1=[1,1,2,3,4,4,1,4,2,1]
print(solution(arr1))