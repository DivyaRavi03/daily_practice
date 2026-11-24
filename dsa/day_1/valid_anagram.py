s='racecar'
t='carrace'
def anagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {},{}
    for i in range(len(s)):
        countS[s[i]]= 1 + countS.get(s[i], 0)
        countT[t[i]]= 1 + countT.get(t[i], 0)
    return countS == countT
print(anagram(s,t))

# T.C = O(n), S.C = O(1)