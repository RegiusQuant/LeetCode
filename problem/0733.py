# -*- coding: utf-8 -*-
# @Time       : 2020/08/16 15:50:35
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0733.py
# @Description: 文件说明

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        def helper(cx, cy):
            image[cx][cy] = newColor
            for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == oldColor:
                    helper(nx, ny)

        helper(sr, sc)
        return image


if __name__ == "__main__":
    solution = Solution()
    print(solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
