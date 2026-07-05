def zigzag(n, k):

    dp = [[0 for x in range(k+1)] for y in range(n+1)]

    dp[0][0] = 1

    for i in range(1, n+1):

        dp[i][0] = 0

    for i in range(1, n+1):

        for j in range(1, k+1):

            dp[i][j] = (dp[i][j - 1] + dp[i - 1][i - j])

    return dp[n][k]

if __name__ == '__main__':

    n = int(input('Enter n :\t'))

    k = int(input('Enter k :\t'))

    print(zigzag(n, k))