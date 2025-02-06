#p4 : print word which present most time in given string and not be banned in given condition.
import collections
import re

# using regular expression. (pattern | repl | given str|)
# when setting pattern, which in regular expression, maybe 'r' means 'remove' and '^' means 'not
# using collection.Counter
# Counter's parameter is list

def mostCommonWord(paragraph:str, banned:list[str])->str:

    words = [word for word in re.sub(r'[^\w]','',paragraph).lower().split()]

    counter = collections.Counter(words)

    return counter.most_common(1)[0][0]
