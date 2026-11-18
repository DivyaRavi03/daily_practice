def stocks(nums):
    cheapest = nums[0]          # cheapest price seen so far = day 0's price
    best = 0
    for price in nums:
        if price < cheapest:
            cheapest = price
        if (price - cheapest) > best:
            best = price - cheapest
    return best
        

for t in [[7,1,5,3,6,4], [7,6,4,3,1], [2,4,1], [1]]:
    print(t, stocks(t))    
    
