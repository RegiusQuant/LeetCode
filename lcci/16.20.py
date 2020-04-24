# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 上午11:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.20.py
# @Desc    : 说明


from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        map = {
            'a': 2, 'b': 2, 'c': 2,
            'd': 3, 'e': 3, 'f': 3,
            'g': 4, 'h': 4, 'i': 4,
            'j': 5, 'k': 5, 'l': 5,
            'm': 6, 'n': 6, 'o': 6,
            'p': 7, 'q': 7, 'r': 7, 's': 7,
            't': 8, 'u': 8, 'v': 8,
            'w': 9, 'x': 9, 'y': 9, 'z': 9
        }
        result = []
        for word in words:
            for i, c in enumerate(word):
                if str(map[c]) != num[i]:
                    break
            else:
                result.append(word)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getValidT9Words('8733', ["tree", "used"]))
    print(solution.getValidT9Words('2', ['a', 'b', 'c', 'd']))
