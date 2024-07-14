def maximum_sum_subarray(nums):
    max = nums[0]
    curr_sum = 0
    for i in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += i
        if curr_sum > max:
            max = curr_sum
    return max
        
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]
print(maximum_sum_subarray(nums1))
print(maximum_sum_subarray(nums2))
        