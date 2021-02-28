#include <string>

using namespace std;

int solution(string s) {
    int answer = 0;
    int sign = 1;

    for (size_t i = 0; i < s.size(); i++) {
        if (s[i] == '-') {
            sign = -1;
        } else if (s[i] == '+') {
            sign = 1;
        } else {
            answer = answer * 10 + (s[i] - '0');
        }
    }

    return sign * answer;
}
