let solution = word => [...word].reduce((a, c, i) => a + "AEIOU".indexOf(c) * ~~(781 / 5 ** i) + 1, 0);
