# Implement an algorithm to determine if a string has all unique characters.
# What if you can't use additional data structure

def isUnique(string):
    for index, char in enumerate(string):
        for j in xrange(index + 1, len(string)):
            if char == string[j]:
                return True

    return False

print isUnique('aiofj')
