def top_k_frequent(nums, k):
    dicti = {}
    for num in nums:
        dicti[num] = 1 + dicti.get(num,0)
    output = list(sorted(dicti, key=lambda d:dicti[d], reverse = True))
    return output[:k]

tests = [([1,1,1,2,2,3],2), ([1],1), ([4,4,5,5,5,6],1), ([-1,-1,2,2,2,3],2)]
for nums, k in tests:
    print(nums, k, sorted(top_k_frequent(nums, k)))