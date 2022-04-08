# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	proxy_pattern.py
# @Time		:	2022/03/20 23:46:55


from abc import ABC, abstractmethod


class Subject(ABC):
    """主题抽象类，将要被代理的类"""

    @abstractmethod
    def request(self, content=None):
        """任务请求方法"""
        pass


class RealSubject(Subject):
    """真实主题类，具体任务类"""

    def request(self, content):
        print(f"{self.__class__.__name__}'s assignment --> {content}")


class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, subject: RealSubject):
        """传入被代理的对象"""
        self._realSubject = subject

    def preRequest(self):
        print(f"{self.__class__.__name__}'s prework")

    def afterRequest(self):
        print(f"{self.__class__.__name__}'s afterwork")

    def request(self, content=None) -> None:
        self.preRequest()
        if self._realSubject is not None:
            self._realSubject.request(content)
        self.afterRequest()


if __name__ == "__main__":
    realObj = RealSubject()
    proxyObj = ProxySubject(realObj)
    proxyObj.request("do homework")
