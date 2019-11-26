

def LCS_LENGTH(x, y):

    n, m = len(x), len(y)
    c = [[None] * (m+1) for _ in range(n+1)]
    z = [[None] * m for _ in range(n)]

    for i in range(n+1):
        c[i][0] = 0
    for j in range(m+1):
        c[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
           
            if x[i-1] == y[j-1]:
                # 注意到此时lcs的长度加1，因此只需要找到 `left_up` 状态的就可以得到lcs
                c[i][j] = c[i-1][j-1] + 1
                z[i-1][j-1] = 'left_up'
            else:
                if c[i-1][j] > c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    z[i-1][j-1] = 'up'
                else:
                    c[i][j] = c[i][j-1]
                    z[i-1][j-1] = 'left'
    return c, z

def LCS(x, y):

    c, z = LCS_LENGTH(x, y)

    # 从z中构造出子序列
    n, m = len(x), len(y)
    lcs = []

    i, j = n-1, m-1

    while i >= 0 and j >= 0:

        if z[i][j] == 'up':
            i -= 1
        if z[i][j] == 'left':
            j -= 1
        if z[i][j] == 'left_up':
            lcs.insert(0, x[i])
            i -= 1
            j -= 1
    return lcs

if __name__== "__main__":

    def test():
        x = 'belong'
        y = 'cnblogs'

        c, z = LCS_LENGTH(x, y)
        
        for _ in z:
            print(_)
        
        for _ in c:
            print(_)

        print(LCS(x, y))
    test()


