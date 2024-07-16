def third_max(nums):
    first = second = third = float('-inf')
    unique_count = 0

    for num in nums:
        if num > first:
            first, second, third = num, first, second
            unique_count += 1
        elif first > num > second:
            second, third = num, second
            unique_count += 1
        elif second > num > third:
            third = num
            unique_count += 1

    # Check if we have at least three unique numbers
    if unique_count < 3:
        return first
    
    return third

a=[1,2,3,4]
print(third_max(a))