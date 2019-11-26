

def kruskal(V, E):
    n = len(V)
    represents = list(range(n)) # represents[i] 表示结点i的代表元
    dict_represents = dict(zip(V, [[v] for v in V])) # k:v，代表以结点k为代表元的结点集合为v 初始化为 {0: [0], 1: [1], 2: [2], ..}，表示各个节点开始时以自己为代表元
    E.sort()

    T = []
    for e in E:
        r1, r2 = represents[e[1]], represents[e[2]]
        if r1 != r2:
            T.append(e)
            if r1 < r2:
                dict_represents[r1].extend(dict_represents[r2])
                for v in dict_represents[r2]:
                    represents[v] = r1
                del dict_represents[r2]
            elif r1 > r2:
                dict_represents[r2].extend(dict_represents[r1])
                for v in dict_represents[r1]:
                    represents[v] = r2
                del dict_represents[r1]
    return T

if __name__ == "__main__":
    def test():
        n = 7
        V = list(range(n))
        # (5, 0, 1) 表示0结点和1结点有一条边，其权重为5
        E = [(5, 0, 1), (11, 0, 2), (5, 0, 3), (3, 1, 3), (9, 1, 4), (7, 1, 6), (7, 2, 3), (6, 2, 5), (20, 3, 6), (8, 4, 6), (8, 5, 6)]
        print(kruskal(V, E))
    test()
