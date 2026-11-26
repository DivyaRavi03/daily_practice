def maximum_subarray(nums):
    sum =0
    largest = nums[0]
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum > largest:
            largest = sum
        if sum < 0:
            sum = 0
        
    return largest

print(maximum_subarray([-3,-1,-2]))
print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maximum_subarray([1]))
print(maximum_subarray([5,4,-1,7,8]))
            
        
