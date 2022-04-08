# -*- encoding: utf-8 -*-
# @Author  :   Wenqing Nie
# @File    :   temp_test.py
# @Time    :   2022/02/05 13:53:49

from abc import ABC, abstractmethod


class Request:
    """请求（内容）的封装类"""
    pass

class Requester:
    """请求发送者"""

    def __init__(self, nextHandler = None) -> None:
        self._nextHandler: Responsible = nextHandler

    def sendRequest(self, request:Request):
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(request)

class Responsible(ABC):
    """请求处理者基类"""

    def __init__(self, nextHandler = None) -> None:
        self._nextHandler: Responsible = nextHandler

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    @abstractmethod
    def handleRequest(self, request: Request) -> None:
        pass

class NoteForLeave(Request):
    def __init__(self, name, day_off, reason) -> None:
        self._name = name
        self._day_off = day_off
        self._reason = reason

    def getName(self):
        return self._name

    def getDayOff(self):
        return self._day_off

    def getReason(self):
        return self._reason


class Leaver(Requester):
    """请假人"""

    def __init__(self, name, nextHandler: Responsible = None) -> None:
        super().__init__(nextHandler)
        self._name = name

    def setNextHandler(self, nextHandler: Responsible):
        self._nextHandler = nextHandler

    def sendRequest(self, request: NoteForLeave):
        print(
            f"{self._name} 申请请假 {request.getDayOff()} 天。请假事由：{request.getReason()}")
        return super().sendRequest(request)


class Supervisor(Responsible):
    """主管"""

    def __init__(self, name, title="Supervisor", nextHandler=None) -> None:
        super().__init__(nextHandler)
        self._name = name
        self._title = title

    def setnextHandler(self, nextHandler: Responsible):
        self._nextHandler = nextHandler

    def handleRequest(self, request: NoteForLeave):
        if request.getDayOff() <= 2:
            print(
                f"同意 {request.getName()} 请假 {request.getDayOff()} 天。签字人：{self._name}({self._title})")
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(request)


class DepartmentManager(Responsible):
    """部门总监"""

    def __init__(self, name, title="DepartmentManager", nextHandler=None) -> None:
        super().__init__(nextHandler)
        self._name = name
        self._title = title

    def setnextHandler(self, nextHandler: Responsible):
        self._nextHandler = nextHandler

    def handleRequest(self, request: NoteForLeave):
        if 2 < request.getDayOff() <= 5:
            print(
                f"同意 {request.getName()} 请假 {request.getDayOff()} 天。签字人：{self._name}({self._title})")
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(request)


class CEO(Responsible):
    """CEO"""

    def __init__(self, name, title="CEO", nextHandler=None) -> None:
        super().__init__(nextHandler)
        self._name = name
        self._title = title

    def setnextHandler(self, nextHandler: Responsible):
        self._nextHandler = nextHandler

    def handleRequest(self, request: NoteForLeave):
        if 5 < request.getDayOff() <= 22:
            print(
                f"同意 {request.getName()} 请假 {request.getDayOff()} 天。签字人：{self._name}({self._title})")
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(request)

class Administrator(Responsible):
    """行政人员"""

    def __init__(self, name, title="Administrator", nextHandler=None) -> None:
        super().__init__(nextHandler)
        self._name = name
        self._title = title

    def setnextHandler(self, nextHandler: Responsible):
        self._nextHandler = nextHandler

    def handleRequest(self, request: NoteForLeave):
        print(
            f"{request.getName()} 的请假申请已审核，情况属实！已备案处理。处理人：{self._name}({self._title})")
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(request)


if __name__ == "__main__":
    director_leader = Supervisor(name="Eren", title="客户端研发部经理")
    department_manager = DepartmentManager(name="Eric", title="技术研发中心总监")
    ceo = CEO(name="Helen", title="创新文化公司CEO")
    administrator = Administrator(name="Nina", title="行政中心总监")

    director_leader.setnextHandler(nextHandler=department_manager)
    department_manager.setnextHandler(nextHandler=ceo)
    ceo.setnextHandler(nextHandler=administrator)

    print("\n")
    sunny = Leaver(name="Sunny", nextHandler=director_leader)
    sunny.sendRequest(NoteForLeave(name=sunny._name,
                     day_off=1, reason="参加MDCC大会"))

    print("\n")
    tony = Leaver(name="Tony", nextHandler=director_leader)
    tony.sendRequest(NoteForLeave(name=sunny._name,
                                 day_off=5, reason="家里有急事"))

    print("\n")
    pony = Leaver(name="Pony", nextHandler=director_leader)
    pony.sendRequest(NoteForLeave(name=sunny._name,
                                 day_off=15, reason="出国深造"))
