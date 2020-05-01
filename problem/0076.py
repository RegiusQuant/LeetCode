# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 下午7:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0076.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''

        counter = Counter(t)
        record = []
        for i, c in enumerate(s):
            if c in counter:
                record.append((i, c))

        result = (float('inf'), None, None)
        left, right, nums = 0, 0, 0
        windows = Counter()
        while right < len(record):
            c = record[right][1]
            windows[c] += 1
            if windows[c] == counter[c]:
                nums += 1

            while left <= right and nums == len(counter):
                start, end = record[left][0], record[right][0]
                if end - start + 1 < result[0]:
                    result = (end - start + 1, start, end)

                c = record[left][1]
                windows[c] -= 1
                if windows[c] < counter[c]:
                    nums -= 1
                left += 1

            right += 1
        return '' if result[0] == float('inf') else s[result[1]: result[2] + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow('ADOBECODEBANC', 'ABC'))
