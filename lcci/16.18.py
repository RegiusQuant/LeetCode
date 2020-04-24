# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.18.py
# @Desc    : 说明

class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return not value
        n = len(value)
        ca, cb = pattern.count('a'), pattern.count('b')
        ma = 0 if ca == 0 else n // ca
        for la in range(ma + 1):
            lb = 0
            if cb == 0:
                if la * ca != n:
                    continue
            else:
                if (n - la * ca) % cb != 0:
                    continue
                lb = (n - la * ca) // cb
            s, p, l = {'a': None, 'b': None}, 0, {'a': la, 'b': lb}
            for x in pattern:
                if s[x] and s[x] != value[p:p + l[x]]:
                    break
                s[x] = value[p:p + l[x]]
                p += l[x]
            else:
                if s['a'] != s['b']:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.patternMatching('abba', 'dogcatcatdog'))
    print(solution.patternMatching('abba', 'dogcatcatfish'))
    print(solution.patternMatching('aaaa', 'dogcatcatdog'))
    print(solution.patternMatching('abba', 'dogdogdogdog'))
    print(solution.patternMatching('a', ''))
    print(solution.patternMatching('bbb', 'xxxxxx'))