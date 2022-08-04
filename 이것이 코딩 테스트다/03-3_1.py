n, m = map(int, input().split()) # N 행, M 열

minnum_list = []    # 최솟값을 받을 빈 리스트
for i in range(n):  # N 행번의 입력을 받아야함
    li = sorted(list(map(int, input().split())))    #입력받은 숫자를 리스트에 넣은후 오름차순정렬
    minnum_list.append(li[0])   # 빈 리스트에 최솟값만 추가
    minnum_list.sort(reverse=True)  # 리스트 내림차순 정렬

print(minnum_list[0])   # 내림차순 정렬했으니 맨 앞숫자는 작은 숫자들중 가장 큰수이다.