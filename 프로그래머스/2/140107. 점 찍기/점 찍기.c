#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

// 그냥 점들 생성하면서 원점이랑 거리 계산한걸로 조건문 걸어서 필터링 하믄 되겠는걸...?
// 자료형 지정이 큰 걸림돌이었다...
// 그 후엔 자꾸 테스트 3개에서 시간초과 나는데... 이거 for 두번써서 이러는거같음

long long solution(int k, int d) {
    long long answer = 0;
    for (long long i = 0; i <= d / k; i++) {
        long long max_j = sqrt((long long)d * d - (k * i) * (k * i)) / k;
        answer += (max_j + 1);
    }
    return answer;
}