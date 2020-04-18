# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午3:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import deque

class Solution:
    def minJump(self, jump: List[int]) -> int:
        visit = [False] * len(jump)
        queue = deque()
        queue.append((0, 0))
        visit[0] = True

        p = 0
        while queue:
            i, s = queue.popleft()
            if i + jump[i] >= len(jump):
                return s + 1
            while p <= i:
                if not visit[p]:
                    queue.append((p, s + 1))
                    visit[p] = True
                p += 1
            if not visit[i + jump[i]]:
                queue.append((i + jump[i], s + 1))
                visit[i + jump[i]] = True
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minJump([2, 5, 1, 1, 1]))
    print(solution.minJump([2, 4, 1, 1, 3, 1]))
    print(solution.minJump([1, 1, 1, 1, 1, 1]))
    print(solution.minJump([6, 1, 1, 10, 1, 1, 1, 1, 1]))
    print(solution.minJump([1, 1, 1, 10, 2, 1, 1, 1, 1]))
    print(solution.minJump([10]))
    print(solution.minJump([1, 2, 10, 2, 1, 2]))
    print(solution.minJump([1, 2, 3, 4, 5, 6]))
    print(solution.minJump([4, 6, 2, 1, 1, 1, 1, 1]))