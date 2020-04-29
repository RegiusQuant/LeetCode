# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 上午10:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1095.py
# @Desc    : 说明

class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index):
        return self.array[index]

    def length(self):
        return len(self.array)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left
        index = self.search(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = self.search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        return index

    def search(self, mountain, target, left, right, key=lambda x: x):
        target = key(target)
        while left <= right:
            mid = (left + right) // 2
            cur = key(mountain.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    # mountain = MountainArray([1, 2, 3, 4, 5, 3, 1])
    # solution = Solution()
    # print(solution.findInMountainArray(3, mountain))
    #
    mountain = MountainArray([1, 5, 2])
    solution = Solution()
    print(solution.findInMountainArray(0, mountain))
