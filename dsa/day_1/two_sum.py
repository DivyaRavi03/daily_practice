s=[5,5]
t=10
def target(s, t):
    seen = {}
    for i, n in enumerate(s):
        diff = t - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []
print(target(s,t))

# T.C = O(n)