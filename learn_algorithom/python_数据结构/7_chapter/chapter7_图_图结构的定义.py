

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

def testGraph():
    a, b, c, d, e, f, g = 0, 1, 2, 3, 4, 5, 6
    mat = []
    for i in range(7):
        mat.append([0]*7)
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
    print(graph._mat)
    for v, val in graph.out_edges(0):
        print(v, val)

def testGraphAL():
    a, b, c, d, e, f, g = 0, 1, 2, 3, 4, 5, 6
    mat = []
    for i in range(7):
        mat.append([0]*7)
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
    print(graph._mat)
    for v, val in graph.out_edges(0):
        print(v, val)

if __name__ == '__main__':

    testGraph()
    # testGraphAL()

