import re

# using 'regular expression'
# using 'slice'

def isPalindrome(s:str)->bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)
    return s==s[::-1]