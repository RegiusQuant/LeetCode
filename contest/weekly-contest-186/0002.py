# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 下午2:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = [0] * len(cardPoints)
        leftSum[0] = cardPoints[0]
        for i in range(1, len(cardPoints)):
            leftSum[i] = leftSum[i - 1] + cardPoints[i]
        leftSum = [0] + leftSum

        rightSum = [0] * len(cardPoints)
        rightSum[0] = cardPoints[-1]
        for i in range(1, len(cardPoints)):
            rightSum[i] = rightSum[i - 1] + cardPoints[-i - 1]
        rightSum = [0] + rightSum

        result = 0
        for i in range(k + 1):
            result = max(result, leftSum[i] + rightSum[k - i])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore([2, 2, 2], 2))
    print(solution.maxScore([9, 7, 7, 9, 7, 7, 9], 7))
    print(solution.maxScore([1, 1000, 1], 1))
    print(solution.maxScore([1, 79, 80, 1, 1, 1, 200, 1], 3))
