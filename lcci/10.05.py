# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 上午10:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.05.py
# @Desc    : 说明

from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        if not words or not s:
            return -1
        left, right = 0, len(words) - 1
        while left <= right:
            while left <= right and not words[left]:
                left += 1
            while left <= right and not words[right]:
                right -= 1
            mid = (left + right) // 2
            while mid < right and not words[mid]:
                mid += 1
            if words[mid] == s:
                return mid
            if words[mid] < s:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findString(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], 'ta'))
    print(solution.findString(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], 'ball'))
