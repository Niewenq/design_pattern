# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_singleton.py
# @Time		:	2022/04/04 16:36:27

class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


def singleton(cls):
    "构造一个单例的装饰器"
    instance = {}
    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton

if __name__ == "__main__":
    s1 = Singleton.getInstance()
    s2 = Singleton.getInstance()
    print(s1,s2,s1==s2)