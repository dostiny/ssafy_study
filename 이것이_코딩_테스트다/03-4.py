n, k = map(int, (input().split()))
finally_num = 0

while n != 1:    
    if n % k == 0:
        n = n // k
        finally_num += 1
    else:
        n = n - 1
        finally_num += 1

print(finally_num)