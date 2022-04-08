# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_decorator.py
# @Time		:	2022/04/04 00:54:28

from abc import ABC, abstractmethod
import sys


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ComponentImpl(Component):
    def operation(self):
        print(f"----{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._decorated = component

    def operation(self):
        self._decorated.operation()
        self.addBehavior()

    @abstractmethod
    def addBehavior(self):
        pass


class DecoratorImplA(Decorator):
    def addBehavior(self):
        print(f"----{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
  

class DecoratorImplB(Decorator):
    def addBehavior(self):
        print(f"----{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


if __name__ == "__main__":
    A = ComponentImpl()
    print("ComponentImpl")
    A.operation()
    D_A = DecoratorImplA(component=A)
    print("ComponentImpl DecoratorImplA")
    D_A.operation()
    D_B = DecoratorImplB(component=A)
    print("ComponentImpl DecoratorImplB")
    D_B.operation()
    D_AB = DecoratorImplB(component=D_A)
    print("ComponentImpl DecoratorImplA DecoratorImplB")
    D_AB.operation()