# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 下午4:47
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class Solution:
    def entityParser(self, text: str) -> str:
        h = [
            ('&quot;', '"'),
            ('&apos;', "'"),
            ('&gt;', '>'),
            ('&lt;', '<'),
            ('&frasl;', '/'),
            ('&amp;', '&'),
        ]
        for t in h:
            text = text.replace(t[0], t[1])
        return text


if __name__ == '__main__':
    solution = Solution()
    print(solution.entityParser("&amp; is an HTML entity but &ambassador; is not."))
    print(solution.entityParser("and I quote: &quot;...&quot;"))