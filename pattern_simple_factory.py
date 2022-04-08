# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	simple_factory_pattern.py
# @Time		:	2022/03/22 22:14:56

from abc import ABC, abstractmethod
import sys

class Product(ABC):
    @abstractmethod
    def feature(self):
        pass

class SimpleFactory:
    @staticmethod
    def createProduct(name:str)->Product:
        if name == "A":
            product = ProductImplA()
        elif name == "B":
            product = ProductImplB()
        else:
            raise ValueError(f"parameter name: {name} is not supported.")
        return product

class ProductImplA(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductImplB(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

if __name__ == "__main__":
    SimpleFactory.createProduct("A").feature()
    SimpleFactory.createProduct("B").feature()
    SimpleFactory.createProduct("C").feature()

