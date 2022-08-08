n = int(input())
n_drive = list(map(int, input().split()))
n_price = list(map(int, input().split()))
total_drive = 0
for i in n_drive:
    total_drive += i

j=0
price = 0
while total_drive != 0:
    if n_price[j] >= n_price[j+1]:
        price += n_price[j]*n_drive[j]
        total_drive -= n_drive[j]
    elif n_price[j] < n_price[j+1]:
        price += n_price[j]*(n_drive[i]+n_drive[i+1])
        total_drive -= (n_drive[i]+n_drive[i+1])
    j+=1
print(price)