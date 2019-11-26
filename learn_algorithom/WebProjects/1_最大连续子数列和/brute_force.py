import math

def BruteForce(x):
    n = len(x)
    s = - math.inf

    for i in range(n):
        temp_s = 0
        for j in range(i, n):
            temp_s += x[j]
            if temp_s > s:
                s = temp_s
                y = x[i:(j+1)]
    return y

if __name__=="__main__":
    x = [4, -3, 5, -2, -1, 2, 6, -2]
    print(x)
    y = BruteForce(x)
    print(BruteForce(x))
    print(sum(y))


