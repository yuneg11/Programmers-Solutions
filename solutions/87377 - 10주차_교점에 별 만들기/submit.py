solution = lambda line: (
    lambda rx, ry, s: [
        "".join("*" if (x, y) in s else "." for x in rx) for y in ry
    ]
)(
    *(
        lambda i, j, s: (
            range(min(i), max(i) + 1),
            range(max(j), min(j) - 1, -1),
            s,
        )
    )(
        *(lambda s: ([v for v, _ in s], [v for _, v in s], s))(
            {
                (x // z, y // z)
                for x, y, z in [
                    (b * f - e * d, e * c - a * f, a * d - b * c)
                    for (a, b, e) in line
                    for (c, d, f) in line
                ]
                if z and not x % z and not y % z
            }
        )
    )
)
