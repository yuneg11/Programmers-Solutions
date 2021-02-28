function solution(d) {
    let c = 1, o = [, 1, 1, 1], s = [, 0, 0, 0], b = [, 1, 1, 1];

    for (let v of d)
        if ("SDT".includes(v))
            b[c++] = " SDT".indexOf(v);
        else if (v == "#")
            o[c-1] = -1;
        else if (v == "*")
            [o[c-2], o[c-1]] = [o[c-2] * 2, o[c-1] * 2];
        else
            s[c] = s[c] * 10 + Number(v);

    return o[1] * (s[1] ** b[1]) + o[2] * (s[2] ** b[2]) + o[3] * (s[3] ** b[3]);
}
