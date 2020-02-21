# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 上午11:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 24.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(solution.reverseList(head))
