# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	template_method_pattern.py
# @Time		:	2022/03/26 00:04:30

from abc import ABC,abstractmethod
import sys

class Template(ABC):
    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    def templateMethod(self):
        self.stepOne()
        self.stepTwo()

class TemplateImplA(Template):
    def stepOne(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

    def stepTwo(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class TemplateImplB(Template):
    def stepOne(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

    def stepTwo(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

if __name__ == "__main__":
    a = TemplateImplA()
    a.templateMethod()
    print()
    b = TemplateImplB()
    b.templateMethod()
        