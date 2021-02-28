function solution(b, m) {
    let s = [0];

    b = b.map((_, c) => b.map(row => row[c])).map(r => r.filter(x => x));    
    m = m.map(i => b[i - 1].shift()).filter(v => v);

    for (let v of m)
        if (v == s[s.length - 1]) s.pop();
        else s.push(v)

    return m.length - s.length + 1;
}
