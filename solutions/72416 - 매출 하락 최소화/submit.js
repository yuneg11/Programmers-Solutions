function solution(sales, links) {
    const count = new Array(sales.length + 1).fill(0);
    const parent = new Array(sales.length + 1);
    const child = new Map();

    for (const [p, c] of links) {
        parent[c] = p;
        count[p]++;
    }
    parent[1] = 0;
    count[0] = 1;

    const q = [];
    for (const [i, v] of count.entries())
        if (v === 0) q.push(i);

    while (count[0]) {
        const i = q.shift(), p = parent[i];
        let sumv = 0, minv = 0;
        if (child.has(i)) {
            sumv = child.get(i).reduce((sum, [_, npick]) => sum + npick, 0);
            minv = child.get(i).reduce((min, [pick, npick]) => Math.min(min, pick - npick), sales[i - 1]);
        }
        const pushv = [sales[i - 1] + sumv, minv + sumv];
        if (!child.has(p)) child.set(p, [pushv]);
        else child.get(p).push(pushv);
        if (--count[p] === 0) q.push(p);
    }

    return Math.min(...child.get(0)[0])
}
