# Give an image represented by an NxN matrix, where each pixel in the image is
# 4 butes, write a method to rotated the image by 90 degrees. Can you do this in place

def rotate(matix, n):
    if len(matrix) - 2 * n <= 0:
        return

    lastElement = len(matrix) - n - 1
    topLine = matrix[n][n:len(matrix)-n]
    rightLine = [line[lastElement] for line in matrix[n:len(matrix) - n]]
    bottomLine = matrix[lastElement][n:len(matrix) - n][:]
    leftLine = [line[n] for line in matrix[n:len(matrix) - n]]

    # top
    for index, line in enumerate(matrix[n:len(matrix) - n]):
        line[lastElement] = topLine[index]

    # right
    line = matrix[lastElement]
    for index in xrange(0, len(rightLine)):
        line[index + n] = rightLine[0 - index - 1]

    # bottom
    for index, line in enumerate(matrix[n:len(matrix) - n]):
        line[n] = bottomLine[index]

    # left
    line = matrix[n]
    for index in xrange(0, len(leftLine)):
        line[index + n] = leftLine[0 - index - 1]

    return rotate(matrix, n + 1)



matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
rotate(matrix, 0);
print matrix
