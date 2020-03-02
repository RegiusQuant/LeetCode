# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 上午10:48
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 51.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.result

    def mergeSort(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            self.mergeSort(nums, start, mid)
            self.mergeSort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        p1, p2, temp = start, mid + 1, []
        while p1 <= mid and p2 <= end:
            if nums[p1] <= nums[p2]:
                temp.append(nums[p1])
                p1 += 1
            else:
                self.result += mid - p1 + 1
                temp.append(nums[p2])
                p2 += 1
        while p1 <= mid:
            temp.append(nums[p1])
            p1 += 1
        while p2 <= end:
            temp.append(nums[p2])
            p2 += 1
        nums[start:end + 1] = temp


if __name__ == '__main__':
    solution = Solution()
    print(solution.reversePairs([7, 5, 6, 4]))
