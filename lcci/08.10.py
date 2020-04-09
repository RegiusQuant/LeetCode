# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 上午10:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.10.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visit = set()
        queue = deque()
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        queue.append((sr, sc))
        visit.add((sr, sc))

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == oldColor and (nx, ny) not in visit:
                    image[nx][ny] = newColor
                    visit.add((nx, ny))
                    queue.append((nx, ny))
        return image


if __name__ == '__main__':
    solution = Solution()
    print(solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
