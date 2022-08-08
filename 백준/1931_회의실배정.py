n = int(input())
t_set = set()
t_table = []

for i in range(n):  # 회의 수
    t = list(map(int, input().split())) # 입력받는 시간
    start_t = t[0]  # 시작하는 시간
    end_t = t[-1]+1 # 끝나는 시간

    for j in range(start_t, end_t): 
        t_set.add(j)    # 시작 시간과 끝나는 시간의 사이를 채운후 set에 넣음
    
    t_table.append(t_set)   # 시간 set으로 이루어진 타임테이블 리스트
    t_set = set()   # t_set 을 for 문 끝날때 다시 초가화시켜줌

t_count = 1 #최대로 이용할수 있는 회의 카운트
result = 0   # 최종 값

for x in t_table:   # 회의 시간 리스트 안에 있는 시간 set을 가져옴
    full_t = x  # full_t 을 따로 선언한 이유는 full_t에 중첩해서 추가하여 비교하기 위해서
    for y in t_table:   # 회의 시간 리스트 안에 있는 시간 set을 가져옴 (비교를 위해)
        if len(full_t & y) == 0:    # full_t 와 교집합이 0 일때
            full_t = full_t | y # full_t에 full_t와 y의 합집합을 입력
            t_count += 1
    if result <= t_count:   # 카운트가 더 클때 값을 변경해줘야하기때문에
        result = t_count
    t_count = 1

print(result)

# 메모리 초과로 실패