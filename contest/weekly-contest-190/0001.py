# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 上午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, s in enumerate(sentence.split()):
            if s.startswith(searchWord):
                return i + 1
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPrefixOfWord("i love eating burger", "burg"))
    print(solution.isPrefixOfWord("this problem is an easy problem", "pro"))
    print(solution.isPrefixOfWord("i am tired", "you"))
    print(solution.isPrefixOfWord("i use triple pillow", "pill"))
    print(solution.isPrefixOfWord("hello from the other side", "they"))
