# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 上午10:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 33.py
# @Desc    : 说明

from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True

        pos = -1
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] < postorder[-1]:
                pos = i
                break
        left = postorder[: pos + 1]
        right = postorder[pos + 1: -1]
        for x in left:
            if x > postorder[-1]:
                return False
        return self.verifyPostorder(left) and self.verifyPostorder(right)


if __name__ == '__main__':
    solution = Solution()
    print(solution.verifyPostorder([1, 6, 3, 2, 5]))
    print(solution.verifyPostorder([1, 3, 2, 6, 5]))
    print(solution.verifyPostorder([5, 4, 3, 2, 1]))