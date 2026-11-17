def second_largest(nums):
    largest = None
    second = None
    for num in nums:
        if largest is None or num > largest:
            second = largest 
            largest = num
        elif (second is None or num > second) and num!=largest:
            second = num
    return second


assert second_largest([3, 7, 2, 9, 5]) == 7
assert second_largest([1, 2, 3, 4, 5]) == 4
assert second_largest([20, 10]) == 10
assert second_largest([10, 20]) == 10
assert second_largest([5, 5, 4]) == 4
assert second_largest([2, 9, 9, 1]) == 2
assert second_largest([-3, -1, -7]) == -3
assert second_largest([0, -1]) == -1
assert second_largest([9, 9, 9]) is None
assert second_largest([7]) is None
assert second_largest([]) is None

print("All tests passed!")