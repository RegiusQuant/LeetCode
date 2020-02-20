# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 上午11:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 22.py
# @Desc    : 说明

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        while fast:
            fast = fast.next
            if k == 0:
                slow = slow.next
            else:
                k -= 1
        return slow


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print(solution.getKthFromEnd(head, 1).val)
    print(solution.getKthFromEnd(head, 3).val)
