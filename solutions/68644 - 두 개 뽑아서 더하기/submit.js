function solution(numbers) {
    const set = new Set();
    for (let [i, a] of numbers.entries())
        for (let b of numbers.slice(i + 1))
            set.add(a + b);
    return Array.from(set).sort((a, b) => a - b);
}
