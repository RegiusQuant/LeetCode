# -*- coding: utf-8 -*-
# @Time       : 2020/08/25 22:40:57
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0491.py
# @Description: 文件说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, last, temp):
            if cur == len(nums):
                if len(temp) >= 2:
                    self.result.append(temp)
                return

            if nums[cur] >= last:
                dfs(cur + 1, nums[cur], temp + [nums[cur]])
            if nums[cur] != last:
                dfs(cur + 1, last, temp)

        dfs(0, float('-inf'), [])
        return self.result


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubsequences([4, 6, 7, 7]))