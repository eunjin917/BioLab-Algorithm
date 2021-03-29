'''
괄호 문자열 VPS판단
https://www.acmicpc.net/problem/9012
2021.03.23

'''

num=int(input())

for i in range(0, num) : #받은 수 만큼 문자열 입력
    stack1=input() #문자열 입력
    MAX=len(stack1)-1 #리스트 마지막 인덱스
    c_list=len(stack1) #stack1의 요소 개수 
    stack1=list(stack1) #한 문자열을 글자 하나씩 분리
    stack2=[] #임시스택
    index=0 #스택2를 사용하는 데 필요한 인덱스
    
    while(c_list!=0) : #stack1이 비워질때까지 검사 -> 4차 판별

        if(c_list%2!=0): #숫자로 1차 판별
            print("NO\n")
            break

        c1=stack1.count('(')
        c2=stack1.count(')')

        if(c1!=c2): #각 괄호의 개수로 2차 판별
            print("NO\n")
            break

        if(stack1[MAX]=='('or stack1[0]==')'): #괄호 맨 처음과 끝으로 3차 판별
            print("NO\n")
            break

    
        while stack1[MAX]!='(' : # '('가 나올때까지')'를 스택2에 쌓음
            stack2.insert(index,stack1.pop(MAX)) # '('가 나오기 전까지 요소들을 다른 스택에 잠시 옮겨둠
            MAX=len(stack1)-1 #stack1에서 빼내갔으므로 재측정
            c_list=len(stack1) #재측정2
            index=len(stack2)-1
            

        stack1.pop() # '(' 제거
        
        for j in range(0, len(stack2)) : #스택 2에 있는 요소들을 다시 스택1 뒤에 삽입
            stack1.insert(MAX+1, stack2.pop(0))
            MAX=len(stack1)-1
            
        stack1.pop() #
        MAX=len(stack1)-1
        c_list=len(stack1)
        
        if(c_list==0):
            print("YES\n")
            break

            
