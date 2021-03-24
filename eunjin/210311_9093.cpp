// 단어 뒤집기
// https://www.acmicpc.net/problem/9093
// 2021.03.07

// 1try : 스택(배열)에 담고 다시 꺼내는 형식이라 비효율적

// #include <iostream>
// #include <string.h> // strlen 쓸때 필요
// using namespace std;

// int main()
// {
//     int T;s
//     cin >> T;
//     cin.ignore(); // 입력버퍼 비우기

//     for (int i = 0; i < T; i++)
//     {
//         char line[1001];
//         cin.getline(line, 1001); // 한 줄만 입력받음 (cin.ignore() 필요X)
//         int idx = 0;

//         for (int j = 0; j <= strlen(line); j++)
//         {
//             char word[21];
//             if (line[j] == ' ' || j == strlen(line))
//             {
//                 for (int k = 0; k < idx; k++)
//                     cout << word[idx - k - 1];
//                 idx = 0;

//                 if (j != strlen(line))
//                     cout << ' ';
//             }
//             word[idx++] = line[j];
//         }
//         cout << '\n';
//     }
//     return 0;
// }



// 2try : 배열 사용 X, 바로 거꾸로 출력하기

#include <iostream>
#include <string.h> // strlen 쓸때 필요
using namespace std;

int main()
{
    int T;
    cin >> T;
    cin.ignore(); // 입력버퍼 비우기

    for (int i = 0; i < T; i++)
    {
        char line[1001]; // 문장 최대길이 1000이므로 \0 자리 포함 1001
        cin.getline(line, 1001); // 한 줄만 입력받음 (cin.ignore() 필요X)

        for (int j = 0; j <= strlen(line); j++) // 문장길이+1만큼 확인하기 (입력 길이가 3이면 \0포함 길이가 4 => 4번 for문돌리기)
        {
            if (line[j] == ' ' || j == strlen(line)) // 공백이거나, 제일 마지막이면
            {
                for (int k = j - 1; k >= 0; k--) // 뒤에서부터 하나씩
                {
                    if (line[k] == ' ') // 공백 부분이었으면 공백 넣기
                    {
                        cout << ' ';
                        break;
                    }
                    cout << line[k]; // 해당 부분 출력하기
                }
            }
        }
        cout << '\n'; // 테스트케이스 끝나면 엔터
    }
    return 0;
}