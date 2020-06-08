# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1115.py
# @Desc    : 说明

from threading import Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = Semaphore(1)
        self.s2 = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.s2.acquire()
            printBar()
            self.s1.release()
