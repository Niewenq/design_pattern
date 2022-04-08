# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_filter.py
# @Time		:	2022/04/05 15:04:46

from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def doFilter(self, elements):
        pass

class FilterChain(Filter):
    def __init__(self, filters:"list[Filter]"= []) -> None:
        self._filters = filters

    def addFilter(self, filter:Filter):
        self._filters.append(filter)

    def removeFilter(self, filter:Filter):
        self._filters.remove(filter)

    def doFilter(self, elements):
        for filter in self._filters:
            elements = filter.doFilter(elements)
        return elements

class FilterImplA(Filter):
    def doFilter(self, elements):
        return filter(lambda x: x > 0, elements)

class FilterImplB(Filter):
    def doFilter(self, elements):
        return filter(lambda x: x < 10, elements)

if __name__ == "__main__":
    elements = [-10,2,3,10,12,0,-12,-1]
    fc = FilterChain([FilterImplA(), FilterImplB()])
    print(list(fc.doFilter(elements)))