
def rod_cutting(n):

    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    if n ==1 or n==2:
        return p[n]
    else:
        r = [0] * (n+1)
        r[0] = p[0]
        r[1] = p[1]

        for i in range(2, n+1):
            r[i] = p[i]
            for j in range(1, i//2+1):
                tmp = r[j] + r[i-j]
                if tmp > r[i]:
                    r[i] = tmp
                    
        return r[-1]

if __name__ == "__main__":
    for i in range(1, 11):
        print(rod_cutting(i))
