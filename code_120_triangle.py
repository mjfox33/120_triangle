class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        dp = [0]*n
        dp[0] = triangle[0][0]
        for i in range(1,n):
            n2 = len(triangle[i])
            dp[n2-1] = dp[n2-2] + triangle[i][n2-1]
            for j in range(n2-2, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp) 