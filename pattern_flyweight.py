# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	flyweight_pattern.py
# @Time		:	2022/03/24 22:16:32

from abc import ABC, abstractmethod

class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    def __init__(self,intrinsicState) -> None:
        self._intrinsicState = intrinsicState

    def operation(self, extrinsicState):
        print(f"{self.__class__.__name__}\tintrinsicState:{self._intrinsicState}\textrinsicState:{extrinsicState}")

class FlyweightFactory:
    def __init__(self) -> None:
        self._flyweights  = {}

    def getFlyweight(self,key):
        flyweight = self._flyweights.get(key,None)
        if flyweight is None:
            flyweight = FlyweightImpl(key)
        return flyweight

class UnsharedFlyweightImpl(Flyweight):
    def operation(self, extrinsicState):
        print(f"{self.__class__.__name__}\textrinsicState:{extrinsicState}")

if __name__ == "__main__":
    flyweightFactory = FlyweightFactory()

    flyweightA=flyweightFactory.getFlyweight("intrinsicStateA")
    flyweightA.operation("extrinsicStateA")

    flyweightB=flyweightFactory.getFlyweight("intrinsicStateB")
    flyweightB.operation("extrinsicStateB")

    flyweightC=UnsharedFlyweightImpl()
    flyweightC.operation("extrinsicStateC")