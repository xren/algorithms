# Implement a function void reverse(char* str) in C or C++ which reverses a
# null-terminated string


# use a 'n' as null value
def reverse(string):
    if len(string) <= 2:
        return string

    stringArray = list(string)
    head = 0
    tail = len(string) - 2

    while tail > head:
        temp = stringArray[tail]
        stringArray[tail] = stringArray[head]
        stringArray[head] = temp
        head += 1
        tail -= 1

    return ''.join(stringArray);

print reverse('abasdfan')
