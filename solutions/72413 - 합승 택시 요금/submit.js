function solution(n, s, a, b, fares) {
    const min = (a, b) => a < b ? a : b, inf = 100000000;
    let d = Array(n).fill(0).map(() => Array(n).fill(inf)), l;
    for (const [t, f, v] of fares)
        d[t - 1][f - 1] = d[f - 1][t - 1] = v;
    for (let t = 0; t < n; t++)
        d[t][t] = 0;
    for (let k = 0; k < n; k++)
        for (let i = 0; i < n; i++)
            for (let j = 0; j < n; j++)
                if (d[i][j] > (l = d[i][k] + d[k][j]))
                    d[i][j] = l;
    s--; a--; b--;
    return [...Array(n).keys()].reduce((m, k) => min(m, d[s][k] + d[k][a] + d[k][b]), inf);
}
