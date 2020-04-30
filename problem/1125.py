# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午3:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1125.py
# @Desc    : 说明

from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillToState = {s: 1 << i for i, s in enumerate(req_skills)}
        peopleToState = []
        for i in range(len(people)):
            temp = 0
            for s in people[i]:
                temp += skillToState[s]
            peopleToState.append(temp)

        dp = [-1] * (1 << len(req_skills))
        path = [-1] * (1 << len(req_skills))
        team = [-1] * (1 << len(req_skills))
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(len(peopleToState)):
                if dp[i] >= 0:
                    tempState = i | peopleToState[j]
                    if dp[tempState] == -1 or dp[tempState] > dp[i] + 1:
                        dp[tempState] = dp[i] + 1
                        path[tempState] = i
                        team[tempState] = j

        result = []
        state = -1
        while state != 0:
            result.append(team[state])
            state = path[state]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestSufficientTeam(
        ["java", "nodejs", "reactjs"],
        [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    ))
    print(solution.smallestSufficientTeam(
        ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
        [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"],
         ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]
    ))
