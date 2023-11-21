# 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 输入：n = 2，输出：2，解释：有两种方法可以爬到楼顶

class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        sum, a, b = 1, 0, 0
        for i in range(n):
            a = b
            b = sum
            sum = a + b
        return sum
