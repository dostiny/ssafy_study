place = [[0]*100 for _ in range(100)]
arr = [list(map(int, input().split())) for _ in range(4)]
result = 0
for i in range(4):
    sr, sc, er, ec = arr[i][0], arr[i][1], arr[i][2], arr[i][3]
    for r in range(sr, er):
        for c in range(sc, ec):
            if place[r][c] == 0:
                place[r][c] = 1
                result += 1

print(result)