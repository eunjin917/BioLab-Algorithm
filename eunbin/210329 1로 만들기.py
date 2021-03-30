#1463

n = int(input())

dp = [0, 0]                                 #다이나믹 프로그래밍 사용

for i in range(2, n+1):
    
    dp.append(dp[i-1] + 1)                  # 1을 뺏을 경우의 수 저장

    if i % 2 == 0:                          #2로 나눠질 경우
        dp[i] = min(dp[i], dp[i//2] + 1)    #1을 뺏을 경우의 수와 비교하여 최솟값 저장

    if i % 3 == 0:                          #3으로 나눠질 경우
        dp[i] = min(dp[i], dp[i//3] + 1)    #1을 뺏을 경우의 수와 비교하여 최솟값 저장

print(dp[n])