# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	visitor_pattern.py
# @Time		:	2022/03/24 23:51:40

from abc import ABC,abstractmethod

class Visitor:
    @abstractmethod
    def visitElementImplA(self,element):
        pass

    @abstractmethod
    def visitElementImplB(self,element):
        pass

class VisitorImplA(Visitor):
    def visitElementImplA(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

    def visitElementImplB(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

class VisitorImplB(Visitor):
    def visitElementImplA(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

    def visitElementImplB(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

class Element(ABC):
    @abstractmethod
    def accept(self, visitor:Visitor):
        pass

class ElementImplA(Element):
    def accept(self, visitor: Visitor):
        visitor.visitElementImplA(self)

class ElementImplB(Element):
    def accept(self, visitor: Visitor):
        visitor.visitElementImplB(self)

class ObjectStructure:
    def __init__(self, elements=[]) -> None:
        self._elements = elements

    def addElement(self,element:Element):
        self._elements.append(element)

    def removeElement(self, element:Element):
        self._elements.remove(element)

    def accept(self, visitor: Visitor):
        for element in self._elements:
            element.accept(visitor)


if __name__ == "__main__":
    objectStructure = ObjectStructure([])

    objectStructure.addElement(ElementImplA())
    objectStructure.addElement(ElementImplB())

    visitorA = VisitorImplA()
    visitorB = VisitorImplB()

    objectStructure.accept(visitorA)
    objectStructure.accept(visitorB)


