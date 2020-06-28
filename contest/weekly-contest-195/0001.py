# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 下午7:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = {(0, 0)}
        cx, cy = 0, 0
        for c in path:
            if c == 'N':
                cx += 1
            elif c == 'S':
                cx -= 1
            elif c == 'W':
                cy += 1
            else:
                cy -= 1
            if (cx, cy) in s:
                return True
            s.add((cx, cy))
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPathCrossing('NES'))
    print(solution.isPathCrossing('NESWW'))
