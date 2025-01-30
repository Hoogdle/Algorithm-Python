#p1 : check string whether it is palindrome or not.

# char.isalnum()
# char.lower()

def isPalindrom(s:str)->bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False

    return True