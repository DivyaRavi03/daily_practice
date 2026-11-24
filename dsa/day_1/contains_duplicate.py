n = [1,2,3,1]
def duplicate(n):
    hashset = set()
    for i in n:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(duplicate(n))

# T.C = O(n), S.C =O(n)