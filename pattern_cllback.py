# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_cllback.py
# @Time		:	2022/04/05 21:47:34

from abc import ABC,abstractmethod
import sys

class Strategy(ABC):
    @abstractmethod
    def alogrithm(self, *args, **kwargs):
        pass

class StrategyImplA(Strategy):
    def alogrithm(self, *args, **kwargs):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class StrategyImplB(Strategy):
    def alogrithm(self, *args, **kwargs):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Context:
    def interface(self, strategy:Strategy, *args, **kwargs):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} before callback...")
        strategy.alogrithm(*args, **kwargs)
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} after callback...")

if __name__ == "__main__":
    c = Context()
    c.interface(StrategyImplA())
    print("*"*50)
    c.interface(StrategyImplB())