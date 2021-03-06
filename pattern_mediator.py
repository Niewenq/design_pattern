# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_mediator.py
# @Time		:	2022/04/03 22:41:32

from abc import ABC, abstractmethod
import sys
from typing import Any

class InteractiveObject(ABC):
    def __init__(self, mediator) -> None:
        self._mediator = mediator

class InteracivaObjectImplA(InteractiveObject):
    def send(self, message:Any):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name}")
        print("----{} send message:'{}' to {}".format(self.__class__.__name__, message, self._mediator.__class__.__name__))
        self._mediator.send(message, self)
    
    def notify(self, message):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name}")
        print("----{} received mesage:'{}'".format(self.__class__.__name__, message))

class InteracivaObjectImplB(InteractiveObject):
    def send(self, message:Any):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name}")
        print("----{} send message:'{}' to {}".format(self.__class__.__name__, message, self._mediator.__class__.__name__))
        self._mediator.send(message, self)
    
    def notify(self, message):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name}")
        print("----{} received mesage:'{}'".format(self.__class__.__name__, message))

class AbstractMediator(ABC):
    @abstractmethod
    def send(self, message:Any, interactivObject: InteractiveObject):
        pass

class Mediator(AbstractMediator):
    def setInteractiveObjectImplA(self, interactiveObjectImplA):
        self.interactiveObjectImplA = interacivaObjectImplA

    def setInteractiveObjectImplB(self, interactiveObjectImplB):
        self.interactiveObjectImplB = interacivaObjectImplB

    def send(self, message: Any, interactiveObject: InteractiveObject):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name}")
        if interactiveObject ==self.interactiveObjectImplA:
            print("----{} receive message:'{}' from {} and send to {}".format(self.__class__.__name__, message, interactiveObject.__class__.__name__, self.interactiveObjectImplB.__class__.__name__))
            self.interactiveObjectImplB.notify(message)
        else:
            print("----{} receive message:'{}' from {} and send to {}".format(self.__class__.__name__, message, interactiveObject.__class__.__name__, self.interactiveObjectImplA.__class__.__name__))
            self.interactiveObjectImplA.notify(message)

if __name__ == "__main__":
    mediator = Mediator()
    # ??????????????????????????????
    interacivaObjectImplA=InteracivaObjectImplA(mediator)
    interacivaObjectImplB=InteracivaObjectImplB(mediator)
    # ????????????????????????????????????
    mediator.setInteractiveObjectImplA(interacivaObjectImplA)
    mediator.setInteractiveObjectImplB(interacivaObjectImplB)
    # ????????????A???????????????B????????????????????????
    interacivaObjectImplA.send("Have you eaten dinner?")
    interacivaObjectImplB.send("Not yet, do you want to invite me?")
