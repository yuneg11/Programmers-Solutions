const table = {
    "cpp": 4, "java": 2, "python": 1,
    "backend": 2, "frontend": 1,
    "senior": 2, "junior": 1,
    "chicken": 2, "pizza": 1,
    "-": 7,
}

function preprocess(rows, is_query = false) {
    const processed_rows = [];

    for (const row of rows) {
        const values = row.split(" ").filter(value => value != "and");

        const score = Number(values[values.length - 1]);
        let code = 0;

        for (const value of values.slice(0, -1)) {
            if (is_query) {
                code = (code << 3) + (7 - table[value]); // Bit flip
            } else {
                code = (code << 3) + table[value];
            }
        }

        processed_rows.push([code, score]);
    }

    return processed_rows;
}

function bisect_gt(a, x) {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        let mid = Math.floor((lo + hi) / 2);
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return a.length - lo;
}

function solution(info, query) {
    info = preprocess(info);
    query = preprocess(query, true);

    const info_index = new Map();

    for (const [code, score] of info) {
        // Behave likes python defaultdict
        if (!info_index.has(code)) {
            info_index.set(code, []);
        }

        info_index.get(code).push(score);
    }

    const sorted_info_index = [];

    for (const [code, scores] of info_index.entries()) {
        sorted_info_index.push([code, scores.sort((a, b) => a - b)]);
    }

    const results = [];

    for (const [qcode, qscore] of query) {
        let count = 0;

        for (const [icode, iscores] of sorted_info_index) {
            if (!(qcode & icode)) {
                count += bisect_gt(iscores, qscore);
            }
        }

        results.push(count);
    }

    return results;
}
