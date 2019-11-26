
INF = 9999

def flody(w):
    n = len(w)

    d = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (d[i][j] > d[i][k] + d[k][j]):
                    d[i][j] = d[i][k] + d[k][j]
    return d


if __name__ == "__main__":
    w = [   
        [0, 2, 6, 4],
        [INF, 0, 3, INF],
        [7, INF, 0, 1],
        [5, INF, 12, 0]
        ]

    import numpy as np
    print(np.array(flody(w)))
