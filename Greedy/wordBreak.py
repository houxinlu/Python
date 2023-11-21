# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

class Solution:
    def wordBreak(self, s: str, wordDict):
        l = len(s)
        wordMap = {}

        dp = [False] * (l + 1)
        dp[0] = True

        for i in range(l):
            for j in range(i + 1, l + 1):
                subWord = s[i:j]
                if (subWord in wordDict) and dp[i]:
                    dp[j] = True
        return dp[-1]
