# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 下午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        return self.helper(s1, s2) or self.helper(s2, s1)

    def helper(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkIfCanBreak(s1="abc", s2="xya"))
    print(solution.checkIfCanBreak(s1="abe", s2="acd"))
    print(solution.checkIfCanBreak(s1="leetcodee", s2="interview"))
