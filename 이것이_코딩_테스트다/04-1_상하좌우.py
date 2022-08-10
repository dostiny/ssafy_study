import sys

sys.stdin = open('04-1.txt', 'r')

T = int(input())
arr = list(map(str, input().split()))

x, y = 1, 1
U = x - 1
D = x + 1
L = y - 1
R = y + 1

for i in arr:
    if i == 'U':
        if x != 1:
            x -= 1
    elif i == 'D':
        x += 1
    elif i == 'L':
        if y != 1:
            y -= 1
    elif i == 'R':
        y += 1
print(x, y)

