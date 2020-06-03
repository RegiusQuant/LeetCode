# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0328.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        oddHead, evenHead = ListNode(), ListNode()
        oddCurr, evenCurr = oddHead, evenHead
        count, curr = 1, head
        while curr:
            if count % 2:
                oddCurr.next = curr
                oddCurr = oddCurr.next
            else:
                evenCurr.next = curr
                evenCurr = evenCurr.next
            curr = curr.next
            count += 1

        evenCurr.next = None
        oddCurr.next = evenHead.next
        return oddHead.next
