# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 上午10:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List
from collections import defaultdict
from functools import cmp_to_key


class Solution:

    def rankTeams(self, votes: List[str]) -> str:
        numVotes, numRanks, teamSet = len(votes), len(votes[0]), set(votes[0])
        voteDict = defaultdict(list)
        for c in teamSet:
            voteDict[c] = [0] * numRanks
        for v in votes:
            for i, c in enumerate(v):
                voteDict[c][i] += 1
        result = list(voteDict.keys())

        def compare(x, y):
            for i in range(numRanks):
                if voteDict[x][i] != voteDict[y][i]:
                    return voteDict[y][i] - voteDict[x][i]
            return ord(x) - ord(y)

        result = sorted(result, key=cmp_to_key(compare))
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
    print(solution.rankTeams(["WXYZ", "XYZW"]))
    print(solution.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    print(solution.rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))
    print(solution.rankTeams(["M", "M", "M", "M"]))
