#include <string>

using namespace std;

int solution(string word) {
    string v = string("AEIOU");
    int a = word.size();

    for(int i = 0, b = 1; i < word.size(); i++, b *= 5)
        a += v.rfind(word[i]) * 781 / b;

    return a;
}
