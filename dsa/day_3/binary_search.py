def binary_search(nums, target):
    start = 0
    end = len(nums) -1 
    while start <= end:
        middle = (start+end)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle -1
    return -1


tests = [([-1,0,3,5,9,12], 9), ([-1,0,3,5,9,12], 2), ([5], 5), ([2,5], 5), ([1,3,5,7], 1)]
for nums, target in tests:
    print(nums, target, binary_search(nums, target))


