class Solution:
    def numTrees(self, n: int) -> int:
        # 思路：n=0时为空树，因为空树也算是二叉查找树的一种所以个数为1
        # n>=1时，二叉查找树的个数等于根节点左子树个数*根节点右子树个数
        # dp[n]记录0~n对应的二叉查找树的个数
        #
        # dp[0]=1
        # dp[1]=dp[0]*dp[0]
        # n==2时，根节点可以是1和2
        # dp[2]=dp[0]*dp[1]+dp[1]*dp[0]
        # n==3时，根节点可以是1、2、3
        # dp[3]=dp[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]
        #
        # 由此可以推出卡塔兰数列的递推式
        #
        # 加上n=0是n+1种情况
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            for j in range(0, i+1):
                dp[i + 1] += dp[j] * dp[i - j];
        return dp[n]
