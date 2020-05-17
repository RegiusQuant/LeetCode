# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 下午12:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def arrangeWords(self, text: str) -> str:
        temp = text.lower().split()
        temp.sort(key=lambda x: len(x))
        temp[0] = temp[0].capitalize()
        return ' '.join(temp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrangeWords("Leetcode is cool"))
    print(solution.arrangeWords("Keep calm and code on"))
