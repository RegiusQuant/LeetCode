# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 下午1:11
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from collections import defaultdict, Counter
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counter = defaultdict(Counter)
        tableSet, foodSet = set(), set()

        for i in range(len(orders)):
            table, food = orders[i][1], orders[i][2]
            tableSet.add(table)
            foodSet.add(food)
            counter[table][food] += 1

        result = []
        foodList = sorted(list(foodSet))
        result.append(['Table'] + foodList)

        tableList = sorted(list(tableSet), key=lambda x: int(x))
        for i in range(len(tableList)):
            temp = [tableList[i]]
            for j in range(len(foodList)):
                temp.append(str(counter[tableList[i]][foodList[j]]))
            result.append(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.displayTable(
        [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
         ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
    ))
