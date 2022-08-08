n, k = map(int, input().split())    # N: 동전개수, K: 금액

money_list = [] # 동전의 가치를 담을 빈 리스트
for i in range(n):  # n 번 반복
    money_list.append(int(input())) # 동전의 가치 입력
money_list.sort(reverse=True)   # 동전가치 리스트를 내림차순으로 정렬

money_count = 0 #동전의 갯수 변수 설정
for j in money_list:    # 입력받은 동전의 수 만큼 반복
    money_count += k // j   # 
    if k == 0:
        pass
    elif k//j != 0:
        k -= j* (k//j)

print(money_count)