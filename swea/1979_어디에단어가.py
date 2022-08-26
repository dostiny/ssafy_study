import sys; sys.stdin = open('input/1979_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    cnt_r = cnt_c = 0
    result = 0
    for r in range(N):
        cnt_r = cnt_c = 0
        for c in range(N):
            # 가로 확인
            if arr[r][c] == 1:  # 1이면 카운트 업
                cnt_r += 1
                if c == N-1 and cnt_r == K:   # 만약 끝에 도착 + 카운트가 K이면 result+1,cnt초기화
                    result += 1
                    cnt_r = 0
            elif arr[r][c] == 0 or c == N-1:    # 값이 0 or 끝에 도착했을때
                if cnt_r == K:  # 카운트가 K 이면 결과값 추가
                    result += 1
                cnt_r = 0   # 카운트 초기화

            # 세로 확인
            if arr[c][r] == 1:  # 1이면 카운트업
                cnt_c += 1
                if c == N-1 and cnt_c == K: # # c가 인덱스 끝에 도착하고 카운트가 K일때
                    result += 1
                    cnt_c = 0
            elif arr[c][r] == 0 or c == N-1:    # # 0이거나 인덱스 끝에(0인상태로) 도착했을때
                if cnt_c == K:
                    result += 1
                cnt_c = 0   # 카운트 초기화
    print(f'#{tc} {result}')

