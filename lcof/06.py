# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午6:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 06.py
# @Desc    : 说明

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.result = []

    def reversePrint(self, head: ListNode) -> List[int]:
        self.helper(head)
        return self.result

    def helper(self, node: ListNode):
        if not node:
            return
        self.helper(node.next)
        self.result.append(node.val)


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    print(solution.reversePrint(head))
