# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 下午4:34
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, s in enumerate(words):
            for j in range(len(words)):
                if i != j and words[j].find(s) >= 0:
                    result.append(s)
                    break
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.stringMatching(["mass", "as", "hero", "superhero"]))
    print(solution.stringMatching(["leetcode", "et", "code"]))
    print(solution.stringMatching(["blue", "green", "bu"]))
