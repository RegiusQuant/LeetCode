# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 下午10:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.s1 = []
        self.s2 = []

    def visit(self, url: str) -> None:
        self.s1.append(self.curr)
        self.s2 = []
        self.curr = url

    def back(self, steps: int) -> str:
        while steps > 0 and self.s1:
            self.s2.append(self.curr)
            self.curr = self.s1.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps > 0 and self.s2:
            self.s1.append(self.curr)
            self.curr = self.s2.pop()
            steps -= 1
        return self.curr


if __name__ == '__main__':
    obj = BrowserHistory('leetcode.com')
    obj.visit('google.com')
    obj.visit('facebook.com')
    obj.visit('youtube.com')
    print(obj.back(1))
    print(obj.back(1))
    print(obj.forward(1))
    obj.visit('linkedin.com')
    print(obj.forward(2))
    print(obj.back(2))
    print(obj.back(7))
