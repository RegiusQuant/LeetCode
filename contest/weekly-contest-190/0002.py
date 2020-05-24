# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 上午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result, alphas = 0, ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in alphas:
                result += 1

        temp, left, right = result, 0, k
        while right < len(s):
            if s[left] in alphas:
                temp -= 1
            if s[right] in alphas:
                temp += 1
            left, right = left + 1, right + 1
            result = max(result, temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxVowels('abciiidef', 3))
    print(solution.maxVowels('aeiou', 2))
    print(solution.maxVowels('leetcode', 3))
    print(solution.maxVowels('rhythms', 4))
    print(solution.maxVowels('tryhard', 4))
