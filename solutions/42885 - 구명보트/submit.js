function solution(p, l) {
    p = p.sort((a, b) => a - b);
    let i, j, n = p.length;
    for (i = 0, j = n - 1; i <= j; i += p[i] + p[j] <= l, j--);
    return n - j - 1;
}
