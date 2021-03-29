#include <stdio.h>
#include<stdlib.h>
int startR(const char *s, int m, int n);
int startL(const char *s, int m, int n);

int main(void) {
	int i=0, j=0;
	int right=0, left=0;
	char str[100];
	printf("괄호 문자열을 입력하시오");
	gets_s(str);	// 문자열 입력받기
	while (str[j] != '\n') {
		if (str[j] == '(') {
			right = 1;
			j = startR(str, right, left); // '('로 시작하면 right 1 높이고 개수 세기 시작
		}
		if (str[j] == ')') {
			left = 1;
			j = startL(str, right, left); // ')'로 시작하면 left 1 높이고 개수 세기 시작
		}
	}
	printf("VPS가 맞습니다.");
	return 0;
}

int startR(const char* s, int m, int n) {
	int k = 1;
	while (s[k] == '(') {
		m++;
		k++;
	}
	while (s[k] == ')') {
		n++;
		k++;
	}
	if (m != n) {
		printf("VPS가 아닙니다!");
		exit(-1);
	}
	return k;
}

int startL(const char* s, int m, int n) {
	int k = 1;
	while (s[k] == ')') {
		n++;
		k++;
	}
	while (s[k] == '(') {
		m++;
		k++;
	}
	if (m != n) {
		printf("VPS가 아닙니다!");
		exit(-1);
	}
	return k;
}