import sys; sys.stdin = open('input/1961_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    num_li = []
    for _ in range(N):
        num_li += map(int, input().split())

    # 90도
    idx = 0
    num90 = [[0]*N for _ in range(N)]
    for r in range(N - 1, -1, -1):
        for c in range(N):
            num90[c][r] = num_li[idx]
            idx += 1

    # 180도
    idx = 0
    num180 = [[0]*N for _ in range(N)]
    for r in range(N-1, -1, -1):
        for c in range(N-1, -1, -1):
            num180[r][c] = num_li[idx]
            idx += 1

    # 270도
    idx = 0
    num270 = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N-1, -1, -1):
            num270[c][r] = num_li[idx]
            idx += 1

    print(f'#{tc}')
    for r in range(N):
        for c in range(N):
            print(num90[r][c], end='')
        print('', end=' ')
        for c in range(N):
            print(num180[r][c], end='')
        print('', end=' ')
        for c in range(N):
            print(num270[r][c], end='')
        print()
