# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   iterator_pattern.py
# @Time    :   2022/02/20 16:25:07

from abc import ABC, abstractmethod


class Aggregate(ABC):
    @abstractmethod
    def createIterator(self):
        pass

    @abstractmethod
    def getitem(self, key):
        pass


class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

class AggregateImpl(Aggregate):
    def __init__(self, aggregate: list) -> None:
        super().__init__()
        self._aggregate = aggregate

    def createIterator(self) -> Iterator:
        return AggregateImplIterator(self)

    def getitem(self, key):
        return self._aggregate[key]


class AggregateImplIterator(Iterator):
    def __init__(self, aggregate: Aggregate) -> None:
        self.aggregate = aggregate
        self.__index = 0

    def next(self):
        try:
            ele = self.aggregate.getitem(self.__index)
            self.__index += 1
        except IndexError:
            raise StopIteration()
        return ele


if __name__ == "__main__":
    ai = AggregateImpl([1, 2, 3, 4])
    ai_iter = ai.createIterator()
    print(ai_iter.next())
    print(ai_iter.next())
    print(ai_iter.next())
    print(ai_iter.next())
    print(ai_iter.next())
