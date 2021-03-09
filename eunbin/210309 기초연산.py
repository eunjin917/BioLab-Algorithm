#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())
print(a+b)

#응용 1
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a+b)

#응용 2
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break