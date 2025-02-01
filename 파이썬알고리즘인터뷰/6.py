#p6 : find largest length Palindrome

# using two-pointer
# divide case into two
# max() return maximum object(not integer value)
# max() can use 'key' parameter

def longestPalindrome(s: str)->str:
    def expand(left: int, right: int)->str:
        while left>=0 and right<len(str) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s)<2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s)):
        result = max(result, expand(i,i+1), expand(i,i+2), key=len)

    return result

