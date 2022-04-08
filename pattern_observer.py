# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   observer_pattern.py
# @Time    :   2022/02/16 00:02:39

from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    """观察者基类

    Args:
        ABC (abc.ABCMeta): 申明为抽象基类
    """
    @abstractmethod
    def update(self, subject):
        """根据主题状态更新自己接口

        Args:
            subject (Subject): 订阅的主题类
        """
        pass


class Subject(ABC):
    """主题基类

    Args:
        ABC (abc.ABCMeta): 申明为抽象基类
    """

    def __init__(self, observers: "list[Observer]" = [], state: Any=None) -> None:
        """主题基类初始化函数

        Args:
            observers (list[Observer], optional): 订阅该主题观察者列表. Defaults to [].
            state (Any, optional): 主题初始化状态. Defaults to None.
        """
        self._observers = observers
        self._state = state

    def addObserver(self, observer: Observer):
        """为主题添加观察者

        Args:
            observer (Observer): 待添加的观察者
        """
        self._observers.append(observer)

    def removeObserver(self, observer: Observer):
        """为主题移除观察者

        Args:
            observer (Observer): 待移除的观察者
        """
        self._observers.remove(observer)

    def getState(self):
        """获取subject状态

        Returns:
            Any: Subject此时的状态
        """
        return self._state

    def notify(self):
        """通知订阅该主题的观察者
        """
        for o in self._observers:
            o.update(self)

    def change(self, state):
        """subject状态改变

        Args:
            state (Any): subject状态
        """
        self._state = state


class ObserverImplA(Observer):
    """观察者实现类A

    Args:
        Observer (Class): 观察者基类
    """
    def update(self, subject:  Subject):
        """根据subject传来的state，给出不同的操作

        Args:
            subject (Subject): 订阅的主题
        """
        if subject.getState() == "A":
            print(f"{self.__class__.__name__} is updating...")


class ObserverImplB(Observer):
    """观察者实现类B

    Args:
        Observer (Class): 观察者基类
    """
    def update(self, subject: Subject):
        """根据subject传来的state，给出不同的操作

        Args:
            subject (Subject): 订阅的主题
        """
        if subject.getState() == "B":  # 根据state状态，做出相应的动作
            print(f"{self.__class__.__name__} is updating...")

class SubjectImpl(Subject):
    """主题具体实现类

    Args:
        Subject (Class): 主题抽象基类
    """
    def change(self, state):
        """改变主题状态

        Args:
            state (Any): 待转换的状态
        """
        super().change(state)


if __name__ == "__main__":
    observerA = ObserverImplA()
    observerB = ObserverImplB()
    subject = SubjectImpl(observers=[observerA, observerB])

    subject.change(state="A")
    subject.notify()
    print("*" * 35)
    subject.change(state="B")
    subject.notify()
