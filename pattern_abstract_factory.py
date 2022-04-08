# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	abstract_factory_pattern.py
# @Time		:	2022/03/23 08:01:43

from abc import ABC, abstractmethod
import sys

class ProductA(ABC):
    @abstractmethod
    def feature(self):
        pass

class ProductAImplA(ProductA):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductAImplB(ProductA):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


class ProductB(ABC):
    @abstractmethod
    def feature(self):
        pass

class ProductBImplA(ProductB):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductBImplB(ProductB):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class AbstractFactory(ABC):
    @abstractmethod
    def createProductA(self):
        pass

    @abstractmethod
    def createProductB(self):
        pass

class FactoryImplA(AbstractFactory):
    def createProductA(self)->ProductA:
        return ProductAImplA()

    def createProductB(self)->ProductB:
        return ProductAImplB()

class FactoryImplB(AbstractFactory):
    def createProductA(self)->ProductA:
        return ProductBImplA()

    def createProductB(self)->ProductB:
        return ProductBImplB()

if __name__ == "__main__":
    # 采用反射的机制，避免了需要换工厂时需要全部修改使用的工厂类，在反射机制中，只需要修改classPath变量即可
    from importlib import import_module
    classPath = "abstract_factory_pattern.FactoryImplA"
    index = classPath.rfind(".")
    modulePath,className = classPath[:index],classPath[index+1:]
    factory:FactoryImplA = getattr(import_module("abstract_factory_pattern"),className)()
    pa = factory.createProductA()
    pb = factory.createProductB()
    pa.feature()
    pb.feature()

