# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 上午10:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        if s1 > s2:
            return 0

        m = len(evil)
        pi = [0] * m
        evil += '$'
        for i in range(1, m):
            j = pi[i - 1]
            while j and evil[i] != evil[j]:
                j = pi[j - 1]
            pi[i] = j + 1 if evil[i] == evil[j] else 0

        f = [[0] * 26 for _ in range(m)]
        for i in range(m):
            for j in range(26):
                k = i
                while k and ord(evil[k]) - ord('a') != j:
                    k = pi[k - 1]
                f[i][j] = k + 1 if ord(evil[k]) - ord('a') == j else 0

        s, t = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = f[s[i - 1]][ord(s1[i - 1]) - ord('a')]
            if s[i] == m:
                break
        for i in range(1, n + 1):
            t[i] = f[t[i - 1]][ord(s2[i - 1]) - ord('a')]
            if t[i] == m:
                break

        dp = [0] * m
        dp[0] = 1
        ua, ub = False, False
        for i in range(n):
            ndp = [0] * m
            for j in range(m):
                if not dp[j]:
                    continue
                for k in range(26):
                    nxt = f[j][k]
                    if nxt < m:
                        ndp[nxt] += dp[j]
            if s[i] == m:
                ua = True
            if t[i] == m:
                ub =True
            if not ua:
                for k in range(ord(s1[i]) - ord('a')):
                    nxt = f[s[i]][k]
                    if nxt < m:
                        ndp[nxt] -= 1
            if not ub:
                for k in range(ord(s2[i]) - ord('a') + 1, 26):
                    nxt = f[t[i]][k]
                    if nxt < m:
                        ndp[nxt] -= 1
            for j in range(m):
                dp[j] = (ndp[j] + int(1e9 + 7)) % int(1e9 + 7)

        result = 0
        for x in dp:
            result = (result + x) % int(1e9 + 7)
        return result


if __name__ == '__main__':
    soulution = Solution()
    print(soulution.findGoodStrings(n=2, s1="aa", s2="da", evil="b"))
    print(soulution.findGoodStrings(n=8, s1="leetcode", s2="leetgoes", evil="leet"))
    print(soulution.findGoodStrings(n=2, s1="gx", s2="gz", evil="x"))
