import sys; sys.stdin = open('1210_input.txt', 'r')

for N in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for two in range(100):
        if arr[99][two] == 2:
            two_r = 99
            two_c = two
    while two_r > 0:
        arr[two_r][two_c] = 2   # 현재위치를 바꿔주어 1을 찾는데 수월하게 하기위함
        if two_c != 0 and two_c != 99:   # 왼쪽 끝이나 오른쪽 끝이 아닐때
            if arr[two_r][two_c-1] == 1:    # 왼쪽으로 이동
                two_c -= 1
            elif arr[two_r][two_c+1] == 1:  # 오른쪽으로 이동
                two_c += 1
            else:   # 왼쪽 오른쪽 둘다 아니라면 위로
                two_r -= 1
            # if arr[two_r-1][two_c] == 1:    # 위쪽으로 가는 조건
            #     if arr[two_r][two_c-1] == 1:    # 왼쪽 확인
            #         two_c -= 1
            #     elif arr[two_r][two_c+1] == 1:  # 오른쪽 확인
            #         two_c += 1
            #     else:
            #         two_r -= 1  # 왼쪽 오른쪽 확인후 둘다아니라면 위로
            # elif arr[two_r][two_c-1] == 1:  # 왼쪽으로 가는 조건
            #     two_c -= 1
            # elif arr[two_r][two_c+1] == 1:  # 오른쪽으로 가는 조건
            #     two_r -= 1
        elif two_c == 0:    # column 이 0 이면 왼쪽으로 못가기 때문에
            if arr[two_r - 1][two_c] == 1:  # 위쪽으로 가는 조건
                if arr[two_r][two_c + 1] == 1:  # 오른쪽 확인
                    two_c += 1
                else:
                    two_r -= 1
        elif two_c == 99:   # column 이 99이면 오른쪽으로 못가기 때문에
            if arr[two_r-1][two_c] == 1:    # 위쪽으로 가는 조건
                if arr[two_r][two_c-1] == 1:    # 왼쪽 확인
                    two_c -= 1
                else:
                    two_r -= 1

    print(f'#{test_case} {two_c}')