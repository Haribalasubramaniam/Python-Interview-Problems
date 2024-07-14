def two_sum(array,target):
    dict= {}
    for i,num in enumerate(array):
        diff = target - num
        if diff in dict:
            return [i,dict[diff]]
        dict[num] = i
    return []

array1 = [2,7,11,15]
target1 = 9 #output=[0,1]
print(two_sum(array1,target1))
array2 = [3,2,4]
target2 = 6 #output=[1,2]
print(two_sum(array2,target2)) 
 
        
        