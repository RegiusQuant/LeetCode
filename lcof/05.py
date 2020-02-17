# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午6:37
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.py
# @Desc    : 说明

class Solution:
    def replaceSpace(self, s: str) -> str:
        tmp = []
        for x in s:
            if x == ' ':
                tmp.append('%20')
            else:
                tmp.append(x)
        return ''.join(tmp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.replaceSpace("We are happy."))
