# write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0

def flip(matrix):
    rowList = {}
    columnList = {}
    for columnIndex in xrange(0, len(matrix)):
        for rowIndex in xrange(0, len(matrix[0])):
            if matrix[columnIndex][rowIndex] == 0:
                rowList[rowIndex] = True
                columnList[columnIndex] = True

    # row
    for row in rowList:
        for column in matrix:
            column[row] = 0

    # column
    for column in columnList:
        for index in xrange(0, len(matrix[column])):
            matrix[column][index] = 0


    return matrix

print flip([[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 0]])
