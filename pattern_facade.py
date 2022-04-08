# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   facade_pattern.py
# @Time    :   2022/02/16 07:51:19

import sys


class SubSystemA():
    def function(self):
        """子系统类A的功能函数，实现子系统A的功能，处理Facade对象指派的任务"""
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


class SubSystemB():
    def function(self):
        """子系统类B的功能函数，实现子系统B的功能，处理Facade对象指派的任务"""
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


class Facade():
    def __init__(self) -> None:
        self._subSystemA = SubSystemA()
        self._subSystemB = SubSystemB()

    def functionA(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        self._subSystemA.function()

    def functionB(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        self._subSystemB.function()


if __name__ == "__main__":
    facade = Facade()
    facade.functionA()
    print("-" * 50)
    facade.functionB()
