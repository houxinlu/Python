# 无重复字符的最长字串
# 给定一个字符串，请找出其中不含有重复字符的最长字串的长度
# 输入：s = "abcabcbb"     输出:3，因为其无重复最长字串是"abc",其长度为3
# 提解：使用滑动窗口，使用一个临时数组的大小，暂存数组大小
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        tem = []
        max_len = 0
        for i in range(len(s)):
            while s[i] in tem:
                tem.remove(s[left])
                left = left + 1
            tem.append(s[i])
            if len(tem) > max_len:
                max_len = len(tem)
        return max_len


if __name__ == '__main__':
    a = "abcabcab"
    Solu = Solution()
    print(Solu.lengthOfLongestSubstring(a))
