import sys; sys.stdin = open('input/6485_input.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [0 for _ in range(5001)]
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            arr[i] += 1

    print(f'#{tc}', end=' ')
    for _ in range(int(input())):
        c = int(input())
        print(arr[c], end=' ')
    print()