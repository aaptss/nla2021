def binomialCoeff(n, k):
    C = [[0 for i in range(k + 1)]
         for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]


# Function to return the maximum
# value in the nth level
# of the Pascal's triangle
def findMax(n):
    return binomialCoeff(n, n // 2)


# Driver code
n = 30
vals = []
for i in range(n):
    vals.append(binomialCoeff(n,i))

print(sum(vals))


