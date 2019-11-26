
class SStack:

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def push(self, val):
        self._elems.append(val)

    def pop(self):
        return self._elems.pop()

    def top(self):
        return self._elems[-1]


class GraphError(ValueError):
    pass

class Graph:

    def __init__(self, mat, unconn=0):
        self._vnum = len(mat) # 结点个数
        for x in mat:
            if len(x) != self._vnum:
                raise GraphError('Argument for Graph')

        self._mat = [x[:] for x in mat]
        self._unconn = unconn

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        """
        检查v是否是一个合理的顶点
        :param v:
        :return:
        """
        return v < 0 or v >= self._vnum


    def add_vertex(self):
        raise GraphError('Adj Matrix does not support add_vertex')

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('Invalid vertet')

        self._mat[vi][vj] = val

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError('Invalid vertex')

        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        return [(i, row[i]) for i in range(len(row)) if row[i]!=unconn]



class GraphAL(Graph):

    def __init__(self, mat=[], unconn=0):
        self._vnum = len(mat)
        self._unconn = unconn

        for x in mat:
            if len(x) != self._vnum:
                raise GraphError("mat is not a square matrix")
        self._mat = [Graph._out_edges(row, self._unconn) for row in mat]

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum -1


    def add_edge(self, vi, vj, val=1):

        if self._vnum == 0:
            raise GraphError('Cannot add edge to an empty graph')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('Invalid vertex vi: %s or vj: %s'%(vi, vj))

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i][1] = val
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('Invalid vertex vi: %s or vj: %s'%(vi, vj))
        for x in self._mat[vi]:
            if x[0]==vj:
                return x[1]
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError('Invalid vertex vi: %s'%vi)
        return self._mat[vi]

def DFS_graph(graph, v0):
    """
    教材p237的算法，略有改变
    :param graph:
    :param v0:
    :return:
    """
    vnum = graph.vertex_num()
    visisted = [0] * vnum
    DFS_seq = []
    st = SStack()

    st.push((0, graph.out_edges(v0)))
    visisted[v0] = 1
    DFS_seq.append(v0)

    while not st.is_empty():
        index, edges = st.pop()
        while index < len(edges):
            vi = edges[index][0]
            if visisted[vi] == 0:
                visisted[vi] = 1
                st.push((index+1, edges))
                st.push((0, graph.out_edges(vi)))
                DFS_seq.append(vi)
                break
            index += 1

    return DFS_seq

def DFS_graph_recrusive(graph, v0):

    DSF_seq = []

    def dfs(graph, v):
        nonlocal DSF_seq # 由于 DSF_seq 是列表，可变对象，因此可以不使用 nonlocal 也可以
        for u, _ in graph.out_edges(v):
            if u not in DSF_seq:
                DSF_seq.append(u)
                dfs(graph, u)

    DSF_seq.append(v0)
    dfs(graph, v0)
    return DSF_seq


def BFS_graph(graph, v0):
    vnum = graph.vertex_num()
    visisted = [0] * vnum
    l = []

    queue = []
    queue.append(v0)

    while queue:
        vi = queue.pop(0)
        if visisted[vi] == 0:
            visisted[vi] = 1
            l.append(vi)
        for v, _ in graph.out_edges(vi):
            if visisted[v] == 0:
                queue.append(v)
    return l


# def DFS_graph(graph, v0):
#     """
#     自己想的，没有书的那个好。主要是没有想到像书上那样直接将 out_edges的结果入栈
#     :param graph:
#     :param v0:
#     :return:
#     """
#     vnum = graph.vertex_num()
#     visisted = [0] * vnum
#     l = []
#     st = SStack()
#
#     st.push((v0, 0))
#
#     while not st.is_empty():
#         vi, vj = st.pop()
#         if visisted[vi] == 0:
#             l.append(vi)
#             visisted[vi] = 1
#         while vj < vnum:
#             if graph.get_edge(vi, vj) != 0 and visisted[vj] == 0:
#                 st.push((vi, vj+1))
#                 st.push((vj, 0))
#                 break
#             vj += 1
#     return l

def testDFS():

    print(testDFS.__name__)
    a, b, c, d, e, f, g = 0, 1, 2, 3, 4, 5, 6
    mat = []
    for i in range(7):
        mat.append([0] * 7)
    mat[a][d] = 3
    mat[a][c] = 6
    mat[b][a] = 11
    mat[b][c] = 4
    mat[b][f] = 7
    mat[c][b] = 3
    mat[c][e] = 5
    mat[d][e] = 5
    mat[e][g] = 9
    mat[f][g] = 10

    graph = GraphAL(mat)

    d = dict(zip(range(7),'abcdefg'))
    print([d[key] for key in DFS_graph(graph, 0)])

def testBFS():
    # G8
    print(testBFS.__name__)

    a, b, c, d, e, f, g = 0, 1, 2, 3, 4, 5, 6
    mat = []
    for i in range(7):
        mat.append([0] * 7)

    mat[a][b] = 7
    mat[a][c] = 7
    mat[a][d] = 9


    mat[b][d] = 3
    mat[b][e] = 6
    mat[b][g] = 5

    mat[c][d] = 14
    mat[c][f] = 11

    mat[d][g] = 20

    mat[e][g] = 8

    mat[f][g] = 6

    graph = GraphAL(mat)

    d = dict(zip(range(7),'abcdefg'))
    print([d[key] for key in BFS_graph(graph, 0)])

def testDFS_recrusive():

    print(testDFS.__name__)
    a, b, c, d, e, f, g = 0, 1, 2, 3, 4, 5, 6
    mat = []
    for i in range(7):
        mat.append([0] * 7)
    mat[a][d] = 3
    mat[a][c] = 6
    mat[b][a] = 11
    mat[b][c] = 4
    mat[b][f] = 7
    mat[c][b] = 3
    mat[c][e] = 5
    mat[d][e] = 5
    mat[e][g] = 9
    mat[f][g] = 10

    graph = GraphAL(mat)

    d = dict(zip(range(7),'abcdefg'))
    print([d[key] for key in DFS_graph(graph, 0)])


if __name__ == '__main__':
    # 正确的顺序应该是 ['a', 'c', 'b', 'f', 'g', 'e', 'd']
    testDFS()
    testDFS_recrusive()
    testBFS()

