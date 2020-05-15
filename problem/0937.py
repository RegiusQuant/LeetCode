# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 上午11:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0937.py
# @Desc    : 说明

class Solution(object):
    def reorderLogFiles(self, logs):
        def comp(log):
            idx, rest = log.split(' ', 1)
            return (0, rest, idx) if rest[0].isalpha() else (1,)

        return sorted(logs, key=comp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
