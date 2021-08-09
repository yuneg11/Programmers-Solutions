let solution = scores =>
    (scores[0].map((_, c) => scores.map(r => r[c])))
        .map((s, i) => [...s.splice(i, 1), s])
        .map(([m, s]) => Math.min(...s) <= m && m <= Math.max(...s) ? [m, ...s] : s)
        .map(s => "FDDCBAA"[Math.max(parseInt(s.reduce((a, c) => a + c) / s.length / 10) - 4, 0)])
        .join("")
