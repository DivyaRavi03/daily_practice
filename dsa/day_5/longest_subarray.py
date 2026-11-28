def lengthOfLongestSubstring(text):
        longest = 0
        best = ""
        for i,c in enumerate(text):
            if c in best:
                left = best[:i].index(c)
                best = best[left+1:]
                best = best + c
            else:   
                best = best + c
            longest = max(longest, len(best))   
        return longest
for t in ["zxyzxyz", "abcabcbb", "pwwkew", "dvdf", "bbbbb", ""]:
    print(repr(t), lengthOfLongestSubstring(t))