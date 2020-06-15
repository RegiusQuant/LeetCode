# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 下午9:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1300.py
# @Desc    : 说明

from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        left, right, dist, pos = 0, arr[-1], float('inf'), -1
        while left <= right:
            mid, temp = (left + right) // 2, 0
            for i in range(len(arr)):
                if arr[i] <= mid:
                    temp += arr[i]
                else:
                    temp += mid
            if abs(temp - target) < dist:
                dist = abs(temp - target)
                pos = mid
            elif abs(temp - target) == dist and mid < pos:
                pos = mid
            if temp > target:
                right = mid - 1
            else:
                left = mid + 1
        return pos


if __name__ == '__main__':
    solution = Solution()
    print(solution.findBestValue([4, 9, 3], 10))
    print(solution.findBestValue([2, 5, 3], 10))
    print(solution.findBestValue([60864, 25176, 27249, 21296, 20204], 56803))
