function solution(n) {
    let d = n.split("").map(c => c.charCodeAt(0))
                       .map(v => v > 78 ? 91 - v : v - 65);
    let e = d.reduce((a, v) => a + (v > 0), 0);
    let l = n.length;
    let m = l - 1;

    for (let i = 0, j, r; i < l; i++) {
        e -= d[i] > 0;
        for (j = 1, r = e; r > 0; j++) r -= d[l - j] > 0;
        m = m >= i + i + j ? i + i + j - 1 : 
            m >= i + j + j ? i + j + j - 1 : m;
    }

    return m + d.reduce((a, v) => a + v);
}
