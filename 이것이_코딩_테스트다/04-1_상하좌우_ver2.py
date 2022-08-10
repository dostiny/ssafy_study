import sys

sys.stdin = open('04-1.txt', 'r')

n = int(input())
arr = list(map(str, input().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for i in arr:
    for j in range(len(move)):
        if i == move[j]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx < n or ny > n:
        continue
    x, y = nx, ny
print(x, y)