from itertools import count


N = int(input())

count_money = 0
while N != 0:
    if N >= 500:
        count_money += N // 500
        N = N % 500
    elif N >= 100:
        count_money += N // 100
        N = N % 100
    elif N >= 50:
        count_money += N // 50
        N = N % 50
    elif N >= 10:
        count_money += N // 10
        N = N % 10

print(count_money)