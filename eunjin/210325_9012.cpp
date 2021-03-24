// 괄호
// https://www.acmicpc.net/problem/9012
// 2021.03.24

#include <iostream>
#include <string.h>
using namespace std;

// VPS = 올바른 괄호 문자열
// 1) VPS = (VPS)
// 2) VPS = VPSVPS (접합)

int main()
{
    // 테스트케이스
    int T;
    cin >> T;
    cin.ignore();
    for (int i = 0; i < T; i++)
    {
        char line[51]; // 괄호문자열 : 길이 2이상 50이하
        cin.getline(line, 51);

        int count = 0;  // 스택을 count로 구현
        string isVPS = ""; // VPS 여부
        
        for (int j = 0; j < strlen(line); j++) // 괄호문자열 단어 하나하나 확인
        {
            // 해당 단어 확인
            if (line[j] == '(') // ( 이면
            {
                count++;
            }
            else // ) 이면
            {
                count--;
            }

            // 그때 그때 count 확인
            if (count < 0) // )가 더 많은 경우 : VPS X
            {
                isVPS = "NO";
                break;
            }
        }

        // for문 종료 후 count 확인
        if (count == 0) // (와) 개수 같은 경우 : VPS O
        {
            isVPS = "YES";
        }
        else // )가 더 많은 경우 : VPS X
        {
            isVPS = "NO";
        }
        
        // YES or NO 출력
        cout << isVPS << '\n';
    }
}