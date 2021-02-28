const solution = (n, s) =>
    [...Array(n).keys()]
        .map(i => s.filter(x => x == i + 1).length)
        .map((a => v => (a -= v) / v)(s.length))
        .map((i, v) => [i, v])
        .sort((a, b) => a[0] - b[0])
        .map(e => e[1] + 1);
