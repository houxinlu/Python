# 二叉树的右视图
# 给定一个二叉树的根节点root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值
# 示例：输入：[1,2,3,null,5,null,4] ，输出 [1,3,4]
#    1
#  2   3
#   5    4
# 写此题之前，我们先熟悉二叉树的四种遍历方式：根序遍历，中序遍历，后序遍历和层序遍历
# 这道题，1. 使用dfs深度有限遍历，先遍历right孩子，则就是右视图
# 2. 使用层序遍历，然后输出层序遍历的最后一个值，则就是右视图
# dfs写起来更简单，因为每次遍历的先手都是右字数的root，把它推进属组中即可

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        res = []

        def dfs(root, depth):
            if root == None:
                return
            if depth == len(res):
                res.append(root.val)
            depth = depth + 1
            dfs(root.right, depth)
            dfs(root.left, depth)

        dfs(root, 0)
        return res

