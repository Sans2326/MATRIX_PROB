def transpose(arr):
    for i in range(n):
        for j in range(i, n):
            if i != j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]  # swap
    return arr


def rotate90ACW(arr):
    arr = transpose(arr)
    for j in range(n):
        for i in range(n // 2):
            arr[i][j], arr[n-1-i][j] = arr[n - 1 - i][j], arr[i][j]
    return arr


n = int(input())
l = list(map(int, input().split()))
matrix = []
# we are given space separated matrix
for i in range(0, n * n, n):
    temp = l[i:n + i]
    matrix.append(temp)
matrix90 = rotate90ACW(matrix)

print("\t90 DEGREE  ANTICLOCKWISE ROTATION")
for i in range(n):
    print(*matrix90[i])

matrix180 = rotate90ACW(matrix90)  # call in multiple of 90 times
print("\t180 DEGREE ANTICLOCKWISE ROTATION")
for i in range(n):
    print(*matrix180[i])

matrix270 = rotate90ACW(matrix180)
print("\t270 DEGREE ANTICLOCKWISE ROTATION")
for i in range(n):
    print(*matrix270[i])