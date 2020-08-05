# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 下午11:34
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0632.py
# @Desc    : 说明

from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        hashMap = defaultdict(list)
        minVal, maxVal = float('inf'), float('-inf')
        for i, arr in enumerate(nums):
            for x in arr:
                hashMap[x].append(i)
            minVal, maxVal = min(minVal, *arr), max(maxVal, *arr)

        freq, count = [0] * n, 0
        left, right = minVal, minVal - 1
        result = [minVal, maxVal]

        while right < maxVal:
            right += 1
            if right in hashMap:
                for i in hashMap[right]:
                    freq[i] += 1
                    if freq[i] == 1:
                        count += 1
                while count == n:
                    if right - left < result[1] - result[0]:
                        result = [left, right]
                    if left in hashMap:
                        for i in hashMap[left]:
                            freq[i] -= 1
                            if freq[i] == 0:
                                count -= 1
                    left += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
