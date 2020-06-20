# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 下午7:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1028.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, p = [], 0
        while p < len(S):
            level, value = 0, 0
            while S[p] == '-':
                level += 1
                p += 1
            while p < len(S) and S[p].isdigit():
                value = value * 10 + int(S[p])
                p += 1
            node = TreeNode(value)
            if level == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                stack = stack[:level]
                stack[-1].right = node
            stack.append(node)
        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.recoverFromPreorder("1-2--3--4-5--6--7"))
