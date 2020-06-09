# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        head = temp

        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    print(solution.removeNthFromEnd(head, 1))
