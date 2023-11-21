# 分发饼干
# 给小孩分发饼干，每个小孩最多只能给一块饼干
# 每个小孩都有一个胃口值g[i],每块饼干都有一个尺寸值s[j]
# 例子： g = [1,2,3]  s=[1,1] 那自能满足一个小孩，输出 1
# 例子： g = [1,2]  s=[1,2,3] 输出2

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        son = cookie = 0
        while son < n and cookie < m:
            if s[cookie] >= g[son]:
                son = son + 1
            cookie = cookie + 1
        return son


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    Solu = Solution()
    num = Solu.findContentChildren(g, s)
    print(num)
