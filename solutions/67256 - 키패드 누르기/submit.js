const solution = (n, h) =>
    n.map(x => x ? [Math.floor((x - 1) / 3), (x - 1) % 3] : [3, 1])
     .map(((l, r, d, L = "L", R = "R") => v => (
        v[1] == 0 ? (l = v, L) : v[1] == 2 ? (r = v, R) :
        d(v, l) < d(v, r) ? (l = v, L) : d(v, l) > d(v, r) ? (r = v, R) :
        h == "left" ? (l = v, L) : (r = v, R))
     )([3, 0], [3, 2], ([a, b], [c, d]) => Math.abs(a-c) + Math.abs(b-d)))
     .join("");
