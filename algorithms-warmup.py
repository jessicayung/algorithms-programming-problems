# Diagonal Difference

def diagonaldifference(matrix):
    firstdiagonalsum = 0
    seconddiagonalsum = 0
    for i in range(0,n):
        firstdiagonalsum += int(matrix[i][i])
        seconddiagonalsum += int(matrix[i][n-1-i])
    print(abs(firstdiagonalsum - seconddiagonalsum))

n = int(input())
matrix = []
for i in range(0,n):
    new_row = [int(x) for x in input().split()]
    matrix.append(new_row)
diagonaldifference(matrix)

