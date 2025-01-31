#p5 : find Anagrams from given list
import collections

# sorted function returns list which sorted
# dictionary can use 'append' to add element in dictionary
# dictionary.values() returns all the values of dictionary
# good algorithm that using dictionary to deal with complexity

def groupAnagrams(strs: list[str])->list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())
