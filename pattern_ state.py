# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_ state.py
# @Time		:	2022/04/03 12:07:40

from abc import ABC, abstractmethod

class State(ABC):
    """状态抽象基类
    """

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def isMatch(self, stateInfo):
        """状态的属性stateInfo是否在当前的状态范围内

        Args:
            stateInfo (Any): 描述状态的信息
        """
        pass

    @abstractmethod
    def behavior(self, content):
        """定义该状态下Content的行为

        Args:
            content (Content): 与状态相关的上下文
        """
        pass

class Content(ABC):
    """状态模式上下文基类

    Args:
        ABC (abc.ABC): 申明为抽象基类
    """

    def __init__(self) -> None:
        super().__init__()
        self._states = set()
        self._curState = None
        # 状态发生变化依赖的属性,当这一变量由多个变量共同决定时可以将其单独定义成一个类
        self._stateInfo = 0

    def addState(self, state:State):
        self._states.add(state)

    def changeState(self, state:State):
        """Content状态由curState转为state

        Args:
            state (State): 状态类

        Returns:
            _type_: _description_
        """
        if state is None:
            return False
        if self._curState is None:
            print("初始化为", state.getName())
        else:
            print("由", self._curState.getName(), "变为", state.getName())
        self._curState = state

    def getState(self)->State:
        return self._curState

    def setStateInfo(self, stateInfo):
        """Content状态信息改变，状态信息不同值可能对应不同的状态

        Args:
            stateInfo (Any): 状态的描述信息
        """
        self._stateInfo = stateInfo
        for state in self._states:
            if state.isMatch(stateInfo):
                self.changeState(state)
                return

    def _getStateInfo(self):
        return self._stateInfo

    def behavior(self):
        self._curState.behavior(self)


class StateImplA(State):
    def __init__(self, name="stateA"):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo > 0

    def behavior(self, Content:Content):
        print(f"Content:{Content} state:{Content.getState().getName()} do some thing...")

class StateImplB(State):
    def __init__(self, name="stateB"):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, Content:Content):
        print(f"Content:{Content} state:{Content.getState().getName()} do some thing...")

if __name__ == "__main__":
    content = Content()
    content.addState(StateImplA())
    content.addState(StateImplB())
    content.setStateInfo(-2)
    content.behavior()
    content.setStateInfo(2)
    content.behavior()
    content.setStateInfo(-12)
    content.behavior()