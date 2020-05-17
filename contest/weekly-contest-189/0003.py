# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 下午12:36
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies = []
        for i in range(len(favoriteCompanies)):
            companies.append(set(favoriteCompanies[i]))

        result = []
        for i in range(len(companies)):
            for j in range(len(companies)):
                if i != j and len(companies[i] & companies[j]) == len(companies[i]):
                    break
            else:
                result.append(i)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.peopleIndexes(
        [["leetcode", "google", "facebook"],
         ["google", "microsoft"],
         ["google", "facebook"],
         ["google"],
         ["amazon"]]
    ))
    print(solution.peopleIndexes(
        [["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]]
    ))
    print(solution.peopleIndexes(
        [["leetcode"], ["google"], ["facebook"], ["amazon"]]
    ))
