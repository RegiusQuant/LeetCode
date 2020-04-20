# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0005.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        result, _ = self.dfs(root)
        return result

    def dfs(self, node: TreeNode):
        if not node:
            return 0, 0

        timeLeft, sumLeft = self.dfs(node.left)
        timeRight, sumRight = self.dfs(node.right)
        timeCurr, sumCurr = node.val + timeLeft + timeRight, node.val + sumLeft + sumRight

        interLeft, interRight = timeLeft - sumLeft, sumRight - timeRight
        mid = (sumRight - sumLeft) / 2
        if mid < interLeft:
            mid = interLeft
        elif mid > interRight:
            mid = interRight
        timeCurr = min(timeCurr, node.val + max(sumLeft + mid, sumRight - mid))
        return timeCurr, sumCurr


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(4)
    print(solution.minimalExecTime(root))