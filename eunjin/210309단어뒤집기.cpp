// 단어 뒤집기
// https://www.acmicpc.net/problem/9093
// 2021.03.07



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
        char line[1001];
        cin.getline(line, 1001); // 한 줄만 입력받음 (cin.ignore() 필요X)

        for (int j = 0; j <= strlen(line); j++)
        {
            if (line[j] == ' ' || j == strlen(line))
            {
                for (int k = j - 1; k >= 0; k--)
                {
                    if (line[k] == ' ')
                    {
                        cout << ' ';
                        break;
                    }
                    cout << line[k];
                }
            }
        }
         cout << '\n';
    }
    return 0;
}