from re import X


N, M, K = map(int, input().split())
N_list = list(map(int, input().split()))
x, y = N_list[0], 0

if N == len(N_list):    # N이 입력된 숫자들과 맞는지 확인
    for i in N_list:    # 첫번째로 큰수와 두번째로 큰수 구하는 반복문
        if x <= i:
            y = x
            x = i

total_num = 0   # 합을 구할 변수 0 설정
while M != 0:   # M 횟수 동안 반복
    if M > K:
        total_num += x * K
        M -= K
        if M >= 1:
            total_num += y
            M -= 1
    else:
        total_num += x * M
        M -= M

print(total_num)