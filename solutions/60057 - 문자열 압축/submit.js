function solution(s) {
    let m = s.length;

    for (let i = 1; i <= s.length / 2; i++) {
        let l = 0, prev = "", cnt = 1, cur;

        for (let j = 0; j < s.length; j += i) {
            cur = s.slice(j, j + i);
            if (prev === cur) {
                cnt++;
            } else {
                l += prev.length + (cnt > 1 ? cnt.toString().length : 0);
                prev = cur;
                cnt = 1;
            }
        }

        l += cur.length + (cnt > 1 ? cnt.toString().length : 0);
        m = m < l ? m : l;
    }

    return m;
}
