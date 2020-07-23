# isGFG: , Link: 
# IsDone: 0
def LCSLength(X, Y):
    Table = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                Table[i + 1][j + 1] = Table[i][j] + 1
            else:
                Table[i + 1][j + 1] = \
                    max(Table[i + 1][j], Table[i][j + 1])
    # read the substring out from the matrix
    result = ""
    x, y = len(X), len(Y)
    while x != 0 and y != 0:
        if Table[x][y] == Table[x - 1][y]:
            x -= 1
        elif Table[x][y] == Table[x][y - 1]:
            y -= 1
        else:
            assert X[x - 1] == Y[y - 1]
            result = X[x - 1] + result
            x -= 1
            y -= 1
    return result
