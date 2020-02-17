# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 上午9:45
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 13.py
# @Desc    : 说明

from collections import deque


class Solution:
    def countBits(self, x):
        result = 0
        while x:
            result += x % 10
            x //= 10
        return result

    def movingCount(self, m: int, n: int, k: int) -> int:
        grid, q = set(), deque()
        q.append((0, 0))
        while q:
            x, y = q.popleft()
            if x < 0 or x >= m or y < 0 or y >= n \
                    or self.countBits(x) + self.countBits(y) > k \
                    or (x, y) in grid:
                continue
            grid.add((x, y))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                q.append((x + dx, y + dy))
        return len(grid)


if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(2, 3, 1))
    print(solution.movingCount(3, 1, 0))
    print(solution.movingCount(11, 8, 16))
