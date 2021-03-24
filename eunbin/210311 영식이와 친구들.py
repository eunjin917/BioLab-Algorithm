#1592

n,m,l = map(int,input().split())                #n명, m번, l번째

people = {}
for i in range(1,n+1):                          #1부터 n까지 반복
    people[i] = 0 

cnt = 0                                         #공을 던진 횟수
p = people[1] = 1                               #첫번째 사람이 처음 공을 받음
while people[p]!=m:                             #m이 아닐때 반복
    if people[p]%2!=0:                          #홀수
        p = n if (p+l)%n == 0 else (p+l)%n      #시계방향으로 l번 돌림
    else:                                       #짝수
        p = (p-l+n) if (p-l) <= 0 else (p-l)    #반시계 방향으로 l번 돌림

    people[p] += 1                              #p번째 사람이 공받은 횟수 증가
    cnt += 1                                    #공을 던진 횟수 증가
    
print(cnt)