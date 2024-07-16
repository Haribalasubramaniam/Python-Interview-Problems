def tapping_rain_water(arr):
    left = 0
    right = len(arr)-1
    left_max = arr[left]
    right_max = arr[right]
    water = 0
    while left<right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max,arr[left])
            water += left_max-arr[left]
        else:
            right -= 1
            right_max = max(right_max,arr[right])
            water += right_max-arr[right]
    return water

arr1 = [0,1,0,2,1,0,1,3,2,1,2,1]
arr2 = [4,2,0,3,2,5]
print(tapping_rain_water(arr1))
print(tapping_rain_water(arr2))