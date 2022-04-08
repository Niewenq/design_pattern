# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	builder_pattern.py
# @Time		:	2022/03/20 23:47:17

from abc import ABC, abstractmethod


class Produt:
    def __init__(self, name, parts):
        self.name = name
        self._parts = parts

    def addPart(self, part):
        self._parts.append(part)

    def __str__(self) -> str:
        return f"产品{self.name}开始创建:\n"+"\n".join([f"add {part}" for part in self._parts])+f"\n产品{self.name}创建完成!"

class Builder(ABC):
    @abstractmethod
    def buildPartA(self):
        pass

    @abstractmethod
    def buildPartB(self):
        pass

    @abstractmethod
    def getResult(self):
        pass

class BuilderImplA(Builder):
    def __init__(self, product:Produt):
      self._product = product

    def buildPartA(self):
        self._product.addPart("part_A")

    def buildPartB(self):
        self._product.addPart("part_B")

    def getResult(self):
        return self._product


class BuilderImplB(Builder):
    def __init__(self, product:Produt):
      self._product = product

    def buildPartA(self):
        self._product.addPart("part_X")

    def buildPartB(self):
        self._product.addPart("part_Y")

    def getResult(self):
        return self._product

class Director:
    def __init__(self, builder:Builder) -> None:
        self._builder = builder

    def construct(self):
        self._builder.buildPartA()
        self._builder.buildPartB()

if __name__ == "__main__":
    b1 = BuilderImplA(Produt("A",[]))
    b2 = BuilderImplB(Produt("B",[]))
    Director(b1).construct()
    Director(b2).construct()
    print(b1.getResult())
    print()
    print(b2.getResult())