# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	memento_pattern.py
# @Time		:	2022/03/24 00:08:26


class Memento:
    def __init__(self, state) -> None:
        self._state = state

    def setState(self, state):
        self._state = state

    def getState(self):
        return self._state

class Originator:
    def __init__(self, state=None) -> None:
        self.state = state

    def createMemento(self):
        return Memento(self.state)

    def restoreFromMemento(self, memento:Memento):
        self.state = memento.getState()

    def __str__(self) -> str:
        return f"state: {self.state}"

class Caretaker:
    def __init__(self) -> None:
        self._memento = None
    
    def getMemento(self):
        return self._memento

    def setMemento(self, memento:Memento):
        self._memento = memento

if __name__ == "__main__":
    # originator状态为“on”
    originator = Originator()
    originator.state = "on"
    print(originator)

    # 备忘记录状态
    caretaker = Caretaker()
    caretaker.setMemento(originator.createMemento())

    # originator更新状态为“off”
    originator.state = "off"
    print(originator)

    # originator恢复“off”状态
    originator.restoreFromMemento(caretaker.getMemento())
    print(originator)
    
    

        