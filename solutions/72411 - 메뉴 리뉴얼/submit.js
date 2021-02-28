// From python itertools.combinations
function* combinations(a, r) {
    const n = a.length;
    if (r > n) return;
    const indices = [...Array(r).keys()];
    yield indices.map(v => a[v]).join("");
    for (let i;;) {
        for (i = r - 1; i >= 0; i--)
            if (indices[i] != i + n - r) break;
        if (i == -1) return;
        indices[i] += 1;
        for (let j = i + 1; j < r; j++) 
            indices[j] = indices[j - 1] + 1
        yield indices.map(v => a[v]).join("");
    }
}

function solution(orders, course) {
    const d = new Map(), m = new Map();
    for (const order of orders) {
        for (const n of course) {
            for (const v of combinations(order.split("").sort(), n)) {
                if (!d.has(v)) d.set(v, 0);
                if (!m.has(n)) m.set(n, 2);
                const c = d.get(v) + 1, x = m.get(n);
                d.set(v, c); m.set(n, x > c ? x : c);
            }
        }
    }
    return Array.from(d.entries()).filter(([v, c]) => c == m.get(v.length)).map(([v, c]) => v).sort();
}
