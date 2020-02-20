# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 下午12:39
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
                curr = curr.next
            else:
                curr.next, l2 = l2, l2.next
                curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return head.next


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print(solution.mergeTwoLists(l1, l2).val)
