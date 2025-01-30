import collections


# using deque for reducing time complexity when pop(0)

def isPalindrome(s:str)->bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False

    return True