# Implement a method to perform basica string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would be come a2b1c5a3
# If the "compressed" string would not become smaller than the original string our
# method should return the orginal string

def compress(string):
    stringArray = list(string)
    count = 1
    current = 0

    for i in xrange(1, len(stringArray) + 1):
        if i < len(stringArray) and stringArray[i] == stringArray[i - 1]:
            count += 1
        else:
            stringArray[current] = stringArray[i - 1]
            if count > 1:
                current += 1
                stringArray[current] = str(count)
                count = 1
            current += 1

    return ''.join(stringArray[:current])

print compress('bbaa')
