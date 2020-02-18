# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 上午9:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 18.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        prev, curr = temp, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                break
            prev, curr = prev.next, curr.next
        return temp.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    print(solution.deleteNode(head, 5).next.val)
