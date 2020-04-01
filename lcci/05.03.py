# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 上午10:16
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.03.py
# @Desc    : 说明

class Solution:
    def reverseBits(self, num: int) -> int:
        s, count, c = bin(num)[2:], [], 0
        for x in s:
            if x == '0':
                count.append(c)
                c = 0
            else:
                c += 1
        if c != 0:
            count.append(c)
        if len(count) == 0:
            return 1
        elif len(count) == 1:
            return count[0] + 1
        else:
            result = 0
            for i in range(1, len(count)):
                result = max(result, count[i] + count[i - 1] + 1)
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(7))

