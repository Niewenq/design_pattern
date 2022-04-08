# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	interpreter_pattern.py
# @Time		:	2022/03/31 22:50:34

from abc import ABC, abstractmethod
import sys

class Context:
    pass


class AbstractExpession(ABC):
    @abstractmethod
    def interpret(self, context: Context):
        pass

class TerminalExpression(AbstractExpession):
    def interpret(self, context: Context):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class NonterminalExpression(AbstractExpession):
    def interpret(self, context: Context):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

if __name__ == "__main__":
    context = Context()
    for exp in (TerminalExpression(),NonterminalExpression(),TerminalExpression()):
        exp.interpret(context)
