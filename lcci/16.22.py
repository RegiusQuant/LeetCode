# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 上午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.22.py
# @Desc    : 说明

from typing import List


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        if K == 0:
            return ['R']

        directions = [(0, -1, 'L'), (-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D')]
        black, cd, pos = set(), 2, (0, 0)

        for i in range(K):
            if pos in black:
                cd = (cd - 1) % 4
                black.remove(pos)
            else:
                cd = (cd + 1) % 4
                black.add(pos)
            pos = (pos[0] + directions[cd][0], pos[1] + directions[cd][1])

        ax = [x for x, _ in black] + [pos[0]]
        ay = [y for _, y in black] + [pos[1]]
        minx, maxx, miny, maxy = min(ax), max(ax), min(ay), max(ay)

        matrix = [['_'] * (maxy - miny + 1) for _ in range(minx, maxx + 1)]
        for x, y in black:
            matrix[x - minx][y - miny] = 'X'
        matrix[pos[0] - minx][pos[1] - miny] = directions[cd][2]
        for i in range(len(matrix)):
            matrix[i] = ''.join((matrix[i]))
        return matrix


if __name__ == '__main__':
    solution = Solution()
    print(solution.printKMoves(0))
    print(solution.printKMoves(2))
    print(solution.printKMoves(5))
