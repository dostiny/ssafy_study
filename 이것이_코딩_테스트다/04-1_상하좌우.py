import sys

sys.stdin = open('04-1.txt', 'r')

T = int(input())
arr = list(map(str, input().split()))

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

