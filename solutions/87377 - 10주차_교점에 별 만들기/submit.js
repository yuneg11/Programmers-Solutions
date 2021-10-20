function solution(line) {
    const m = [...line.map(([a, b, e]) => line.map(([c, d, f]) => [b * f - e * d, e * c - a * f, a * d - b * c]))
                      .flat().filter(([x, y, z]) => z && !(x % z || y % z))
                      .map(([x, y, z]) => [x / z, y / z])
                      .reduce((m, v) => m.set(v.join(","), v), new Map()).values()];
    const [[xa, xb], [ya, yb]] = [m.map(v => v[0]), m.map(v => v[1])].map(v => [Math.min(...v), Math.max(...v)]);
    const s = Array(yb - ya + 1).fill(false).map(() => Array(xb - xa + 1).fill(false));
    for (const [x, y] of m) s[yb - y][x - xa] = true;
    return s.map(l => l.map(v => v ? "*" : ".").join(""))
};
