N = int(input())
f = int(input())

arr = [[0]*N for _ in range(N)]
start = 1
nn = N**2   # 최대값
cr = cc = (N - 1) // 2   # 중앙 + 위치
dire = 0
while start != nn:
    arr[cr][cc] = start
    if dire == 0:
        cr, cc = cr - 1, cc
        if arr[cr][cc+1] == 0:
            dire = 3
    elif dire == 1:
        cr, cc = cr + 1, cc
        if arr[cr][cc-1] == 0:
            dire = 2
    elif dire == 2:
        cr, cc = cr, cc - 1
        if arr[cr-1][cc] == 0:
            dire = 0
    elif dire == 3:
        cr, cc = cr, cc + 1
        if arr[cr+1][cc] == 0:
            dire = 1
    start += 1
    if start == nn:
        arr[cr][cc] = start

x, y = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == f:
           y, x = i, j
for ar in arr:
    print(*ar)
print(y+1, x+1)