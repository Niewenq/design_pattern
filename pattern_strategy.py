# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	strategy_pattern.py
# @Time		:	2022/03/22 07:53:11

from abc import ABC,abstractmethod
import sys

class Strategy(ABC):
    @abstractmethod
    def algorithmInterface(self):
        pass
    
class StrategyImplA(Strategy):
    def algorithmInterface(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        
class StrategyImplB(Strategy):
    def algorithmInterface(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        
class StrategyImplC(Strategy):
    def algorithmInterface(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        
class Context:
    def __init__(self,strategy:Strategy): # 初始化时，传入具体的策略对象
        self.strategy=strategy
    def contextInterface(self): # 根据具体的策略对象，调用其算法的方法
        self.strategy.algorithmInterface()
    
if __name__ == "__main__":
    context=Context(StrategyImplA())
    context.contextInterface()
    
    context=Context(StrategyImplB())
    context.contextInterface()
    
    context=Context(StrategyImplC())
    context.contextInterface()