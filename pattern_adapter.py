# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	adapter_pattern.py
# @Time		:	2022/03/21 22:09:29

from abc import ABC, abstractmethod
import sys

class Target(ABC):
    @abstractmethod
    def request(self):
        pass

class Adaptee():
    def specificRequest(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Adaptor(Target):
    def __init__(self):
      self._adaptee = Adaptee()
    def request(self):
        self._adaptee.specificRequest()

if __name__ == "__main__":
    target = Adaptor()
    # 对客户端来说，调用的就是Target rewuest函数
    target.request()

