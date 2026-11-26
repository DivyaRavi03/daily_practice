import re
def is_valid_email(mail):
    match = re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', mail)
    return match
    # return match is not None

# assert is_valid_email("divya@gmail.com") == True
# assert is_valid_email("first.last+jobs@umich.edu") == True
# assert is_valid_email("user_1@mail.co.uk") == True
# assert is_valid_email("a-b@my-site.io") == True

# assert is_valid_email("divyagmail.com") == False      # no @
# assert is_valid_email("divya@@gmail.com") == False    # two @
# assert is_valid_email("@gmail.com") == False          # nothing before @
# assert is_valid_email("divya@gmail") == False         # no ending
# assert is_valid_email("divya@gmail.c") == False       # ending too short
# assert is_valid_email("divya @gmail.com") == False    # space
# assert is_valid_email("") == False

assert is_valid_email("a@b_c.com") == False   # _ isn't allowed in the domain
assert is_valid_email("a@b.COM") == True      # capital letters are fine in the ending

print("All tests passed!")