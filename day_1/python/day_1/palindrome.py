def is_palindrome(word):
    cleaned = ""
    for letter in word:
        if letter.isalnum():
            cleaned+=letter.lower()
    for i in range(len(cleaned)//2):
        if cleaned[i] != cleaned[(len(cleaned)-i)-1]:
            return False
    return True


assert is_palindrome("racecar") == True
assert is_palindrome("RaceCar") == True
assert is_palindrome("A man, a plan, a canal: Panama!") == True
assert is_palindrome("No 'x' in Nixon") == True
assert is_palindrome("Was it a car or a cat I saw?") == True
assert is_palindrome("12321") == True
assert is_palindrome("a") == True
assert is_palindrome("") == True
assert is_palindrome("!!!") == True
assert is_palindrome("hello") == False
assert is_palindrome("ab") == False
assert is_palindrome("1a2") == False

print("All tests passed!")


