long long solution(int p, int m, int c) {
    auto t = p * (c + 1LL) * c / 2;
    return t > m ? t - m : 0;
}
