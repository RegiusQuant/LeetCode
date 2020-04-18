# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午12:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0234.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        if fast:
            slow = slow.next
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(0)
    temp = head
    for x in [1, 2, 3, 3, 1]:
        temp.next = ListNode(x)
        temp = temp.next
    print(solution.isPalindrome(head.next))
