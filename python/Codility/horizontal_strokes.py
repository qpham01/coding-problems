def paint(matrix:list, c:int, r:int, cols:int):
    checks = 1
    matrix[c][r] = 0
    if c >= cols - 1: return checks
    for i in range(c + 1, cols):
        if matrix[i][r] == 0: break
        matrix[i][r] = 0
        checks += 1
    return checks

def solution(A):
    # write your code in Python 3.6
    rows = max(A)
    cols = len(A)
    matrix = []    
    for c in range(cols):
        ch = A[c]
        col = []
        for r in range(rows):
            col.append(1 if r < ch else 0)
        matrix.append(col)

    strokes = 0
    totalChecks = 0
    for c in range(cols):
        for r in range(rows):            
            if matrix[c][r] == 0: continue
            # if c == 0 or matrix[c - 1, r] == 0                
            totalChecks += paint(matrix, c, r, cols)
            strokes += 1
    print("Checks", totalChecks, sum(A))
    return strokes
                


    
A = [5, 8]
a = solution(A)
assert a == 8
A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
a = solution(A)
assert a == 9
A = [1, 1, 1, 1]
a = solution(A)
assert a == 1
A = [1, 100, 0, 1]
a = solution(A)
assert a == 101
A = [3, 0, 4, 0, 9, 0, 67, 0, 120424, 120424, 0, 8, 34]
a = solution(A)
assert a < 130000

maxStrokes = 1000000000

def paint1(matrix:list, c:int, r:int, cols:int):
    #checks = 1
    matrix[c][r] = 0
    if c >= cols - 1: return # checks
    for i in range(c + 1, cols):
        if matrix[i][r] == 0: break
        matrix[i][r] = 0
        #checks += 1
    return # checks

def solution1(A):
    # write your code in Python 3.6
    rows = max(A)
    cols = len(A)
    matrix = []    
    for c in range(cols):
        ch = A[c]
        col = []
        for r in range(rows):
            col.append(1 if r < ch else 0)
        matrix.append(col)

    strokes = 0
    #totalChecks = 0
    for c in range(cols):
        for r in range(rows):            
            if matrix[c][r] == 0: continue
            # if c == 0 or matrix[c - 1, r] == 0                
            paint(matrix, c, r, cols)
            strokes += 1
            if strokes > maxStrokes:
                return -1
    #print("Checks", totalChecks, sum(A))
    return strokes
