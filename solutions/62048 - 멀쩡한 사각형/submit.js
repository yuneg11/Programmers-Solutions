function solution(w, h) {
    let s = 0;
    for (let j = 1; j <= w; j++)
        s += Math.ceil(h * j / w) - Math.floor(h * (j - 1) / w);
    return BigInt(w) * BigInt(h) - BigInt(s);
}
