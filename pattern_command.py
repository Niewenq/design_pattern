# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	command_pattern.py
# @Time		:	2022/03/23 22:36:58

from abc import ABC,abstractmethod
import sys

class Receiver:
    def action(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Command(ABC):
    def __init__(self, receiver:Receiver) -> None:
         self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass

class CommandImpl(Command):
    def execute(self):
        self._receiver.action()

class Invoker:
    def __init__(self) -> None:
        self._command = None
    def setCommand(self, command:Command):
        self._command = command
    def action(self):
        if self._command is not None:
            self._command.execute()

if __name__ == "__main__":
    receiver = Receiver()
    command = CommandImpl(receiver)
    invoker = Invoker()

    invoker.setCommand(command)
    invoker.action()