# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   composite_pattern.py
# @Time    :   2022/02/20 17:51:02

from abc import ABC, abstractmethod


class Component(ABC):
    @staticmethod
    def addComponent():
        pass

    @staticmethod
    def removeComponent():
        pass

    @abstractmethod
    def show():
        pass


class Composite(Component):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._components = []

    def addComponent(self, component: Component):
        self._components.append(component)

    def removeComponent(self, component: Component):
        self._components.remove(component)

    def show(self, depth):
        print(f"{'-'*4*depth}{self.name}")
        for component in self._components:
            component.show(depth + 1)


class Leaf(Component):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def addComponent(self):
        pass

    def removeComponent(self):
        pass

    def show(self, depth):
        print(f"{'-'*4*depth}{self.name}")


if __name__ == "__main__":
    root = Composite("root")
    root.addComponent(Leaf("Leaf A"))
    comp = Composite("Composite X")
    comp.addComponent(Leaf("Leaf XA"))
    comp.addComponent(Leaf("Leaf XB"))
    comp2 = Composite("Composite XY")
    comp2.addComponent(Leaf("Leaf XYA"))
    comp2.addComponent(Leaf("Leaf XYB"))
    comp.addComponent(comp2)
    root.addComponent(comp)
    root.addComponent(Leaf("Leaf B"))
    leaf = Leaf("Leaf C")
    root.addComponent(leaf)
    root.removeComponent(leaf)
    root.show(0)
