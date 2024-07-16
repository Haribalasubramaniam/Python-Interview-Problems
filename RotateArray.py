"""
Method 1 : Creating a New Array

def rotate_array(nums,k):
    a=[]
    n = len(nums)
    for i in range(n-k,n):
        a.append(nums[i])
    for i in range(n-k):
        a.append(nums[i])
    return a
"""
#Method 2 -- Replacing in the Array itself 

def rotate_array(nums,k):
    n = len(nums)
    r = n-k
    new = nums[:r]
    nums[0:r] = []
    nums.extend(new)
    return nums
    
   
nums=[1,2,3,4,5,6,7]
k=3
print(rotate_array(nums,k))