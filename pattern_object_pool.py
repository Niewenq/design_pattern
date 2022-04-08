# -*- encoding: utf-8 -*-
# @Author	:   Wenqing Nie
# @File		:	pattern_object_pool.py
# @Time		:	2022/04/05 16:12:30

from abc import ABC,abstractmethod
from time import strftime, localtime, time

class PooledObject:
    """池对象，也称池化对象,对象池中的对象
    """

    def __init__(self, obj=None) -> None:
        self.__obj = obj
        self.__busy = False

    def getObject(self):
        return self.__obj

    def setObject(self, obj):
        self.__obj = obj

    def isBusy(self):
        return self.__busy

    def setBusy(self, busy):
        self.__busy = busy

class ObjectPool(ABC):
    """对象池

    Args:
        ABC (metaClass): 抽象类
    """
    initialNumberOfObject = 2 # 对象池初始化大小
    maxNUmberOfObject = 3 # 对象池最大的大小

    def __init__(self) -> None:
        self.__pool:list[PooledObject] = []
        for _ in range(ObjectPool.initialNumberOfObject):
            self.__pool.append(self.createPooledObject())
    
    @abstractmethod
    def createPooledObject(self):
        pass

    def borrowObject(self):
        pooledObject:PooledObject = self._findFreePooledObject()
        if pooledObject is not None:
            pooledObject.setBusy(True)
            print("{}对象已被借用，time：{}".format(id(pooledObject.getObject()), strftime("%Y-%m-%d %H:%M:%s", localtime(time()))))
        else:
            pooledObject = self.addObject()
            if pooledObject is None:
                print("对象池中没有空余对象，借出失败！！！")
        print(f"对象池中有：{len(self.__pool)}，已借：{len(list(filter(lambda x:x.isBusy(),self.__pool)))}，还剩：{len(list(filter(lambda x:not x.isBusy(),self.__pool)))}")
        return pooledObject.getObject() if pooledObject is not None else None

    def returnObject(self, obj):
        for pooledObject in self.__pool:
            if pooledObject.getObject() == obj:
                pooledObject.setBusy(False)
                print("{}对象已归返，time：{}".format(id(obj), strftime("%Y-%m-%d %H:%M:%s", localtime(time()))))
                return True

    def addObject(self):
        obj = None
        if len(self.__pool)<ObjectPool.maxNUmberOfObject:
            obj = self.createPooledObject()
            self.__pool.append(obj)
            print("添加新对象{}，time：{}".format(id(obj), strftime("%Y-%m-%d %H:%M:%s", localtime(time()))))
        return obj

    def clear(self):
        self.__pool.clear()

    def _findFreePooledObject(self):
        pooledObj = None
        for obj in self.__pool:
            if not obj.isBusy():
                pooledObj = obj
                break
        return pooledObj

class PowerBank:
    def __init__(self, serialNUmber, electricQuantity) -> None:
        self.__serialNumber = serialNUmber
        self.__electricQuantity = electricQuantity
        self.__user = "NA"

    def getSerialNumber(self):
        return self.__serialNumber

    def getElectricQuantity(self):
        return self.__electricQuantity

    def setElectricQuantity(self, electricQuantity):
        self.__electricQuantity = electricQuantity

    def setUser(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    def __str__(self) -> str:
        return "序列号：{}\t电量：{:.2%}\t使用者：{}".format(self.__serialNumber, self.__electricQuantity,self.__user)


class PowerBankPool(ObjectPool):
    __serialNumber = 0

    @classmethod
    def getSerilNUmber(cls):
        cls.__serialNumber += 1
        return "{:03d}".format(cls.__serialNumber)

    def createPooledObject(self):
        powerBank = PowerBank(PowerBankPool.getSerilNUmber(), 1)
        return PooledObject(powerBank)

if __name__ == "__main__":
    pbp = PowerBankPool()

    pb_1:PowerBank = pbp.borrowObject()
    if pb_1 is not None:
        pb_1.setUser("Nie")
        print(pb_1)
    pb_2:PowerBank = pbp.borrowObject()
    if pb_2 is not None:
        pb_2.setUser("Wen")
        print(pb_2)
    pb_3 = pbp.borrowObject()
    if pb_3 is not None:
        pb_3.setUser("Qing")
        print(pb_3)
    pb_4 = pbp.borrowObject()
    if pb_4 is not None:
        pb_4.setUser("Wen")
        print(pb_4)
    if pbp.returnObject(pb_2):
        pb_2.setUser("NA")
        pb_2.setElectricQuantity(0.74)
        print(pb_2)
    pb = pbp.borrowObject()
    if pb is not None:
        pb.setUser("Wen")
        print(pb)
    pb = pbp.borrowObject()
    if pb is not None:
        pb.setUser("Wen")
        print(pb)

    
    