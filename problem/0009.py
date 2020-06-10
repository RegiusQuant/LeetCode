# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 上午10:39
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0009.py
# @Desc    : 说明

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        temp = []
        while x > 0:
            temp.append(x % 10)
            x //= 10
        for i in range(len(temp) // 2 + 1):
            if temp[i] != temp[len(temp) - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))