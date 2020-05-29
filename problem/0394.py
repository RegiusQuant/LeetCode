# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 下午8:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0394.py
# @Desc    : 说明

class Solution:
    def decodeString(self, s: str) -> str:
        def helper(p):
            result, num = '', 0
            while p < len(s):
                if s[p].isdigit():
                    num = num * 10 + int(s[p])
                elif s[p] == '[':
                    p, temp = helper(p + 1)
                    result += num * temp
                    num = 0
                elif s[p] == ']':
                    return p, result
                else:
                    result += s[p]
                p += 1
            return result

        return helper(0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString('3[a]2[bc]'))
    print(solution.decodeString('3[a2[c]]'))
    print(solution.decodeString('2[abc]3[cd]ef'))
