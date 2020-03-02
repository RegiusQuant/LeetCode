# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 上午10:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 49.py
# @Desc    : 说明

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, ptr = [1] * n, {2: 0, 3: 0, 5: 0}
        for i in range(1, n):
            dp[i] = float('inf')
            for k, p in ptr.items():
                dp[i] = min(dp[i], dp[p] * k)
            for k, p in ptr.items():
                if dp[i] == dp[p] * k:
                    ptr[k] += 1
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(10))
