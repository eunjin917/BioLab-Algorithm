#9012

t = int(input())            #입력 데이터 수

v = list()                  #VPS판단 결과 문자열
a = 0

for i in range(t):          #t만큼 반복 입력
    ps = input()            #괄호 문자열 입력
    s = list(ps)            
    sum = 0

    for i in s:             #리스트 모든 요소
        if i == '(':        #열린 괄호일때 +1
            sum += 1
        elif i == ')':      #닫힌 괄호일때 -1
            sum -= 1

        if sum < 0:         #합이 -1이 될 경우
            break

    if sum > 0 or sum < 0:  #VPS가 아님
        v.append(0)
    elif sum == 0:          #VPS
        v.append(1)

for i in range(t):          #리스트 차례대로 출력
    if v[a] == 0:
        print('NO')
    elif v[a] ==1:
        print('YES')
    a += 1