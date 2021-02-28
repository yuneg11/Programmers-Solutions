function isCorrect(p) {
    let stack = 0;
    for (let c of p) {
        stack += c === "(" ? 1 : -1;
        if (stack === -1) return false;
    }
    return stack === 0;
}

function solution(p) {
    if (p === "") {
        return "";
    } else {
        let a = 0, b = 0;
        for (let c of p) {
            if (c === "(") a++;
            else b++;

            if (a === b) break;
        }

        const [u, v] = [p.slice(0, a + b), p.slice(a + b)];
        if (isCorrect(u)) {
            return u.concat("", solution(v));
        } else {
            return [
                "(", solution(v), ")",
                u.slice(1, u.length - 1)
                 .replace(/./g, c => c === "(" ? ")" : "(")
            ].join("");
        }
    }
}
