N=int(input("N: "))
M=int(input("M: "))
L=int(input("L: "))
#N, M, L 입력받음

list=[0]*N #각 리스트의 값 0으로 초기화
list[0]=1 #첫번째부터 공 받으므로 1 대입
person=1 #인덱스 값 (1으로 초기화)
count=1 #공 던지는 횟수


while(True):

    if(list[person]==M):
        break #M번 카운팅 되면 종료

    else :
        if(list[person]%2==0): #현재 공을 받은 횟수가 짝수면
            person=person-L #반시계 방향으로 L만큼 회전
            if(person<0):
                person=N+person

        else : #홀수면 시계방향으로 L만큼 회전
            person=person+L
            if(person>N-1):
                person=person-N

    list[person]+=1
    count+=1

        

    
print("공을 던진 횟수: ", count)
