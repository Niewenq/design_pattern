# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	factory_pattern.py
# @Time		:	2022/03/22 23:41:08

from abc import ABC, abstractmethod
import sys

class Product(ABC):
    @abstractmethod
    def feature(self):
        pass

class ProductImplA(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductImplB(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Factory(ABC):
    @abstractmethod
    def createProduct(self):
        pass

class ProductAFactory(Factory):
    def createProduct(self)->ProductImplA:
        return ProductImplA()

class ProductBFactory(Factory):
    def createProduct(self)->ProductImplB:
        return ProductImplB()

if __name__ == "__main__":
    ProductAFactory().createProduct().feature()
    ProductBFactory().createProduct().feature()

