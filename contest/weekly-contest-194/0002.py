# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        s, result = {}, []
        for name in names:
            if name not in s:
                result.append(name)
                s[name] = 0
            else:
                for i in range(s[name] + 1, len(names)):
                    temp = name + '({})'.format(i)
                    if temp not in s:
                        result.append(temp)
                        s[temp] = 0
                        break
                    else:
                        s[name] = i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getFolderNames(["pes", "fifa", "gta", "pes(2019)"]))
    print(solution.getFolderNames(["gta", "gta(1)", "gta", "avalon"]))
    print(solution.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
    print(solution.getFolderNames(["wano", "wano", "wano", "wano"]))
    print(solution.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]))
