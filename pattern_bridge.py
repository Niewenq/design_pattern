# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	bridge_pattern.py
# @Time		:	2022/03/31 07:54:01

from abc import ABC, abstractmethod
import sys

class Implementor(ABC):
    @abstractmethod
    def operationImpl(self):
        pass

class ImplementorImplA(Implementor):
    def operationImpl(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ImplementorImplB(Implementor):
    def operationImpl(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Abstraction(ABC):
    def __init__(self) -> None:
        self.implementor = None

    def setImplementor(self, implementor:Implementor):
        self.implementor = implementor

    @abstractmethod
    def operation(self):
        pass

class RefinedAbstraction(Abstraction):
    def operation(self):
        self.implementor.operationImpl()

if __name__ == "__main__":
    ra = RefinedAbstraction()
    ra.setImplementor(ImplementorImplA())
    ra.operation()
    ra.setImplementor(ImplementorImplB())
    ra.operation()
        