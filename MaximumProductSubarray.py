def maximum_product_subarray(nums):
    min_product = nums[0]
    max_product = nums[0]
    result = max_product
    for i in nums[1:]:
        if i<0:
            min_product,max_product = max_product,min_product
        min_product = min(i,min_product*i)
        max_product = max(i,max_product*i)
        result = max(result,max_product)
    return result
    
nums1=[2,3,-2,-4]
nums2=[-2,0,-1]
print(maximum_product_subarray(nums1))
print(maximum_product_subarray(nums2))