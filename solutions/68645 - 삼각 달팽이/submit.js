function solution(n) {
    let result = [];
    const rng = (l, t, u) => l <= t && t <= u && u < n;
    const cnt = (i, d, p) => (2*n-3*i+1) * 3/2*i + (n-3*i-1) * d + p;

    for (let x = 0; x < n; x++)
        for (let y = 0; y <= x; y++)
            result.push(rng(n-x-1, y, 2*x-n) ? cnt(n-x-1, 1, y-n+x+2)
                       : rng(2*x-2*y+1, x, n-x+y-1) ? cnt(x-y, 2, n-2*x+y)
                       : cnt(y, 0, x-2*y+1));
    return result;
}
