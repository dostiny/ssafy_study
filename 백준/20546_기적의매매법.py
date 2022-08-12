A = B = int(input())
arr = list(map(int, input().split()))
N = len(arr)
ac = 0
bc = 0
for i in range(N):
    ac += A // arr[i]
    A = A % arr[i]
    if i >= 4:
        if arr[i-1] > arr[i-2] > arr[i-3]:
            B += arr[i] * bc
            bc = 0
        elif arr[i-1] < arr[i-2] < arr[i-3]:
            bc += B // arr[i]
            B = B % arr[i]
am = ac * arr[-1] + A
bm = bc * arr[-1] + B
print(am, bm)
if am > bm:
    print('BNP')
elif am < bm:
    print('TIMING')
else:
    print('SAMESAME')