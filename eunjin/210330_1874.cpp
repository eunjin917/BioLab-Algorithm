// 스택 수열
// https://www.acmicpc.net/problem/1874
// 2021.03.29

// Q. 스택으로 임의의 수열 만들 수 있는지 계산
// - 오름차순으로 push할 것
// - pop하여 수열 만들 것

// 1try : 성공, But 이해 어려우니 다시 해볼 것

#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int suyeol[100001]; // 수열의 최대값
	int stack[100001]; // 스택의 최대값 (수열 원소의 최대값이 n일 경우가 최악의 경우)
	char cal[200001] = { '\0' }; // +- 출력하기 (1~n push하고 n~1 pop 경우가 최악의 경우)
	int calindex = 0;

	for (int i = 0; i < n; i++)
	{
		cin >> suyeol[i];
	}

	int maxtop = 0; // 스택 최대 top값
	int size = 0; // 현재 스택의 크기

	for (int i = 0; i < n; i++) // 수열 원소 하나씩 기준
	{
		while (suyeol[i] > maxtop) // 아직 기준까지 push해본 적 없으면 기준 도달할때까지
		{
			stack[size++] = ++maxtop;	// maxtop+1 push하기
			cal[calindex++] = '+';
		}
		if (suyeol[i] == stack[size - 1]) // 기준 도달하면
		{
			size--; // pop해서 수열 만들기
			cal[calindex++] = '-';
		}
		else // 기준 도달X경우 = 수열 만들기 불가능한 경우
		{
			cout << "NO";
			return 0;	// 종료
		}
	}

	for (int i = 0; i < strlen(cal); i++)	// 계산 과정 출력
	{
		cout << cal[i] << '\n';
	}
}