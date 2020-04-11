# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 下午6:57
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.03.py
# @Desc    : 说明

from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        left, right, result = 0, len(arr) - 1, len(arr)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = min(result, mid)

            if arr[left] < arr[mid]:
                if arr[left] <= target <= arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[left] > arr[mid]:
                if arr[left] <= target or target <= arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[left] != target:
                    left += 1
                else:
                    right = mid - 1
        return result if result != len(arr) else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))
    print(solution.search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 11))
    print(solution.search([5, 5, 1, 2, 3, 4, 5], 5))
    print(solution.search([2, 1, 2, 2, 2, 2, 2], 1))