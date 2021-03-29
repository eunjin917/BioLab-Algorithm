#include <stdio.h>
#include <ctype.h>
#define _CRT_SECURE_NO_WARNINGS
int count_word(const char* s);

int main(void)
{
	char sentence[100];
	printf("영어로 이루어진 문자열을 입력하시오.\n");
	gets_s(sentence);
	printf("%d", count_word(sentence));
	return 0;
}

int count_word(const char* s) {
	int i;
	int wc = 0, waiting = 1;	
	for (i = 0; s[i] != NULL; i++) {
		if (isalpha(s[i])) {	// 알파벳일 때 실행
			if (waiting) {
				wc++;	// 단어의 개수 +1
				waiting = 0;	// 한 단어를 여러 개의 단어로 인식하는 것 방지
			}
		}
		else
			waiting = 1;	// 공백이 나온 후 다시 단어를 셀 수 있게 한다.
	}
	return wc;
}