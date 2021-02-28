const solution = (n, a, b) => a.map((v, i) => (v | b[i]).toString(2).padStart(n, 0).replace(/./g, c => c > 0 ? "#" : " "));
