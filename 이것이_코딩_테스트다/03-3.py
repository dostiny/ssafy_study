N, M = map(int, input().split())

a, b = 10000, 0
for i in range(1, N+1): #N행번의 줄이 나와야 하기 때문에 반복
    num_list = list(map(int, input().split()))
    for j in num_list:
        if a > j:   #a 가 리스트의 숫자보다 클때 a에 j를 넣으려고
            b = a   #b 에 a를 넣는 이유는 현재 두번째 작은 수를 표현하기 위해서
            a = j
        elif b > j > a: #초반에 빠르게 a가 최솟값이 나온다면 b도 최솟값이 되기 때문에 elif 를 추가해 a보다 큰 수 일때를 만들어 줌
            b = j
print(b)