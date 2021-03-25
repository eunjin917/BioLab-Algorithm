class Stack(list):
    push = list.append # push
    pop = list.pop # pop
    
    def is_empty(self):
        if not self:
            return True
        else:
            return False #스택 클래스

def stackCNT(string,lengthg):
    stack = []
    for i in string:
        op = '('
        cl = ')'
        if i in op: # push('('로 시작될때 스택에  넣기)
            stack.append(i)            
            if op.find(stack.pop()) != cl.find(i):
                return True #pop (,) 다르면 True
            
            
        if i in cl: # push( ')'로 시작될때 스택에  넣기)
            stack.append(i)
            if cl.find(stack.pop()) != op.find(i):
                return False #pop ),( 다르면 False
            
    if not stack:
        return True #스택이 비어있다면  Ture
    else:
        return False #스택에 남아 있다면 False 

while True:
    string = str(input("input ()  : "))
    lenstring = len(string)
    print(lenstring)
    if stackCNT(string,lenstring) == False:
        print('NO')
    else:
        print('YES')

###########################

#def CNT(string,length):
#     result = 0
#     cnt = 0
#     if (length % 2) == 1:
#         return False
#     else:
#         for i in string:
#             if i == '(':
#                 print(i)
#                 result += 1
#                 print(result)
#             else:
#                 print(i)
#                 result -= 1
#                 print(result)
#             if result < 0:
#                 return False
            
#             if (length-1) == cnt:
#                 print(length)
#                 print(i)
#                 if result == 0:
#                     return True
#                 else:
#                     return False
#             cnt += 1
            

# while True:
#     string = str(input("input ()  : "))
#     lenstring = len(string)
#     print(lenstring)
#     if CNT(string,lenstring) == False:
#         print('NO')
#     else:
#         print('YES')
    



  


