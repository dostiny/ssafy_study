N = int(input())

sqN = 1 + 4 * (N - 1)
arr = [[' ']*sqN for _ in range(sqN)]
ar = ac = (sqN - 1) // 2

while ar >= 0:
    for i in range(ar, ac+1):
        arr[ar][i] = '*'
        arr[i][ar] = '*'
        arr[i][ac] = '*'
        arr[ac][i] = '*'
    ar, ac = ar - 2, ac + 2

for ar in arr:
    print(*ar)
