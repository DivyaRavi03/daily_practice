def move_zeros(nums):
    position = 0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[position] = nums[i]
            position +=1
    for i in range(position, len(nums)):
        nums[i] = 0
    return nums
for t in [[0,1,0,3,12], [0], [1,2,3], [0,0,1]]:
    move_zeros(t)
    print(t)        


