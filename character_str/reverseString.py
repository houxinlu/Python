# 反转字符串，使用O(1)的额外空间解决这个问题
# O(1)就是不借助任何外部空间
# 示例：输入 s=["h","e","l","l","o"] 输入：["o","l","l","e","h"]

class Solution:
    def reverseString(self, s):
        if len(s) <= 1:
            return s
        left = 0
        right = len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1
        return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solu = Solution()
    print(Solu.reverseString(s))
