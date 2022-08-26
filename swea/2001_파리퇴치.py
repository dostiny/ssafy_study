import sys; sys.stdin = open('input/2001_input.txt', 'r')

for tc in range(1, int(input())+1):
    M, N = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(M)]
    sum_v = 0
    mav_v = 0
    for x in range(M-N+1):
        for y in range(M-N+1):
            for r in range(N):
                for c in range(N):
                    sum_v += area[x+r][y+c]
            if mav_v < sum_v:
                mav_v = sum_v
            sum_v = 0
    print(f'#{tc} {mav_v}')
