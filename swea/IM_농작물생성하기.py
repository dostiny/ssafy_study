import sys; sys.stdin = open('input/IM_농작물_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    n = N // 2
    sum_v = 0
    for r in range(N):
        for c in range(N):
            if n-1 < r + c < N+n:
                sum_v += farm[r][c]

    for r in range(n):
        for c in range(r+n+1, N):
            sum_v -= farm[r][c]

    for r in range(n):
        for c in range(n-r):
            sum_v -= farm[N-1-r][c]

    print(f'#{tc} {sum_v}')