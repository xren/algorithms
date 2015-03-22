# Given two strings, check if one is the permutation of the other

def isPermutation(string1, string2):
    return sorted(list(string1)) == sorted(list(string2))
