function solution(play, adv, logs) {
    const c = ([h, m, s]) => h * 3600 + m * 60 + s * 1;
    play = c(play.split(":")), adv = c(adv.split(":"))
    logs = logs.map(t => t.split("-").map((v, i) => [c(v.split(":")), i]))
               .flat().sort((a, b) => a[0] - b[0]);

    let v = 0, p = 0, b = Array(play).fill(0);
    for (const [t, m] of logs) {
        if (v) for (let i = p; i < t; i++) b[i] = v;
        v += (m ? -1 : 1), p = t;
    }

    let s = b.slice(0, adv).reduce((a, v) => a + v), mv = s, mi = 0;
    for (let i = 0, j = adv; j < play; i++, j++) {
        s += b[j] - b[i];
        if (s > mv) [mv, mi] = [s, i + 1];
    }

    const f = v => `${Math.floor(v)}`.padStart(2, 0);
    return `${f(mi/3600)}:${f(mi%3600/60)}:${f(mi%60)}`;
}
