# Write a method to replace all spaces in a string with %20. Assume you have enough space


['g', 'e', ' ', 's', 'g']
def replaceString(stringArray):
    p = len(stringArray) - 1
    lastIndex = len(stringArray) - 1
    while p > 0:
        if stringArray[p] == ' ':
            spaceToAdd = lastIndex - p
            stringArray.extend([None, None])

            while lastIndex > p:
                stringArray[lastIndex+2] = stringArray[lastIndex]
                lastIndex -= 1

            stringArray[p] = '%'
            stringArray[p+1] = '2'
            stringArray[p+2] = '0'

        p -= 1
    return stringArray

print replaceString(['g', 'e', ' '])
