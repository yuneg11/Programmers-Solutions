const solution = n => (n > 3 ? solution(~~((n - 1) / 3)) : '') + '412'[n % 3];
