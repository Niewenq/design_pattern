[TOC]

# 第一章 前言

## 1.1 初学者常犯的错误
1. 代码要规范；
2. 不要做无用功；
3. 考虑边界值，异常值；
4. 遇到问题，习惯性地用计算机能够理解的逻辑来描述和表达待解决的问题及具体的求解过程。这其实使用计算机的方式去思考，比如计算器这个程序，先要求输入两个数和符号，然后根据运算符号判断选择如何运算，得到结果，这本身没有错，但这样的思维却使得我们的程序只能满足当前的需求，程序不易<font color=red>**维护**</font>，不容易<font color=red>**扩展**</font>，更不容易<font color=red>**复用**</font>，从而达不到高质量代码的需求；

## 1.2 好的代码
刻版印刷、活字印刷与面向对象
1. 第一，要改，只需更改要改之字，此为<font color=red>**可维护**</font>；
2. 第二，这些字并非用完这次就无用，完全可以在后来的印刷中重复使用，此乃<font color=red>**可复用**</font>；
3. 第三，此诗若要加字，只需另刻字加入即可，这是<font color=red>**可扩展**</font>；
4. 第四，字的排列其实可能是竖排可能是横排，此时只需将活字移动就可做到满足排列需求，此是<font color=red>**灵活性好**</font> 。
5. 通过**封装**、**继承**、**多态**把程序的耦合度降低，用**设计模式**使得程序更加的灵活，容易修改，并且易于复用。

## 1.3 UML

Unified Modeling Language，统一建模语言

**泛化（Generalization）**是一种继承关系，表示一般与特殊的关系，它指定了子类如何特化父类的所有特征和行为。如：哺乳动物具有恒温、胎生、哺乳等生理特征，猫和牛都是哺乳动物，也都具有这些特征，但除此之外，猫会捉老鼠，牛会耕地。

**实现（Realization）**是一种类与接口的关系，表示类是接口所有特征和行为的实现。如：蝙蝠也是哺乳动物，它除具有哺乳动物的一般特征之外，还会飞，我们可以定义一个IFlyable的接口，表示飞行的动作，而蝙蝠需要实现这个接口。

**组合（Composition）**也表示整体与部分的关系，但部分离开整体后无法单独存在。因此，组合与聚合相比是一种更强的关系。如：我们的电脑由CPU、主板、硬盘、内存组成，电脑与CPU、主板、硬盘、内存是整体与部分的关系，但如果让CPU、主板等组件单独存在，就无法工作，因此没有意义。

**聚合（Aggregation）**是整体与部分的关系，部分可以离开整体而单独存在。如：一个公司会有多个员工，但员工可以离开公司单独存在，离职了依然可以好好地生活。

**关联（Association）**是一种拥有关系，它使一个类知道另一个类的属性和方法。关联可以是双向的，也可以是单向的。如：一本书会有多个读者，一个读者也可能会有多本书，书和读者是一种双向的关系（也就是多对多的关系）；但一本书通常只会有一个作者，是一种单向的关系（就是一对一的关系，也可能是一对多的关系，因为一个作者可能会写多本书）。

**依赖（Dependency）**是一种使用的关系，即一个类的实现需要另一个类的协助，所以尽量不要使用双向的互相依赖。如：所有的动物都要吃东西才能活着，动物与食物就是一种依赖关系，动物依赖食物而生存。

![UML](https://s2.loli.net/2022/04/01/RynekcCxmOotq2J.jpg)

## 1.4 SOLID设计原则

SOLID是面向对象设计（OOD）的五大基本原则的首字母缩写组合，由俗称“鲍勃大叔”的RobertC.Martin在《敏捷软件开发：原则、模式与实践》一书中提出来。这些原则结合在一起能够指导程序员开发出易于维护和扩展的软件。这五大原则分别是：S—单一职责原则，O—开放封闭原则，L—里氏替换原则，I—接口隔离原则，D—依赖倒置原则。

### 1.4.1 单一职责原则

单一职责原则，即Single Responsibility Principle，简称SRP。

一个类应该有且仅有一个原因引起它的变更。这句话这样说可能不太容易理解，解释一下。类T负责两个不同的职责（可以理解为功能）：职责P1，职责P2。当由于职责P1需求发生改变而需要修改类T时，可能会导致原本运行正常的职责P2功能发生故障，这就不符合单一职责原则。这时就应该将类T拆分成两个类T1、T2，使T1完成职责P1功能，T2完成职责P2功能。这样，当修改类T1时，不会使职责P2存在故障风险；同理，当修改T2时，也不会使职责P1存在故障风险。

一个类只负责一项功能或一类相似的功能。当然这个“一”并不是绝对的，应该理解为一个类只负责尽可能独立的一项功能，尽可能少的职责。就好比一个人的精力、时间都是有限的，如果什么事情都做，那么什么事情都做不好；所以应该集中精力做一件事，才能把事情做好。

### 1.4.2 开放封闭原则

开放封闭原则，即Open Close Principle，简称OCP。

软件实体（如类、模块、函数等）应该对拓展开放，对修改封闭。

在一个软件产品的生命周期内，不可避免会有一些业务和需求的变化，我们在设计代码的时候应该尽可能地考虑这些变化。在增加一个功能时，应当尽可能地不去改动已有的代码；当修改一个模块时不应该影响到其他模块。

### 1.4.3 里氏替换原则

里氏替换原则，即Liskov Substitution Principle，简称LSP。

所有能引用基类的地方必须能透明地使用其子类的对象。

一个类T有两个子类T1、T2，凡是能够使用T对象的地方，就能使用T1的对象或T2的对象，这是因为子类拥有父类的所有属性和行为。通俗来讲，只要父类能出现的地方子类就能出现（就可以用子类来替换它）。反之，子类能出现的地方父类不一定能出现（子类拥有父类的所有属性和行为，但子类拓展了更多的功能）。

里氏替换原则通俗来讲就是：子类可以扩展父类的功能，但不能改变父类原有的功能。也就是说：子类继承父类时，除添加新的方法完成新增功能外，尽量不要重写父类的方法。

### 1.4.4 接口隔离原则

接口隔离原则，即Interface Segregation Principle，简称ISP。

客户端不应该依赖它不需要的接口。用多个细粒度的接口来替代由多个方法组成的复杂接口，每一个接口服务于一个子模块。

类A通过接口interface依赖类C，类B通过接口interface依赖类D，如果接口interface对于类A和类B来说不是最小接口，则类C和类D必须去实现它们不需要的方法。

通俗来讲建立单一接口，不要建立庞大臃肿的接口，尽量细化接口，接口中的方法尽量少。也就是说，我们要为不同类别的类建立专用的接口，而不要试图建立一个很庞大的接口供所有依赖它的类调用。接口尽量小，但是要有限度。当发现一个接口过于臃肿时，就要对这个接口进行适当的拆分。但是如果接口过小，则会造成接口数量过多，使设计复杂化。所以接口大小一定要适度。

### 1.4.5 依赖倒置原则

依赖倒置原则，即Dependence Inversion Principle，简称DIP。

高层模块不应该依赖低层模块，二者都该依赖其抽象。抽象不应该依赖细节，细节应该依赖抽象。

高层模块就是调用端，低层模块就是具体实现类。抽象就是指接口或抽象类，细节是指具体的实现类。也就是说，我们只依赖抽象编程。把具有相同特征或相似功能的类，抽象成接口或抽象类，让具体的实现类继承这个抽象类（或实现对应的接口）。抽象类（接口）负责定义统一的方法，实现类负责具体功能的实现。

面向过程的开发，上层调用下层，上层依赖于下层，当下层剧烈变动时上层也要跟着变动，这就会导致模块的复用性降低而且大大提高了开发的成本。

面向对象的开发很好的解决了这个问题，一般情况下抽象的变化概率很小，让用户程序依赖于抽象，实现的细节也依赖于抽象。即使实现细节不断变动，只要抽象不变，客户程序就不需要变化。这大大降低了客户程序与实现细节的耦合度。

### 1.4.6 总结

1. 单一职责原则告诉我们实现类要职责单一。用于指导类的设计，增加一个类时使用单一职责原则来核对该类的设计是否纯粹干净。也就是让一个类的功能尽可能单一，不要想着一个类包揽所有功能。
2. 里氏替换原则告诉我们不要破坏继承体系。用于指导类继承的设计，设计类之间的继承关系时，使用里氏替换原则来判断这种继承关系是否合理。只要父类能出现的地方子类就能出现（就可以用子类来替换它），反之则不一定。
3. 依赖倒置原则告诉我们要面向接口编程。用于指导如何抽象，即要依赖抽象和接口编程，不要依赖具体的实现。
4. 接口隔离原则告诉我们在设计接口的时候要精简单一。用于指导接口的设计，当发现一个接口过于臃肿时，就要对这个接口进行适当的拆分。
5. 开放封闭原则告诉我们要对扩展开放，对修改封闭。开放封闭原则可以说是整个设计的最终目标和原则！开放封闭原则是总纲，其他四个原则是对这个原则的具体解释。

## 1.5 其它实用原则

### 1.5.1 迪米特法则

LoD原则（Law of Demeter）每一个逻辑单元应该对其他逻辑单元有最少的了解：也就是说只亲近当前的对象。只和直接（亲近）的朋友说话，不和陌生人说话。简单地说就是：一个类对自己依赖的类知道的越少越好，这个类只需要和直接的对象进行交互，而不用在乎这个对象的内部组成结构。例如，类A中有类B的对象，类B中有类C的对象，调用方有一个类A的对象a，这时如果要访问C对象的属性，不要采用类似下面的写法：`a.getB().getC().getProperties`，而应该是`a.getCProperties`。

至于getCProperties怎么实现是类A要负责的事情，我只和我直接的对象a进行交互，不访问我不了解的对象。

大家都知道大熊猫是我们国家的国宝，而为数不多的熊猫大部分都生活在动物园中。动物园内的动物种类繁多，展馆布局复杂，如有鸟类馆、熊猫馆等。假设某国外领导人来访华，参观我们的动物园，他想知道动物园内叫“贝贝”的大熊猫年龄多大，体重多少。他难道要先去调取熊猫馆的信息，然后去查找叫“贝贝”的这只大熊猫，再去看它的信息吗？显然不用，他只要问一下动物园的馆长就可以了。动物园的馆长会告诉他所有需要的信息，因为他只认识动物园的馆长，而且他并不了解动物园的内部结构，也不需要去了解。

### 1.5.2 KISS原则

Keep It Simple and Stupid

保持简单和愚蠢。

这一原则正如这句话本身一样容易理解。“简单”就是要让你的程序能简单、快速地被实现；“愚蠢”是说你的设计要简单到傻瓜都能理解，即简单就是美！

如果你的程序设计得太复杂，有些成员可能无法理解这种设计的真实意图，而且复杂的程序讲解起来也会增加沟通成本。为什么说愚蠢呢？对有同样需求的一个软件，每个人都有自己独特的思维逻辑和实现方式，因此你写的程序对于另一个人来说就是个陌生的项目。所以你的代码要愚蠢到不管是什么时候，不管是谁来接手这个项目，都能很容易地被看懂。

### 1.5.3 DRY原则

Don't repeat yourself

不要重复自己：不要重复你的代码，即多次遇到同样的问题，应该抽象出一个共同的解决方法，不要重复开发同样的功能。也就是要尽可能地提高代码的复用率。

要遵循DRY原则，实现的方式非常多。

1. 函数级别的封装：把一些经常使用的、重复出现的功能封装成一个通用的函数。
2. 类级别的抽象：把具有相似功能或行为的类进行抽象，抽象出一个基类，并把这几个类都有的方法提到基类去实现。
3. 泛型设计：Java中可使用泛型，以实现通用功能类对多种数据类型的支持；C++中可以使用类模板的方式，或宏定义的方式；Python中可以使用装饰器来消除冗余的代码。

### 1.5.4 YAGNI原则

You aren't gonna need it, don't implement something until it is necessary.

你没必要那么着急，不要给你的类实现过多的功能，直到你需要它的时候再去实现。这个原则简而言之为—只考虑和设计必需的功能，避免过度设计。只实现目前需要的功能，在以后需要更多功能时，可以再进行添加。如无必要，勿增加复杂性。软件开发首先是一场沟通博弈。它背后的指导思想就是尽可能快、尽可能简单地让软件运行起来。

### 1.5.5 三次法则

Rule of three

“三次法则”，指的是当某个功能第三次出现时，再进行抽象化，即事不过三，三则重构。这个准则表达的意思是：第一次实现一个功能时，就尽管大胆去做；第二次做类似的功能设计时会产生反感，但是还得去做；第三次还要实现类似的功能做同样的事情时，就应该去审视是否有必要做这些重复劳动了，这个时候就应该重构你的代码了，即把重复或相似功能的代码进行抽象，封装成一个通用的模块或接口。

1.5.6 CQS原则

Comm and Query Separation

查询（Query）：当一个方法返回一个值来回应一个问题的时候，它就具有查询的性质；

命令（Command）：当一个方法要改变对象的状态的时候，它就具有命令的性质。

通常，一个方法可能是单纯的查询模式或者是单纯的命令模式，也可能是两者的混合体。在设计接口时，如果可能，应该尽量使接口单一化（也就是方法级别的单一职责原则）。保证方法的行为严格的是命令或者查询，这样查询方法不会改变对象的状态，没有副作用；而会改变对象的状态的方法不可能有返回值。也就是说，如果我们要问一个问题，就不应该影响到它的答案。

原则的实际应用要视具体情况而定，需要权衡语义的清晰性和使用的简单性。将Command和Query功能合并入一个方法，方便了客户的使用，但是降低了清晰性。

这一原则尤其适用于后端接口设计，在一个接口中，尽量不要又有查数据又有更新（修改或插入）数据的操作。在系统设计中，很多系统也是以这样的原则去设计的（如数据库的主从架构），查询功能和命令功能的系统分离，有利于提高系统的性能，也有利于增强系统的安全性。

# 第二章 观察者模式

## 2.1 核心思想

监听模式又名观察者模式，顾名思义就是观察与被观察的关系。比如你在烧开水的时候看着它开没开，你就是观察者，水就是被观察者；再比如你在带小孩，你关注他是不是饿了，是不是渴了，是不是撒尿了，你就是观察者，小孩就是被观察者。观察者模式是对象的行为模式，又叫发布/订阅（Publish/Subscribe）模式，模型/视图（Model/View）模式，源/监听器（Source/Listener）模式或从属者（Dependents）模式。

监听模式是一种一对多的关系，可以有任意个（一个或多个）观察者对象同时监听某一个对象。监听的对象叫观察者（后面提到监听者，其实就指观察者，两者是相同的），被监听的对象叫被观察者（Observable，也叫主题，即Subject）。被观察者对象在状态或内容（数据）发生变化时，会通知所有观察者对象，使它们能够做出相应的变化（如自动更新子集的信息）。

观察者模式的核心思想就是在被观察者与观察者之间建立一种自动触发的关系。

## 2.2 UML类图

![观察者模式UML类图](https://s2.loli.net/2022/04/03/LSclsuVM5kQ2ioZ.jpg)

## 2.3 代码框架

```python
from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    """观察者基类

    Args:
        ABC (abc.ABCMeta): 申明为抽象基类
    """
    @abstractmethod
    def update(self, subject):
        """根据主题状态更新自己接口

        Args:
            subject (Subject): 订阅的主题类
        """
        pass


class Subject(ABC):
    """主题基类

    Args:
        ABC (abc.ABCMeta): 申明为抽象基类
    """

    def __init__(self, observers: "list[Observer]" = [], state: Any=None) -> None:
        """主题基类初始化函数

        Args:
            observers (list[Observer], optional): 订阅该主题观察者列表. Defaults to [].
            state (Any, optional): 主题初始化状态. Defaults to None.
        """
        self.__observers = observers
        self.__state = state

    def addObserver(self, observer: Observer):
        """为主题添加观察者

        Args:
            observer (Observer): 待添加的观察者
        """
        self.__observers.append(observer)

    def removeObserver(self, observer: Observer):
        """为主题移除观察者

        Args:
            observer (Observer): 待移除的观察者
        """
        self.__observers.remove(observer)

    def getState(self):
        """获取subject状态

        Returns:
            Any: Subject此时的状态
        """
        return self.__state

    def notify(self):
        """通知订阅该主题的观察者
        """
        for o in self.__observers:
            o.update(self)

    @abstractmethod
    def change(self, state):
        """subject状态改变

        Args:
            state (Any): subject状态
        """
        self.__state = state


class ObserverImplA(Observer):
    """观察者实现类A

    Args:
        Observer (Class): 观察者基类
    """
    def update(self, subject:  Subject):
        """根据subject传来的state，给出不同的操作

        Args:
            subject (Subject): 订阅的主题
        """
        if subject.getState() == "A":
            print(f"{self.__class__.__name__} is updating...")


class ObserverImplB(Observer):
    """观察者实现类B

    Args:
        Observer (Class): 观察者基类
    """
    def update(self, subject: Subject):
        """根据subject传来的state，给出不同的操作

        Args:
            subject (Subject): 订阅的主题
        """
        if subject.getState() == "B":  # 根据state状态，做出相应的动作
            print(f"{self.__class__.__name__} is updating...")

1
class SubjectImpl(Subject):
    """主题具体实现类

    Args:
        Subject (Class): 主题抽象基类
    """
    def change(self, state):
        """改变主题状态

        Args:
            state (Any): 待转换的状态
        """
        super().change(state)


if __name__ == "__main__":
    observerA = ObserverImplA()
    observerB = ObserverImplB()
    subject = SubjectImpl(observers=[observerA, observerB])

    subject.change(state="A")
    subject.notify()
    print("*" * 35)
    subject.change(state="B")
    subject.notify()
```



## 2.4 模型说明

### 2.4.1 设计要点

在设计监听模式的程序时要注意以下几点：

1. 要明确谁是观察者谁是被观察者，只要明白谁是应该关注的对象，问题也就明白了。一般观察者与被观察者之间是多对一的关系，一个被观察对象可以有多个监听对象（观察者）。如一个编辑框，有鼠标点击的监听者，也有键盘的监听者，还有内容改变的监听者。
2. Observable 在发送广播通知的时候，无须指定具体的 Observer，Observer可以自己决定是否订阅Subject的通知。
3. 被观察者至少需要有三个方法：添加监听者、移除监听者、通知Observer的方法。观察者至少要有一个方法：更新方法，即更新当前的内容，做出相应的处理。
4. 添加监听者和移除监听者在不同的模型称谓中可能会有不同命名，如在观察者模型中一般是addObserver/removeObserver；在源/监听器（Source/Listener）模型中一般是attach/detach，应用在桌面编程的窗口中还可能是attachWindow/detachWindow或Register/Unregister。不要被名称弄迷糊了，不管它们是什么名称，其实功能都是一样的，就是添加或删除观察者。

### 2.4.2 推模型和拉模型

监听模式根据其侧重的功能还可以分为推模型和拉模型。推模型和拉模型其实更多的是语义和逻辑上的区别。

+ 推模型：被观察者对象向观察者推送主题的详细信息，不管观察者是否需要，推送的信息通常是主题对象的全部或部分数据。一般在这种模型的实现中，会把被观察者对象中的全部或部分信息通过update参数传递给观察者（update（Objectobj），通过obj参数传递）。如某App的服务要在凌晨1:00开始进行维护，1:00—2:00所有服务会暂停，这里你就需要向所有的App客户端推送完整的通知消息：“本服务将在凌晨1:00开始进行维护，1:00—2:00所有服务会暂停，感谢您的理解和支持！”不管用户想不想知道，也不管用户会不会在这期间访问App，消息都需要被准确无误地发送到。这就是典型的推模型的应用。
+ 拉模型：被观察者在通知观察者的时候，只传递少量信息。如果观察者需要更具体的信息，由观察者主动到被观察者对象中获取，相当于观察者从被观察者对象中拉数据。一般在这种模型的实现中，会把被观察者对象自身通过 update 方法传递给观察者（update（Observable observable），通过observable 参数传递），这样在观察者需要获取数据的时候，就可以通过这个引用来获取了。如某App有新的版本推出，需要发送一个版本升级的通知消息，而这个通知消息只会简单地列出版本号和下载地址，如果需要升级App，还需要调用下载接口去下载安装包完成升级。这其实也可以理解成拉模型。

### 2.4.3 优缺点

1. 优点
    + 观察者和被观察者是抽象耦合的。 
    + 建立一套触发机制。

2. 缺点
    + 如果一个被观察者对象有很多的直接和间接的观察者的话，将所有的观察者都通知到会花费很多时间。 
    + 如果在观察者和观察目标之间有循环依赖的话，观察目标会触发它们之间进行循环调用，可能导致系统崩溃。 
    + 观察者模式没有相应的机制让观察者知道所观察的目标对象是怎么发生变化的，而仅仅只是知道观察目标发生了变化。

## 2.5 应用场景

1. 对一个对象状态或数据的更新需要其他对象同步更新，或者一个对象的更新需要依赖另一个对象的更新。
2. 对象仅需要将自己的更新通知给其他对象而不需要知道其他对象的细节，如消息推送。

# 第三章 状态模式

## 3.1 核心思想

允许一个对象在其内部状态发生改变时改变其行为，使这个对象看上去就像改变了它的类型一样。状态模式是说一个对象在其内部状态发生改变时，其表现的行为和外在属性不一样，这个对象看上去就像改变了它的类型一样。因此，状态模式又称为对象的行为模式。

比如生活中，水有三种不同状态：冰、水、水蒸气。三种不同的状态有着完全不一样的外在特性：冰，质坚硬，无流动性，表面光滑；水，具有流动性；水蒸气：质轻，肉眼看不见，却存在于空气中。这三种状态的特性差距很大，根本不像是同一种东西，但事实却是不管它在什么状态，其内部组成都是一样的，都定水分子（$H_2O$）。

<font color=red>__状态模式的核心思想__</font>就是一个事物（对象）有多种状态，在不同的状态下所表现出来的行为和属性不一样。

## 3.2 UML类图

![状态模式UML类图](https://s2.loli.net/2022/04/03/Tsa86tOxpgkB3Sw.jpg)

## 3.3 代码框架

```python
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
```



## 3.4 模型说明

### 3.4.1 设计要点

1. 在实现状态模式的时候，实现的场景状态有时候会非常复杂，决定状态变化的因素也非常多，我们可以把决定状态变化的属性单独抽象成一个类StateInfo，这样判断状态属性是否符合当前的状态 isMatch 时就可以传入更多的信息。
2. 每一种状态应当只有唯一的实例。

### 3.4.2 优缺点

1. 优点:
    + 封装了状态的转换规则，在状态模式中可以将状态的转换代码封装在环境类中，对状态转换代码进行集中管理,而不是分散在一个个业务逻辑中。
    + 将所有与某个状态有关的行为放到一个类中（称为状态类)，使开发人员只专注于该状态下的逻辑开发。
    + 允许状态转换逻辑与状态对象合为一体，使用时只需要注入一个不同的状态对象即可使环境对象拥有不同的行为。

2. 缺点:
    + 会增加系统类和对象的个数。
    + 状态模式的结构与实现都较为复杂，如果使用不当容易导致程序结构和代码的混乱。

## 3.5 应用场景

1. 一个对象的行为取决于它的状态，并且它在运行时可能经常改变它的状态，从而改变它的行为。
2. 一个操作中含有庞大的多分支的条件语句，这些分支依赖于该对象的状态，且每一个分支的业务逻辑都非常复杂时，我们可以使用状态模式来拆分不同的分支逻辑，使程序有更好的可读性和可维护性。

# 第四章 中介模式

## 4.1 核心思想

由中介来承接房客与房东之间的交互过程，可以使得整个租房过程更加畅通、高效。这在程序中叫作中介模式，中介模式又称为调停模式。

在很多系统中，多个类很容易相互耦合，形成网状结构。中介模式的作用就是将这种网状结构分离成星型结构。经过这样的调整后，对象之间的结构更加简洁，交互更加顺畅。

![网状和星型结构](https://s2.loli.net/2022/04/03/xvoTFKp9Qqw2csm.jpg)

## 4.2 UML类图

![中介者模式UML类图](https://s2.loli.net/2022/04/04/x8chEFHBJ41lguO.jpg)

## 4.3 代码框架

```python
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
    # 交互对象认识中介对象
    interacivaObjectImplA=InteracivaObjectImplA(mediator)
    interacivaObjectImplB=InteracivaObjectImplB(mediator)
    # 中介对象认识每个交互对象
    mediator.setInteractiveObjectImplA(interacivaObjectImplA)
    mediator.setInteractiveObjectImplB(interacivaObjectImplB)
    # 交互对象A和交互对象B通过中介对象交流
    interacivaObjectImplA.send("Have you eaten dinner?")
    interacivaObjectImplB.send("Not yet, do you want to invite me?")
```



## 4.4 模型说明

### 4.3.1 设计要点

中介模式主要有以下三个角色，在设计中介模式时要找到并区分这些角色：

1. 交互对象（InteractiveObject）：要进行交互的一系列对象。
2. 中介者（Mediator）：负责协调各个对象之间的交互。
3. 具体中介者（Mediator）：中介的具体实现。

### 4.3.2 优缺点

1. 优点
    + Mediator将原本分布于多个对象间的行为集中在一起，作为一个独立的概念并将其封装在一个对象中，简化了对象之间的交互。
    + 将多个调用者与多个实现者之间多对多的交互关系，转换为一对多的交互关系，一对多的交互关系更易于理解、维护和扩展，大大减少了多个对象之间相互交叉引用的情况。

2. 缺点
    + 中介者承接了所有的交互逻辑，交互的复杂度转变成了中介者的复杂度，中介者类会变得越来越庞大和复杂，以至于难以维护。
    + 中介者出问题会导致多个使用者同时出问题。

## 4.5 应用场景

1. 一组对象以定义良好但复杂的方式进行通信。产生的相互依赖关系结构混乱且难以理解。
2. 一个对象引用其他很多对象并且直接与这些对象通信，导致难以复用该对象。
3. 想通过一个中间类来封装多个类中的行为，同时又不想生成太多的子类。

# 第五章 装饰器模式

## 5.1 核心思想

动态地给一个对象增加一些额外的职责而不改变原来的代码。

## 5.2 UML类图

![装饰模式UML类图](https://s2.loli.net/2022/04/04/MFg4ok78dqaAx62.jpg)

## 5.3 框架代码

```python
from abc import ABC, abstractmethod
import sys


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ComponentImpl(Component):
    def operation(self):
        print(f"----{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._decorated = component

    def operation(self):
        self._decorated.operation()
        self.addBehavior()

    @abstractmethod
    def addBehavior(self):
        pass


class DecoratorImplA(Decorator):
    def addBehavior(self):
        print(f"----{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
  

class DecoratorImplB(Decorator):
    def addBehavior(self):
        print(f"----{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


if __name__ == "__main__":
    A = ComponentImpl()
    print("ComponentImpl")
    A.operation()
    D_A = DecoratorImplA(component=A)
    print("ComponentImpl DecoratorImplA")
    D_A.operation()
    D_B = DecoratorImplB(component=A)
    print("ComponentImpl DecoratorImplB")
    D_B.operation()
    D_AB = DecoratorImplB(component=D_A)
    print("ComponentImpl DecoratorImplA DecoratorImplB")
    D_AB.operation()
```

## 5.4 模型说明

### 5.4.1 设计要点

1. 可灵活地给一个对象增加职责或拓展功能。你可任意地穿上自己想穿的衣服。不管穿上什么衣服，你还是那个你，但穿上不同的衣服你就会有不同的外表。
2. 可增加任意多个装饰你可以只穿一件衣服，也可以只穿一条裤子，也可以衣服和裤子搭配着穿，随你意！
3. 装饰的顺序不同，可能产生不同的效果。

### 5.4.2 优缺点

1. 优点
    + 使用装饰模式来实现扩展比使用继承更加灵活，它可以在不创造更多子类的情况下，将对象的功能加以扩展。
    + 可以动态地给一个对象附加更多的功能。
    + 可以用不同的装饰器进行多重装饰，装饰的顺序不同，可能产生不同的效果。
    + 装饰类和被装饰类可以独立发展，不会相互耦合；装饰模式相当于继承的一个替代模式。
2. 缺点
    + 与继承相比，用装饰的方式拓展功能容易出错，排错也更困难。对于多次装饰的对象，调试寻找错误时可能需要逐级排查，较为烦琐。所以设计装饰器时，保证装饰类之间彼此独立，这样它们就可以以任意的顺序进行组合了。

## 5.5 Python中装饰器

### 5.3.1 无参函数装饰器

使用语法糖之前：

```python
from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"logger\t\t开始执行:{datetime.now()}")
        func(*args, **kwargs)
        print(f"logger\t\t执行完毕{datetime.now()}")
    return wrapper


def function(name="Wenqing Nie", age=18):
    print(f"function\thi everyone, I'm {name}, {age} years old.")


if __name__ == "__main__":
    logger(function)(name="Wu Zun", age=38)
```

使用语法糖之后：

```python
from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"logger\t\t开始执行:{datetime.now()}")
        func(*args, **kwargs)
        print(f"logger\t\t执行完毕{datetime.now()}")
    return wrapper


@logger
def function(name="Wenqing Nie", age=18):
    print(f"function\thi everyone, I'm {name}, {age} years old.")


if __name__ == "__main__":
    function(name="Wu Zun", age=38)
```

### 5.3.2 无参类装饰器

装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。使用类装饰器主要依靠类的`__call__`方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。

```python
from datetime import datetime
from typing import Any


class Logger(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"logger\t\t开始执行:{datetime.now()}")
        self._func(*args, **kwargs)
        print(f"logger\t\t执行完毕{datetime.now()}")


@Logger
def function(name="Wenqing Nie", age=18):
    print(f"function\thi everyone, I'm {name}, {age} years old.")


if __name__ == "__main__":
    function()
```

### 5.3.3 有参函数装饰器

使用语法糖之前：

```python
from datetime import datetime


def logger(level="Info"):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f"[{level}]:\t开始执行:{datetime.now()}")
            func(*args, **kwargs)
            print(f"[{level}]:\t执行完毕{datetime.now()}")
        return inner_wrapper
    return outer_wrapper


def function(name="Wenqing Nie", age=18):
    print(f"function\thi everyone, I'm {name}, {age} years old.")


if __name__ == "__main__":
    logger("Error")(function)(name="WuJing", age=38)
```

使用语法糖之后：

```python
from datetime import datetime


def logger(level="Info"):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f"[{level}]:\t开始执行:{datetime.now()}")
            func(*args, **kwargs)
            print(f"[{level}]:\t执行完毕{datetime.now()}")
        return inner_wrapper
    return outer_wrapper

@logger("Error")
def function(name="Wenqing Nie", age=18):
    print(f"function\thi everyone, I'm {name}, {age} years old.")


if __name__ == "__main__":
    function(name="WuJing", age=38)
```

### 5.3.4 有参类装饰器

```python
from datetime import datetime
from pyclbr import Function
from typing import Any


class Logger:
    def __init__(self, level='INFO'):
        self._level = level

    def __call__(self, func: Function) -> Any:
        def wrapper(*args, **kwargs):
            print(f"[{self._level}]:\t开始执行:{datetime.now()}")
            func(*args, **kwargs)
            print(f"[{self._level}]:\t执行完毕{datetime.now()}")
        return wrapper


@Logger("Error")
def function(name="Wenqing Nie", age=18):
    print(f"function\thi everyone, I'm {name}, {age} years old.")


if __name__ == "__main__":
    function(name="WuJing", age=38)
```

### 5.3.5 修饰类

因为类和函数一样，都是对象，函数传入的是`func`，类装饰器需要传入`cls`。

```python
def singleton(cls):
    "构造一个单例的装饰器"
    instance = {}
    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton
```

### 5.3.6 闭包自由变量

```Python
>>> def make_averager():
...     series = []
...     def averager(new_value):
...         series.append(new_value)
...         total = sum(series)
...         return total/len(series)
...     return averager
... 
>>> avg = make_averager()
>>> avg(10) 
10.0
>>> avg(11) 
10.5
>>> avg(12) 
11.0
```

示例中 `avg` 函数在哪里寻找` series` 呢？？

注意，`series` 是 `make_averager `函数的局部变量，因为那个函数的定义体中初始化了` series: series = [ ]`。可是，调用` avg(10)` 时，`make_averager` 函数已经返回了，而它的本地作用域也一去不复返了。在 `averager `函数中，`series` 是自由变量（`free variable`）。这是一个技术术语，指未在本地作用域中绑定的变量，参见下图。

![闭包自由变量](https://s2.loli.net/2022/04/04/V97ksz24XxdGcU1.jpg)

审查返回的 `averager `对象，我们发现` Python` 在`__code__`属性（表示编译后的函数定义体）中保存局部变量和自由变量的名称，`series` 的绑定在返回的` avg` 函数的`__closure__`属性中。`avg.__closure__` 中的各个元素对应于`avg.__code__.co_freevars` 中的一个名称。这些元素是`cell`对象，有个`cell_contents`属性，保存着真正的值。这些属性的值如下所示：

```python
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__
(<cell at 0x000001201CCF6D00: list object at 0x000001201D19E540>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
```

综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。

注意，只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量。

## 5.6 python装饰器和装饰器模式的区别

|  区别点  |                         python装饰器                         |          装饰模式          |
| :------: | :----------------------------------------------------------: | :------------------------: |
| 设计思想 |                        函数式编程思想                        |     面向对象的编程思想     |
| 装饰对象 |               可以装饰一个函数也可以装饰一个类               | 修饰的是某和类中的指定方法 |
| 影响范围 | 装饰一个函数时，对这个函数的所有调用都起效；修饰一个类时，对这个类的所有实例都起效 |    只对修饰的该对象起效    |

## 5.7 应用场景

1. 有大量独立的扩展，为支持每一种组合将产生大量的子类，使得子类数目呈爆炸性增长时。
2. 需要动态地增加或撤销功能时。
3. 不能采用生成子类的方法进行扩充时，类的定义不能用于生成子类(（如Java 中的 final类)。

# 第六章 单例模式

## 6.1 核心思想

确保一个类只有一个实例，并且提供一个访问它的全局方法。

## 6.2 UML类图

![单例模式UML类图](https://s2.loli.net/2022/04/04/rWXSjqbZwpg6ztl.jpg)

## 6.3 框架代码

使用装饰器实现

```python
def singleton(cls):
    "构造一个单例的装饰器"
    instance = {}
    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton
```

通过修改`__new__`函数实现

```python
class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
```



## 6.4 应用场景

1. 你希望这个类只有一个且只能有一个实例。
2. 项目中的一些全局管理类（Manager）可以用单例模式来实现。

# 第七章 克隆模式

## 7.1 核心思想

用原型实例指定要创建对象的种类，并通过拷贝这些原型的属性来创建新的对象。

通过拷贝自身的属性来创建一个新对象的过程叫作克隆模式（Clone）。在很多书籍和资料中被称为原型模式。

## 7.2 UML类图

![克隆模式UML类图](https://s2.loli.net/2022/04/04/tdITwfzQ8LMl3bW.jpg)

## 7.3 框架代码

```python
from copy import copy, deepcopy


class Clone:
    """克隆基类"""

    def clone(self):
        """通过浅拷贝的方式克隆对象"""
        return copy(self)

    def deepClone(self):
        """通过深拷贝的方式克隆对象"""
        return deepcopy(self)
```

## 7.4 优缺点

1. 优点:
    + 克隆模式通过内存拷贝的方式进行复制，比 new 的方式创建对象性能更好。
    + 通过深拷贝的方式，可以方便地创建一个具有相同属性和行为的另一个对象，特别是对于复杂对象，方便性尤为突出。

1. 缺点：
    + 通过克隆的方式创建对象，**不会执行类的初始化函数(\_\_init\_\_)**。这不一定是缺点，但大家使用的时候需要注意这一点。

## 7.5 应用场景

1. 如果创建新对象（如复杂对象）成本较高，我们可以利用已有的对象进行复制来获得。
2. 类的初始化需要消耗非常多的资源时，如需要消耗很多的数据、硬件等资源。
3. 可配合备忘录模式做一些备份的工作。

# 第八章 职责链模式

## 8.1 核心思想

为避免请求发送者与接收者耦合在一起，让多个对象都有可能接收请求。将这些接收对象连接成一条链，并且沿着这条链传递请求，直到有对象处理它为止。__职责模式__也称为__责任链模式__，它将请求的发送者和接收者解耦了。客户端不需要知道请求处理者的明确信息和处理的具体逻辑，甚至不需要知道链的结构，它只需要将请求进行发送即可。

比如请教条的审批，我们并不需要知道假条处理的具体细节，甚至不需要知道假条去哪儿了，只需要知道假条有人会处理。而假条的处理流程是一手接一手的责任传递，处理假条的所有人构成了一条责任的链条，如下图所示。

![处理请假条流程](https://s2.loli.net/2022/04/04/H5UPjcEWCZoz6rS.jpg)

链条上的每一个人只处理自己职责范围内的请求，对于自己处理不了的请求，直接交给下一个责任人。这就是程序设计中职责模式的核心思想。在职责模式中我们可以随时随地增加或者更改责任人，甚至可以更改责任人的顺序，增加了系统的灵活性。但是有时候可能会导致一个请求无论如何也得不到处理，它会被放置在链条末端。

## 8.2 UML类图

![职责模式UML类图](https://s2.loli.net/2022/04/05/jcCJv6G9gVubQrB.jpg)

## 8.3 框架代码

```python
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
```

## 8.4 模型说明

### 8.4.1 设计要点

在设计职责模式的程序时要注意以下几点：

1. 请求者与请求内容：确认谁要发送请求，发送请求的对象称为请求者。请求的内容通过发送请求时的参数进行传递。

2. 有哪些责任人：责任人是构成责任链的关键要素。请求的流动方向是链条中的线，而责任人则是链条上的节点，线和节点共同构成了一条链条。
3. 对责任人进行抽象：真实世界中的责任人多种多样，纷繁复杂，有不同的职责和功能；但他们也有一个共同的特征——都可以处理请求。所以需要对责任人进行抽象，使他们具有责任的可传递性。
4. 责任人可自由组合：责任链上的责任人可以根据业务的具体逻辑进行自由的组合和排序。

### 8.4.2 优缺点

1. 优点：

    + 降低耦合度。它将请求的发送者和接收者解耦。

    + 简化了对象。它使得对象不需要知道链的结构。

    + 增强给对象指派职责的灵活性，可改变链内的成员或者调动它们的次序，允许动态地新增或者删除责任人。

    + 增加新的处理类很方便。


2. 缺点：

    + 不能保证请求一定被接收。

    + 系统性能将受到一定的影响，而且在进行代码调试时不太方便，可能会造成循环调用。


## 8.5 应用场景

1. 有多个对象可以处理同一个请求，具体哪个对象处理该请求在运行时刻自动确定。
2. 请求的处理具有明显的一层层传递关系。
3. 请求的处理流程和顺序需要程序运行时动态确定。
4. 常见的审批流程（账务报销、转岗申请等）。

# 第九章 代理模式

## 9.1 核心思想

一个对象完成某项动作或任务，是通过对另一个对象的引用来完成的，这种模式叫代理模式。

代理模式核心思想是：

1. 使用一个额外的间接层来支持分散的、可控的、智能的访问。
2. 增加一个包装和委托来保护真实的组件，以避免过度复杂。

代理对象可以在客户端和目标对象之间起到中间调和的作用，并且可以通过代理对象隐藏不希望被客户端看到的内容和服务，或者添加客户需要的额外服务。在现实生活中能找到非常多的代理模式的模型：火车票和机票的代售点、代表公司出席商务会议。

## 9.2 UML类图

![代理模式UML类图](https://s2.loli.net/2022/04/05/s3TNBaWmyeP7ukt.jpg)

## 9.3 框架代码

```python
from abc import ABC, abstractmethod


class Subject(ABC):
    """主题抽象类，将要被代理的类"""

    @abstractmethod
    def request(self, content=None):
        """任务请求方法"""
        pass


class RealSubject(Subject):
    """真实主题类，具体任务类"""

    def request(self, content):
        print(f"{self.__class__.__name__}'s assignment --> {content}")


class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, subject: RealSubject):
        """传入被代理的对象"""
        self._realSubject = subject

    def preRequest(self):
        print(f"{self.__class__.__name__}'s prework")

    def afterRequest(self):
        print(f"{self.__class__.__name__}'s afterwork")

    def request(self, content=None) -> None:
        self.preRequest()
        if self._realSubject is not None:
            self._realSubject.request(content)
        self.afterRequest()


if __name__ == "__main__":
    realObj = RealSubject()
    proxyObj = ProxySubject(realObj)
    proxyObj.request("do homework")

```



## 9.4 模型说明

### 9.2.1 设计要点

代理模式中主要有三个角色，在设计代理模式时要找到并区分这些角色。

+ 主题（Subject）：定义操作、活动、任务的接口类。
+ 真实主题（RealSubject）：真正完成操作、活动、任务的具体类。
+ 代理主题（ProxySubject）：代替真实主题完成操作、活动、任务的代理类。

### 9.2.2 优缺点

1. 优点

    + 代理模式能够协调调用者和被调用者，在一定程度上降低系统的耦合度。

    + 可以灵活地隐藏被代理对象的部分功能和服务，也可以增加额外的功能和服务。


2. 缺点

    + 由于在客户端和真实主题之间增加了代理对象，因此有些类型的代理模式可能会造成请求的处理速度变慢。

    + 实现代理模式需要额外的工作，有些代理模式的实现非常复杂。


## 9.5 应用场景

1. 不想或者不能直接引用一个对象时，如在移动端加载网页信息时，因为下载真实大图比较耗费流量、影响性能，可以用一个小图代替进行渲染（用一个代理对象去下载小图），在真正点击图片时，才下载大图，显示大图效果。还有HTML 中的占位符，其实也是代理模式的思想。
2. 想对一个对象的功能进行加强时，如在字体（Font）渲染时，对粗体（BoldFont）进行渲染时，可使用字体Font对象进行代理，只要在对Font进行渲染后进行加粗的操作即可。
3. 各种特殊用途的代理：远程代理、虚拟代理、Copy-on-Write 代理、保护（Protect or Access）代理、Cache代理、防火墙（Firewall）代理、同步化（Synchronization）代理、智能引用（SmartReference）代理。

# 第十章 外观模式

## 10.1 核心思想

为子系统中的一组接口提供一个一致的界面称为<font color=red>__外观模式__</font>，外观模式定义了一个高层接口，这个接口使得这―子系统更容易使用。

比如生活中的志愿者，他们相当于一个对接人，将复杂的业务通过一个对接人来提供一整套统一的（一条龙式的）服务，让用户不用关心内部复杂的运行机制。这种方式在程序中叫外观模式，也叫门面模式。

迎新志愿者陪同并帮助入学新生完成报到登记、缴纳学费、领日用品、入住宿舍等一系列的报到流程。新生不用知道具体的报到流程，不用去寻找各个场地；只要跟着志愿者走，到指定的地点，根据志愿者的指导，完成指定的任务即可。志愿者虽然不直接提供这些报到服务，但也相当于间接提供了报到登记、缴纳学费、领日用品、入住宿舍等条龙的服务，帮新生减轻了不少麻烦和负担。
<font color=red>__外观模式的核心思想__</font>：用一个简单的接口来封装一个复杂的系统,使这个系统更容易使用。

## 10.2 UML类图

![外观模式UML类图](https://s2.loli.net/2022/04/05/iA4RQDZhYe7LqKP.jpg)

## 10.3 框架代码

```python
import sys


class SubSystemA():
    def function(self):
        """子系统类A的功能函数，实现子系统A的功能，处理Facade对象指派的任务"""
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


class SubSystemB():
    def function(self):
        """子系统类B的功能函数，实现子系统B的功能，处理Facade对象指派的任务"""
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


class Facade():
    def __init__(self) -> None:
        self._subSystemA = SubSystemA()
        self._subSystemB = SubSystemB()

    def functionA(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        self._subSystemA.function()

    def functionB(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        self._subSystemB.function()


if __name__ == "__main__":
    facade = Facade()
    facade.functionA()
    print("-" * 50)
    facade.functionB()
```

## 10.4 模型说明

### 10.4.1 设计要点

外观模式是最简单的设计模式之一，只有以下两个角色：

1. 外观角色（Facade）：为子系统封装统一的对外接口，如同子系统的门面。这个类一般不负责具体的业务逻辑，只是一个委托类，具体的业务逻辑由子系统完成。
2. 子系统（SubSystem）：由多个类组成的具有某一特定功能的子系统。可以是第三方库，也可以是自己的基础库，还可以是一个子服务，为整个系统提供特定的功能或服务。

### 10.4.2 优缺点

1. 优点：
    + 实现了子系统与客户端之间的松耦合关系，这使得子系统的变化不会影响调用它的客户端。
    + 简化了客户端对子系统的使用难度，客户端（用户）无须关心子系统的具体实现方式而只需要和外观进行交互即可。
    + 为不同的用户提供了统一的调用接口，方便了系统的管理和维护。
2. 缺点：
    + 因为统一了调用的接口，降低了系统功能的灵活性。

## 10.5 应用场景

1. 要为一个复杂子系统提供一个简单接口时。
2. 客户程序与多个子系统之间存在很大的依赖性时。引入外观类将子系统与客户以及其他子系统解耦，可以提高子系统的独立性和可移植性。
3. 在层次化结构中，可以使用外观模式定义系统中每一层的入口，层与层之间不直接产生联系，而通过外观类建立联系，降低层之间的耦合度。

# 第十一章 迭代模式

## 11.1 核心思想

提供一种方法顺序地访问一组聚合对象（一个容器）中的各个元素，而又不需要暴露该对象的内部细节。

迭代模式也称为迭代器模式。迭代器其实就是一个指向容器中当前元素的指针，这个指针可以返回当前所指向的元素，可以移到下一个元素的位置，通过这个指针可以遍历容器中的所有元素。

比如医院的排号系统，通过数字化的方式精确地维护着先来先就诊的秩序。医生不用在乎外面有多少人在等待，更不需要了解每一个人的名字和具体信息。他只要在诊断完一个病人后按一下按钮，排号系统就会自动为他呼叫下一位病人，这样医生就可专注于病情的诊断！这个排号系统就如同程序设计中的迭代模式。

## 11.2 UML类图

![迭代模式UML类图](https://s2.loli.net/2022/04/05/1JRMk8gZK2zaQf5.jpg)

## 11.3 框架代码

```python
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
```

## 11.4 模型说明

1. 设计要点，在设计迭代模式时，要注意以下几点：
    + 了解容器的数据结构及可能的层次结构。
    + 根据需要确定迭代器要实现的功能，如next()、previous()、current()、toBegin()、toEnd()中的一个或几个。
2. 优缺点：
    1. 优点:
        + 迭代器模式将存储数据和遍历数据的职责分离。
        + 简化了聚合数据的访问方式。
        + 可支持多种不同的方式（如顺序和逆序）遍历一个聚合对象。
    2. 缺点：
        + 需要额外增加迭代器的功能实现，增加新的聚合类时，可能需要增加新的迭代器。

## 11.5 python中迭代器和生成器

迭代是Python中常用且非常强大的一个功能，它可以用于访问集合、列表、字符串、字典等数据结构的元素。我们经常使用循环和条件语句，我们也清楚哪些是可以迭代访问，但是具体它们之间有什么有什么异同之处？有哪些特点？什么是迭代器、什么是生成器、什么是可迭代对象？

### 11.5.1 可迭代对象

![可迭代对象](https://s2.loli.net/2022/04/05/GOdU81Q39k2FWA7.jpg)

可迭代对象是Python中一个非常庞大的概念，它主要包括如下三类：

- 迭代器
- 序列
- 字典

从上图可以看出不同概念之间的关系，迭代器是可迭代对象的一个子集，而生成器又是迭代器的一个子集，是一种特殊的迭代器。除了迭代器之外，Python中还有序列、字典等可迭代对象。

现在已经直观的了解了可迭代对象与迭代器、生成器之间的关系，那么用Python语言怎么表述它们的区别呢？

- **可迭代对象需要实现`__iter__`方法**
- **迭代器不仅要实现`__iter__`方法，还需要实现`__next__`方法**

在使用层面，可迭代对象可以通过**`in`**和**`not in`**访问对象中的元素，举一个例子，

```python
X = set([1,2,3,4,5])
print(X)
print(type(X))
print(1 in X)
print(2 not in X)
for x in X:
    print(x)
    
# 输出
{1, 2, 3, 4, 5}
<class 'set'>
True
False
1
2
3
4
5
```

前面提到，可迭代对象实现了`__iter__`方法，但是它没有实现`__next__`，这也是判定迭代器和其他可迭代对象的关键之处，可以看一下通过next访问上述示例中可迭代对象`X`会报错，

```python
next(X)

# 输出
TypeError: 'set' object is not an iterator
```

报的错误是`'set' object is not an iterator`，它指明了set集合是一个可迭代对象，但不是迭代器，下面就来介绍一下迭代器。

### 11.5.2 迭代器

迭代器是可迭代对象的一个子集，它是一个可以记住遍历的位置的对象，它与列表、元组、集合、字符串这些可迭代对象的区别就在于next方法的实现，其他列表、元组、集合、字符串这些可迭代对象可以很简单的转化成迭代器，通过Python内置的`iter`数能够轻松把可迭代对象转化为迭代器，下面来看一个例子，

```python
X = [1,2,3,4,5]
print(type(X))
Y = iter(X)
print(type(Y))
print(next(Y))
print(next(Y))
print(next(Y))

# 输出
<class 'list'>
<class 'list_iterator'>
1
2
3
```

从上述示例中我们可以看出两点：

- 通过`iter`函数把`list`转化成了迭代器
- 可迭代器能够记住遍历位置，能够通过next方法不断从前往后访问

除了Python内置的`iter`之外，还可以通过Python内置的工具包`itertools`创建迭代器，其中函数包括，

- count
- cycle
- repeat
- accumulate
- chain
- compress
- dropwhile
- islice
- product
- permutations
- combinations
- ......

`itertools`中包含很多用于创建迭代器的实用方法，如果感兴趣可以访问[官方文档](https://docs.python.org/3/library/itertools.html)进行详细了解。

当然，也可以自己通过实现`__iter__`和`__next__`方法来定义迭代器，

```python
class Iterator(object):
    def __init__(self, array):
        self.x = array
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.x):
            value = self.x[self.index]
            self.index += 1
        else:
            raise StopIteration
        return value
    
it = Iterator([1,2,3,4,5])
print(type(it))
for i in it:
    print(i)

# 输出
<class '__main__.Iterator'>
1
2
3
4
5
```

### 11.5.3 生成器

从文章开头的流程图可以直观的看出，生成器是迭代器的子集，换句话说，生成器一定是迭代器，但是迭代器不全是生成器对象。

提及生成器就不得不提及一个Python中的关键字`yiled`，在Python中一个函数可以用`yiled`替代`return`返回值，这样的话这个函数就变成了一个生成器对象，举个例子对比一下，

```python
def generator(array):
    for i in array:
        return i
    
gen = generator([1,2,3,4,5])
print(type(gen))

# 输出
<class 'int'>
```

这是我们常见的return返回方式，这样的话generator函数获取的是一个`int`型对象，下面看一下换成`yield`关键字，

```python
def generator(array):
    for i in array:
        yield(i)
        
gen = generator([1,2,3,4,5])
print(type(gen))

# 输出
<class 'generator'>
```

这样的话获取的是一个生成器`generator`，除了`yield`之外，在Python3.3之后还加入了`yield from`获取生成器，允许一个生成器将其部分操作委派给另一个生成器，使得生成器的用法变得更加简洁，`yield from`后面需要加上可迭代对象，这样可以把可迭代对象变成生成器，当然，这里的可迭代对象不仅包含列表、元组，还包含迭代器、生成器。`yield from`相对于`yield`的有几个主要优点：

- 代码更加简洁
- 可以用于生成器嵌套
- 易于异常处理

下面就从简洁代码方面举个例子说明一下，

```python
def generator(array):
    for sub_array in array:
        yield from sub_array

gen = generator([(1,2,3), (4,5,6,7)])

# 输出
1
2
3
4
5
6
7
```

当我们需要访问多层/多维可迭代对象时，我们就不需要逐层的去用`for ... in ...`去访问，可以简单的通过`yiled from`把生成器委派给子生成器，除此之外还可以通过`生成器表达式`的方法得到生成式，后面会介绍。

```python
print(next(gen))
print(next(gen))

# 输出
1
2
```

通过上面示例可以看出，生成器可以像迭代器那样使用`iter`和`next`方法。

读到这里可以会有疑惑，从这个示例看来生成器和迭代器并没有什么区别啊？为什么生成器还可以称得上是Python中的一大亮点？

首先它对比于迭代器在编码方面更加简洁，这是显而易见的，其次生成器运行速度更快，最后一点，也是需要着重说明的一点：节省内存。

也许在一些理论性实验、学术论文阶段可以不考虑这些工程化的问题，但是在公司做项目时，内存和资源占用是无法逃避的问题 。如果我们使用其他可迭代对象处理庞大的数据时，当创建或者返回值时会申请用于存储整个可迭代对象的内存，显然这是非常浪费的，因为有的元素当前我们用不到，也不会去访问，但它却一直占用这内存。这时候就体现了生成器的优点，它不是一次性把所有的结果都返回，而是当我们每读取一次，它会返回一个结果，当我们不读取时，它就是一个生成器表达式，几乎不占用内存。

### 11.5.4 生成器表达式

首先来看一个对比示例，

```python
X = [1, 2, 3, 4, 5]
it = [i for i in X]
gen = (i for i in X)
print(type(X))
print(type(it))
print(type(gen))

# 输出
<class 'list'>
<class 'list'>
<class 'generator'>
```

首先说一下`it = [i for i in X]`，这种用法叫做**列表生成式**，在很多编程规范中非常推崇的一种替代`for`循环的方式，仔细看一下代码会发现，`it = [i for i in X]`与`gen = (i for i in X)`的区别非常小，只是一个用了中括号，一个用了小括号，但是它们的区别缺失非常大的，使用中括号的叫做列表生成式，获得的返回值是一个列表，而使用小括号叫做生成器表达式，获得的返回结果是一个生成器，这也是前面提到的，除了使用`yield`和`yield from`两个关键字外还可以使用生成器表达式获得生成器。

## 11.6 应用场景

1. 集合的内部结构复杂，不想暴露对象的内部细节，只提供精简的访问方式。
2. 需要提供统一的访问接口，从而对不同的集合使用统一的算法。
3. 需要为一系列聚合对象提供多种不同的访问方式。

# 第十二章 组合模式

## 12.1 核心思想

将对象组合成树形结构以表示”整体-部分“的层次结构关系。组合使得用户对单个对象和复合对象的使用具有一致性。
组合模式使得用户对单个对象和组合对象的使用具有一致性，即使用组合对象就像使用一般对象一样，不用关心内部的组织结构。

比如在组装电脑的过程中，电脑由各个配件组成的，在组装之前，就是单个CPU、硬盘、显卡等配件，不能称为电脑，只有把它们按正确的方式组装在一起，配合操作系统才能正常运行。一般人使用电脑并不会关注内部的结构，只会关注一台整机。组装的电脑具有明显的部分与整体的关系，主板、电源等是电脑的一部分，而主板上又有CPU、硬盘、显卡，它们又是主板的一部分。像电脑一样，把对象组合成树形结构，以表示”部分-整体”的层次结构的程序设计模式就叫组合模式。
![组合模式_电脑组装](https://s2.loli.net/2022/04/05/UP653vm2NTe7Esk.jpg)

## 12.2 UML类图

![组合模式UML类图](https://s2.loli.net/2022/04/05/PwkVWL4o1gneYEi.jpg)

## 12.3 框架代码

```Python
from abc import ABC, abstractmethod


class Component(ABC):
    @staticmethod
    def addComponent():
        pass

    @staticmethod
    def removeComponent():
        pass

    @abstractmethod
    def show():
        pass


class Composite(Component):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._components = []

    def addComponent(self, component: Component):
        self._components.append(component)

    def removeComponent(self, component: Component):
        self._components.remove(component)

    def show(self, depth):
        print(f"{'-'*4*depth}{self.name}")
        for component in self._components:
            component.show(depth + 1)


class Leaf(Component):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def addComponent(self):
        pass

    def removeComponent(self):
        pass

    def show(self, depth):
        print(f"{'-'*4*depth}{self.name}")


if __name__ == "__main__":
    root = Composite("root")
    root.addComponent(Leaf("Leaf A"))
    comp = Composite("Composite X")
    comp.addComponent(Leaf("Leaf XA"))
    comp.addComponent(Leaf("Leaf XB"))
    comp2 = Composite("Composite XY")
    comp2.addComponent(Leaf("Leaf XYA"))
    comp2.addComponent(Leaf("Leaf XYB"))
    comp.addComponent(comp2)
    root.addComponent(comp)
    root.addComponent(Leaf("Leaf B"))
    leaf = Leaf("Leaf C")
    root.addComponent(leaf)
    root.removeComponent(leaf)
    root.show(0)
```

## 12.4 模型说明

### 12.4.1 设计要点

在设计组合模式时，要注意以下两点：

+ 理清部分与整体的关系，了解对象的组成结构。
+ 组合模式是一种具有层次关系的树形结构，不能再分的叶子节点是具体的组件，也就是最小的逻辑单元；具有子节点（由多个子组件组成）的组件称为复合组件，也就是组合对象。

### 12.4.2 优缺点

1. 优点

    + 调用简单，组合对象可以像一般对象一样使用，不用去区分，有统一的调用接口。

    + 组合对象可以自由地增加、删除组件，可灵活地组合不同的对象。


2. 缺点
    + 在一些层次结构太深的场景中，组合结构会变得太庞杂。

## 12.5 应用场景

1. 对象之间具有明显的部分整体”的关系时，或者具有层次关系时；
2. 组合对象与单个对象具有相同或类似行为（方法），用户希望统一地使用组合结构中的所有对象。

# 第十三章 构建模式

## 13.1 核心思想

将一复杂对象的构建过程和它的表现分离，使得同样的构建过程可以获取（创建）不同的表现。

建造者模式可以将一个产品的内部表象与产品的生成过程分割开来，从而可以使一个建造过程生成具有不同的内部表象的产品对象。如果我们用了建造者模式，那么用户就只需指定需要建造的类型就可以得到它们，而具体建造的过程和细节就不需知道了。比如一份炒粉，炒粉有一系列的制作流程，但是我们购买时并不需要知道是如何炒的，我们只需要报出自己的需求，是辣一点还是加肉或者鸡蛋等，就可以得到一份符合自己口味的炒粉了。

构建模式是一个产品或对象的生成器，强调产品的构建过程。

## 13.2 UML类图

![构建模式UML类图](https://s2.loli.net/2022/04/05/9zy36lYxguR5n4m.jpg)

## 13.3 框架代码

```python
from abc import ABC, abstractmethod


class Produt:
    def __init__(self, name, parts):
        self.name = name
        self._parts = parts

    def addPart(self, part):
        self._parts.append(part)

    def __str__(self) -> str:
        return f"产品{self.name}开始创建:\n"+"\n".join([f"add {part}" for part in self._parts])+f"\n产品{self.name}创建完成!"

class Builder(ABC):
    @abstractmethod
    def buildPartA(self):
        pass

    @abstractmethod
    def buildPartB(self):
        pass

    @abstractmethod
    def getResult(self):
        pass

class BuilderImplA(Builder):
    def __init__(self, product:Produt):
      self._product = product

    def buildPartA(self):
        self._product.addPart("part_A")

    def buildPartB(self):
        self._product.addPart("part_B")

    def getResult(self):
        return self._product


class BuilderImplB(Builder):
    def __init__(self, product:Produt):
      self._product = product

    def buildPartA(self):
        self._product.addPart("part_X")

    def buildPartB(self):
        self._product.addPart("part_Y")

    def getResult(self):
        return self._product

class Director:
    def __init__(self, builder:Builder) -> None:
        self._builder = builder

    def construct(self):
        self._builder.buildPartA()
        self._builder.buildPartB()

if __name__ == "__main__":
    b1 = BuilderImplA(Produt("A",[]))
    b2 = BuilderImplB(Produt("B",[]))
    Director(b1).construct()
    Director(b2).construct()
    print(b1.getResult())
    print()
    print(b2.getResult())
```

## 13.4 模型说明

### 13.4.1 设计要点

构建模式中主要有三个角色，在设计构建模式时要找到并区分这些角色。

+ 产品（Product）：即你要构建的对象；
+ 构建者（Builder）：构建模式的核心类，负责产品的构建过程；
+ 指挥者（Director）：构建的管理类，负责管理每一种产品的创建数量和创建顺序。

### 13.4.2 优缺点

+ 优点
    1. 将产品（对象）的创建过程与产品（对象）本身分离开来，让使用方（调用者）可以用相同的创建过程创建不同的产品（对象）。
    2. 将对象的创建过程单独分解出来，使得创建过程更加清晰，能够更加精确地控制复杂对象的创建过程。
    3. 每一个具体构建者都相对独立，而与其他的具体构建者无关，因此可以很方便地替换具体构建者或增加新的具体构建者。
+ 缺点：
    1. 增加了很多创建类，如果产品的类型和种类比较多，将会增加很多类，使整个系统变得更加庞杂。
    2. 产品之间的结构相差很大时，构建模式将很难适应。

## 13.5 应用场景

1. 产品（对象）的创建过程比较复杂，希望将产品的创建过程和它本身的功能分离开来。
2. 产品有很多种类，每个种类之间内部结构比较类似，但有很多差异；不同的创建顺序或不同的组合方式，将创建不同的产品。

# 第十四章 适配模式

## 14.1 核心思想

将一个类的接口变成客户端所期望的另一种接口，从而使原本因接口不匹配而无法一起工作的两个类能够在一起工作。

简单地说，就是需要的东西就在面前，但却不能使用，而短时间又无法改造它，于是我们就想办法适配它。换句话说，我们想使用的库可以实现我们的目标，但是调用时不符合我们的规范，所以需要一个适配器，再次开发，写出符合我们规范的接口，方便调用。

适配模式的作用：

1. 接口转换，将原有的接口（或方法）转换成另一种接口。
2. 用新的接口包装一个已有的类。
3. 匹配一个老的组件到一个新的接口。

适配模式又叫变压器模式，也叫包装模式（Wrapper），它的核心思想是：将一个对象经过包装或转换后使它符合指定的接口，使得调用方可以像使用接口的一般对象一样使用它。这一思想在生活中可谓处处可见，除了故事剧情中的插座转换器，具有电压转换功能的变压器插座也有类似的功能，它能让你像使用国标（220V）电器一样使用美标（110V）电器；还有就是各种转接头，如MiniDP转HDMI接头、HDMI转VGA线转换器、MicroUSB转TypeC接头等。

当年，魏文王问名医扁鹊说：“你们家兄弟三人，都精于医术，到底哪一位最好呢？”扁鹊答：“长兄最好，中兄次之，我最差。”文王再问：“那么为什么你最出名呢？”扁鹊答：“长兄治病，是治病于病情发作之前。由于一般人不知道他事先能铲除病因，所以他的名气无法传出去；中兄治病，是治病于病情初起时。一般人以为他只能治轻微的小病，所以他的名气只及本乡里。而我是治病于病情严重之时。一般人都看到我在经脉上穿针管放血、在皮肤上敷药等大手术，所以大家都以为我的医术高明，名气因此响遍全国。”

如果能事先预防接口不同的问题，不匹配问题就不会发生；在有小的接口不统一问题发生时，及时重构，问题不至于扩大；只有碰到无法改变原有设计和代码的情况时，才考虑适配。事后控制不如事中控制，事中控制不如事前控制。

适配器模式当然是好模式，但如果无视它的应用场合而盲目使用，其实是本末倒置了。

## 14.2 UML类图

![适配模式UML类图](https://s2.loli.net/2022/04/05/uvIedT7Nwn9hgcC.jpg)

## 14.3 框架代码

```python
from abc import ABC, abstractmethod
import sys

class Target(ABC):
    @abstractmethod
    def request(self):
        pass

class Adaptee():
    def specificRequest(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Adaptor(Target):
    def __init__(self):
      self._adaptee = Adaptee()
    def request(self):
        self._adaptee.specificRequest()

if __name__ == "__main__":
    target = Adaptor()
    # 对客户端来说，调用的就是Target rewuest函数
    target.request()
```

## 14.4 模型说明

### 14.4.1 设计要点

适配模式中主要有三个角色，在设计适配模式时要找到并区分这些角色。

1. 目标（Target）：即你期望的目标接口，要转换成的接口。
2. 源对象（Adaptee）：即要被转换的角色，要把谁转换成目标角色。
3. 适配器（Adapter）：适配模式的核心角色，负责把源对象转换和包装成目标对象。

### 14.4.2 优缺点

+ 优点
    1. 可以让两个没有关联的类一起运行，起中间转换的作用。
    2. 提高了类的复用率。
    3. 灵活性好，不会破坏原有系统。
+ 缺点：
    1. 如果原有系统没有设计好（如Target不是抽象类或接口，而是一个实体类），适配模式将很难实现。
    2. 过多地使用适配器，容易使代码结构混乱，如明明看到调用的是A接口，内部调用的却是B接口的实现。

## 14.5 应用场景

1. 系统需要使用现有的类，而这些类的接口不符合现有系统的要求。
2. 对已有的系统拓展新功能，尤其适用于在设计良好的系统框架下增加接入第三方的接口或第三方的SDK。

# 第十五章 策略模式

## 15.1 核心思想

定义一系列算法，将每个算法都封装起来，并且使它们之间可以相互替换。策略模式使算法可以独立于使用它的用户而变化。

比如在生活中，将不同的出行方式（采用的交通工具）理解成一种出行算法，将这些算法抽象出一个基类IVehicle，并定义一系列算法：共享单车（SharedBicycle）、快速公交（ExpressBus）、地铁（Subway）、快车（Express）......。我们可以选择任意一种（实际场景中肯定会选择最合适的）出行方式，并且可以方便地更换出行方式。

策略模式的核心思想：对算法、规则进行封装，使得替换算法和新增算法更加灵活。

## 15.2 UML类图

![策略模式UML类图](https://s2.loli.net/2022/04/05/mY47XM2oNFAfWv1.jpg)

## 15.3 框架代码

```Python
from abc import ABC,abstractmethod
import sys

class Strategy(ABC):
    @abstractmethod
    def algorithmInterface(self):
        pass
    
class StrategyImplA(Strategy):
    def algorithmInterface(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        
class StrategyImplB(Strategy):
    def algorithmInterface(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        
class StrategyImplC(Strategy):
    def algorithmInterface(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")
        
class Context:
    def __init__(self,strategy:Strategy): # 初始化时，传入具体的策略对象
        self.strategy=strategy
    def contextInterface(self): # 根据具体的策略对象，调用其算法的方法
        self.strategy.algorithmInterface()
    
if __name__ == "__main__":
    context=Context(StrategyImplA())
    context.contextInterface()
    
    context=Context(StrategyImplB())
    context.contextInterface()
    
    context=Context(StrategyImplC())
    context.contextInterface()
```

## 15.4 模型说明

### 15.4.1 设计要点

策略模式中主要有三个角色，在设计策略模式时要找到并区分这些角色。

1. 上下文环境（Context）：起着承上启下的封装作用，屏蔽上层应用对策略（算法）的直接访问，封装可能存在的变化。
2. 策略的抽象（Strategy）：策略（算法）的抽象类，定义统一的接口，规定每个子类必须实现的方法。
3. 具备的策略：策略的具体实现者，可以有多个不同的（算法或规则）实现。

### 15.4.2 优缺点

1. 优点
    + 算法（规则）可自由切换。
    + 避免使用多重条件判断。
    + 方便拓展和增加新的算法（规则）。
2. 缺点：所有策略类都需要对外暴露。

## 15.5 应用场景

1. 如果一个系统里面有许多类，它们之间的区别仅在于有不同的行为，那么可以使用策略模式动态地让一个对象在许多行为中选择一种；
2. 一个系统需要动态地在几种算法中选择一种；
3. 设计程序接口时希望部分内部实现由调用方自己实现；
4. 策略模式是一种定义一系列算法的方法，从概念上来看，所有这些算法完成的都是相同的工作，只是实现不同，它可以以相同的方式调用所有的算法，减少了各种算法类与使用算法类之间的耦合；

# 第十六章 简单工厂模式

## 16.1 核心思想

专门定义一个类来负责创建其他类的实例，根据参数的不同创建不同类的实例，被创建的实例通常具有共同的父类，这个模式叫简单工厂模式（SimpleFactoryPattern）。在工厂模式中，用来创建对象的类叫工厂类，被创建的对象的类称为产品类。

只有一个工厂类SimpleFactory，类中有一个静态的创建方法createProduct，该方法根据参数传递过来的类型值（type）或名称（name）来创建具体的产品（子类）对象。

![简单工厂模式示意图](https://s2.loli.net/2022/04/05/XUGh2mVJDWTNrud.jpg)

## 16.2 UML类图

![简单工厂模式UML类图](https://s2.loli.net/2022/04/05/m4EU13veNJnP7bC.jpg)

## 16.3 框架代码

```python
from abc import ABC, abstractmethod
import sys

class Product(ABC):
    @abstractmethod
    def feature(self):
        pass

class SimpleFactory:
    @staticmethod
    def createProduct(name:str)->Product:
        if name == "A":
            product = ProductImplA()
        elif name == "B":
            product = ProductImplB()
        else:
            raise ValueError(f"parameter name: {name} is not supported.")
        return product

class ProductImplA(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductImplB(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

if __name__ == "__main__":
    SimpleFactory.createProduct("A").feature()
    SimpleFactory.createProduct("B").feature()
    SimpleFactory.createProduct("C").feature()
```

## 16.4 模型说明

### 16.4.1 设计要点

简单工厂模式中有两个要点：

1. SimpleFactory工厂类，里面必须有返回Product对象的函数createProduct，该函数以参数的类型或者名字来决定返回哪个Product；
2. Product是产品基类，定义了产品共有的属性和方法；

### 16.4.2 优缺点

1. 优点：
    + 实现简单、结构清晰。
    + 抽象出一个专门的类来负责某类对象的创建，分割出创建的职责，不能直接创建具体的对象，只需传入适当的参数即可。
    + 使用者可以不关注具体对象的类名称，只需知道传入什么参数可以创建哪些需要的对象。
    + 工厂类中包含了必要的逻辑判断，根据客户端的选择条件动态实例化相关的类，对于客户端来说，去除了与具体产品的依赖
2. 缺点：
    + 不易拓展，一旦添加新的产品类型，就不得不修改工厂的创建逻辑。不符合“开放封闭”原则，如果要增加或删除一个产品类型，就要修改switch...case...（或if...else...）的判断代码。
    + 当产品类型较多时，工厂的创建逻辑可能过于复杂，switch...case...（或if...else...）判断会变得非常多。一旦出错可能造成所有产品创建失败，不利于系统的维护。

## 16.5 应用场景

1. 产品具有明显的继承关系，且产品的类型不太多。
2. 所有的产品具有相同的方法和类似的属性，使用者不关心具体的类型，只希望传入合适的参数能返回合适的对象。

# 第十七章 工厂方法模式

## 17.1 核心思想

工厂方法模式是简单工厂模式的一个升级版本，为解决简单工厂模式不符合“开放封闭”原则（对扩展开放，对修改封闭）的问题，我们对SimpleFactory进行了一个拆分，抽象出一个父类Factory，并增加多个子类分别负责创建不同的具体产品。

定义一个创建对象（实例化对象）的接口，让子类来决定创建哪个类的实例。工厂方法使一个类的实例化延迟到其子类。

## 17.2 UML类图

![工厂方法模式UML类图](https://s2.loli.net/2022/04/06/K7sNpnc1ztjfu9S.jpg)

## 17.3 框架代码

```python
from abc import ABC, abstractmethod
import sys

class Product(ABC):
    @abstractmethod
    def feature(self):
        pass

class ProductImplA(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductImplB(Product):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Factory(ABC):
    @abstractmethod
    def createProduct(self):
        pass

class ProductAFactory(Factory):
    def createProduct(self)->ProductImplA:
        return ProductImplA()

class ProductBFactory(Factory):
    def createProduct(self)->ProductImplB:
        return ProductImplB()

if __name__ == "__main__":
    ProductAFactory().createProduct().feature()
    ProductBFactory().createProduct().feature()
```

## 17.4 模型说明

### 17.4.1 设计要点

工厂方法模式中有两个要点：

1. 子工厂类继承于Factory，每个子工厂类调用createProduct函数返回对应的具体产品类；
2. 具体的产品类型继承于Product基类；

### 17.4.2 优缺点

1. 优点
    + 解决了简单工厂模式不符合“开放封闭”原则的问题，使程序更容易拓展。
    + 实现简单。
2. 缺点
    + 对于有多种分类的产品，或具有二级分类的产品，工厂方法模式并不适用。**多种分类**：如我们有一个电子白板程序，可以绘制各种图形，那么画笔的绘制功能可以理解为一个工厂，而图形可以理解为一种产品；图形可以根据形状分为直线、矩形、椭圆等，也可以根据颜色分为红色图形、绿色图形、蓝色图形等。**二级分类**：如一个家电工厂，它可能同时生产冰箱、空调和洗衣机，那么冰箱、空调、洗衣机属于一级分类；而洗衣机又可分为高效型的和节能型的，高效型洗衣机和节能型洗衣机就属于二级分类。

## 17.5 应用场景

1. 客户端不知道它所需要的对象的类。
2. 工厂类希望通过其子类来决定创建哪个具体类的对象。

# 第十八章 抽象工厂模式

## 18.1 核心思想

提供一个创建一系列相关或相互依赖的对象的接口，而无须指定它们的具体类。

抽象工厂模式适用于有多个系列且每个系列有相同子分类的产品。

比如，为了适应不同数据库管理系统的需求。这时，需要考虑到使用sql server和access数据库管理系统。不同的数据库就是多个系列。数据库中不同的表，对应着相同子分类的产品。

## 18.2 UML类图

![抽象工厂模式UML类图](https://s2.loli.net/2022/04/06/AeDFiW7M3PhHox1.jpg)

## 18.3 框架代码

```python
from abc import ABC, abstractmethod
import sys

class ProductA(ABC):
    @abstractmethod
    def feature(self):
        pass

class ProductAImplA(ProductA):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductAImplB(ProductA):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")


class ProductB(ABC):
    @abstractmethod
    def feature(self):
        pass

class ProductBImplA(ProductB):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ProductBImplB(ProductB):
    def feature(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class AbstractFactory(ABC):
    @abstractmethod
    def createProductA(self):
        pass

    @abstractmethod
    def createProductB(self):
        pass

class FactoryImplA(AbstractFactory):
    def createProductA(self)->ProductA:
        return ProductAImplA()

    def createProductB(self)->ProductB:
        return ProductAImplB()

class FactoryImplB(AbstractFactory):
    def createProductA(self)->ProductA:
        return ProductBImplA()

    def createProductB(self)->ProductB:
        return ProductBImplB()

if __name__ == "__main__":
    # 采用反射的机制，避免了需要换工厂时需要全部修改使用的工厂类，在反射机制中，只需要修改classPath变量即可
    from importlib import import_module
    classPath = "abstract_factory_pattern.FactoryImplA"
    index = classPath.rfind(".")
    modulePath,className = classPath[:index],classPath[index+1:]
    factory:FactoryImplA = getattr(import_module("abstract_factory_pattern"),className)()
    pa = factory.createProductA()
    pb = factory.createProductB()
    pa.feature()
    pb.feature()
```

## 18.4 模型说明

### 18.4.1 设计要点

抽象工厂方法模式中有两个要点：

1. 抽象工厂类里面应包含所有产品创建的抽象方法，且其子类具体工厂，实现产品创建的抽象方法，返回对应的产品对象；
2. 不同的产品有不同的产品基类，具体的产品类型继承于产品基类；

### 18.4.2 优缺点

1. 优点
    + 解决了具有二级分类的产品的创建。
    + 易于交换产品系列，抽象工厂模式只需要改变具体工厂即可使用不同的产品配置。
    + 让具体的创建实例过程与客户端分离，客户端是通过它们的抽象接口操纵实例，产品的具体类名也被具体工厂的实现分离，不会出现在客户代码中
2. 缺点
    + 如果产品的分类超过二级，如三级甚至更多级，抽象工厂模式将会变得非常臃肿。
    + 不能解决产品有多种分类、多种组合的问题。

## 18.5 应用场景

1. 系统中有多于一个的产品族，而每次只使用其中某一产品族。
2. 产品等级结构稳定，设计完成之后，不会向系统中增加新的产品等级结构或者删除已有的产品等级结构。

# 第十九章 命令模式

## 19.1 核心思想

将一个请求封装成一个对象，从而让你使用不同的请求把客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能。

在餐馆中点餐，我们只要发一个订单就能吃到我们想要的那种加工方式的美味佳肴，而不用知道厨师是谁，更不用关心他是怎么做的。像点餐的订单一样，发送者（客户）与接收者（厨师）没有任何依赖关系，我们只要发送订单就能完成想要完成的任务。

命令模式的最大特点是将具体的命令与对应的接收者相关联（捆绑），使得调用方不用关心具体的行动执行者及如何执行，只要发送正确的命令，就能准确无误地完成相应的任务。

## 19.2 UML类图

![命令模式UML类图](https://s2.loli.net/2022/04/06/cQ1mBNAUMJpai7x.jpg)

## 19.3 框架代码

```python
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
```

## 19.4 模型说明

### 19.4.1 设计要点

命令模式中主要有四个角色，在设计命令模式时要找到并区分这些角色。

1. 命令（Command）：要完成的任务，或要执行的动作，这是命令模式的核心角色。
2. 接收者（Receiver）：任务的具体实施方，或行动的真实执行者。
3. 调度者（Invoker）：接收任务并发送命令，对接用户的需求并执行内部的命令，负责外部用户与内部命令的交互。
4. 用户（Client）：命令的使用者，即真正的用户。

### 19.4.2 优缺点

1. 优点
    + 对命令的发送者与接收者进行解耦，使得调用方不用关心具体的行动执行者及如何执行，只要发送正确的命令即可。
    + 可以很方便地增加新的命令。
2. 缺点
    + 在一些系统中可能会有很多命令，而每一个命令都需要一个具体的类去封装，容易使命令的类急剧膨胀。

## 19.5 应用场景

1. 你希望系统发送一个命令（或信号），任务就能得到处理时。如GUI中的各种按钮的点击命令，再如自定义一套消息的响应机制。
2. 需要将请求调用者和请求接收者解耦，使得调用者和接收者不直接交互时。
3. 需要将一系列的命令组合成一组操作时，可以使用宏命令的方式。

# 第二十章 备忘录模式

## 20.1 核心思想

在不破坏内部结构的前提下捕获一个对象的内部状态，这样便可在以后将该对象恢复到原先保存的状态。

备忘模式的最大功能就是备份，可以保存对象的一个状态作为备份，这样便可让对象在将来的某一时刻恢复到之前保存的状态。

如游戏中死了的英雄可以满血复活，很多电器（如电视、冰箱）都有恢复出厂设置功能；再如很多虚拟机管理软件（如VMware）都可以保存快照，这样在操作系统出现问题时可以快速地恢复到保存的某个点。

## 20.2 UML类图

![备忘录模式UML类图](https://gitee.com/WenqingNie/picgo/raw/master/images/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F-%E5%A4%87%E5%BF%98%E5%BD%95%E6%A8%A1%E5%BC%8FUML%E7%B1%BB%E5%9B%BE-2022-03-24-08-19-24-32042e2b455c0cca7bcc830ed8e5c237-ddf835.jpg)

## 20.3 框架代码

```python
from abc import ABC,abstractmethod

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
```



## 20.4 模型说明

### 20.4.1 设计要点

备忘模式中主要有三个角色，在设计备忘模式时要找到并区分这些角色。

1. 发起人（Originator）：需要进行备份的对象。
2. 备忘录（Memento）：备份的状态，即一个备份的存档。
3. 备忘录管理者（Caretaker）：备份存档的管理者，由它负责与发起人的交互。

### 20.4.2 优缺点

1. 优点
    + 提供了一种可以恢复状态的机制，使得用户能够比较方便地回到某个历史状态。
    + 实现了信息的封装，用户不需要关心状态的保存细节。
2. 缺点
    + 如果类的成员变量过多，势必会占用比较多的资源，而且每一次保存都会消耗一定的内存。此时可以限制保存的次数。

## 20.5 应用场景

1. 需要保存/恢复对象的状态或数据时，如游戏的存档、虚拟机的快照。
2. 需要实现撤销、恢复功能的场景，如Word中的Ctrl+Z、Ctrl+Y功能，DOS命令行或Linux终端的命令记忆功能。
3. 提供一个可回滚的操作，如数据库的事务管理。

# 第二十一章 享元模式

## 21.1 核心思想

运用共享技术有效地支持大量细粒度对象的复用。享元模式以共享的方式高效地支持大量的细粒度对象，享元对象能做到共享的关键是区分内部状态和外部状态。

+ 内部状态（intrinsicState）是存储在享元对象内部并且不会随环境改变而改变的状态，因此内部状态是可以共享的状态。

+ 外部状态（extrinsicState）是随环境改变而改变的、不可以共享的状态。享元对象的外部状态必须由客户端保存，并在享元对象被创建之后，在需要使用的时候再传入享元对象内部。

比如游戏中，围棋和五子棋，它们有很多棋子，但是可以使用享元模式，只创建一个棋子的对象。棋子的颜色只有黑白两种，所以颜色应该是棋子的内部状态，而各个棋子之间的差别主要就是位置的不同，所以方位坐标应该是棋子的外部状态。

## 21.2 UML类图

![享元模式UML类图](https://gitee.com/WenqingNie/picgo/raw/master/images/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F-%E4%BA%AB%E5%85%83%E6%A8%A1%E5%BC%8FUML%E7%B1%BB%E5%9B%BE-2022-03-24-23-03-41-9105fdeb19cf60ff9796bc14afc5815c-a8e55c.jpg)

## 21.3 框架代码

```python
from abc import ABC, abstractmethod

class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    def __init__(self,intrinsicState) -> None:
        self._intrinsicState = intrinsicState

    def operation(self, extrinsicState):
        print(f"{self.__class__.__name__}\tintrinsicState:{self._intrinsicState}\textrinsicState:{extrinsicState}")

class FlyweightFactory:
    def __init__(self) -> None:
        self._flyweights  = {}

    def getFlyweight(self,key):
        flyweight = self._flyweights.get(key,None)
        if flyweight is None:
            flyweight = FlyweightImpl(key)
        return flyweight

class UnsharedFlyweightImpl(Flyweight):
    def operation(self, extrinsicState):
        print(f"{self.__class__.__name__}\textrinsicState:{extrinsicState}")

if __name__ == "__main__":
    flyweightFactory = FlyweightFactory()

    flyweightA=flyweightFactory.getFlyweight("intrinsicStateA")
    flyweightA.operation("extrinsicStateA")

    flyweightB=flyweightFactory.getFlyweight("intrinsicStateB")
    flyweightB.operation("extrinsicStateB")

    flyweightC=UnsharedFlyweightImpl()
    flyweightC.operation("extrinsicStateC")
```

## 21.4 模型说明

### 21.4.1 设计要点

享元模式的实现非常简单，在设计享元模式的程序时要注意两个主要角色和四个设计要点。

**两个主要角色：**

1. 享元对象（Flyweight）：即你期望用来共享的对象，享元对象必须是轻量级对象，也就是细粒度对象。
2. 享元工厂（FlyweightFactory）：享元模式的核心角色，负责创建和管理享元对象。享元工厂提供一个用于存储享元对象的享元池，用户需要对象时，首先从享元池中获取，如果享元池中不存在，则创建一个新的享元对象返回给用户，并在享元池中保存该新增对象。享元工厂其实是一个修改版本的简单工厂模式

**四个设计要点：**

1. 享元对象必须是轻量级、细粒度的对象。
2. 区分享元对象的内部状态和外部状态。
3. 享元对象的内部状态和属性一经创建不会被随意改变。因为如果可以改变，则A取得这个对象obj后，改变了其状态，B再去取这个对象obj时就已经不是原来的状态了。
4. 使用对象时通过享元工厂获取，使得传入相同的key时获得相同的对象。

### 21.4.2 优缺点

1. 优点：
    + 可以极大减少内存中对象的数量，使得相同对象或相似对象（内部状态相同的对象）在内存中只保存一份。
    + 享元模式的外部状态相对独立，而且不会影响其内部状态，从而使得享元对象可以在不同的环境中被共享。
2. 缺点：
    + 享元模式使得系统更加复杂，需要分离出内部状态和外部状态，这使得程序的逻辑复杂化。
    + 享元对象的内部状态一经创建不能被随意改变。要解决这个问题，需要使用对象池机制。

## 21.5 应用场景

1. 如果一个应用程序使用了大量的对象，而大量的这些对象造成了很大的存储开销时就应该考虑使用；
2. 对象的大多数状态可以外部状态，如果删除对象的外部状态，那么可以用相对较少的共享对象取代很多组对象，此时可以考虑使用享元模式。

# 第二十二章 访问模式

## 22.1 核心思想

封装一些作用于某种数据结构中各元素的操作，它可以在不改变数据结构的前提下定义作用于这些元素的新的操作。

## 22.2 UML类图

![访问者模式UML类图](https://s2.loli.net/2022/03/25/k4DjiUSGX6Hy1EN.jpg)

## 22.3 框架代码

```python
from abc import ABC,abstractmethod

class Visitor:
    @abstractmethod
    def visitElementImplA(self,element):
        pass

    @abstractmethod
    def visitElementImplB(self,element):
        pass

class VisitorImplA(Visitor):
    def visitElementImplA(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

    def visitElementImplB(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

class VisitorImplB(Visitor):
    def visitElementImplA(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

    def visitElementImplB(self, element):
        print(f"{element.__class__.__name__}被{self.__class__.__name__}访问。。。")

class Element(ABC):
    @abstractmethod
    def accept(self, visitor:Visitor):
        pass

class ElementImplA(Element):
    def accept(self, visitor: Visitor):
        visitor.visitElementImplA(self)

class ElementImplB(Element):
    def accept(self, visitor: Visitor):
        visitor.visitElementImplB(self)

class ObjectStructure:
    def __init__(self, elements=[]) -> None:
        self._elements = elements

    def addElement(self,element:Element):
        self._elements.append(element)

    def removeElement(self, element:Element):
        self._elements.remove(element)

    def accept(self, visitor: Visitor):
        for element in self._elements:
            element.accept(visitor)


if __name__ == "__main__":
    objectStructure = ObjectStructure([])

    objectStructure.addElement(ElementImplA())
    objectStructure.addElement(ElementImplB())

    visitorA = VisitorImplA()
    visitorB = VisitorImplB()

    objectStructure.accept(visitorA)
    objectStructure.accept(visitorB)
```



## 22.4 模型说明

### 22.4.1 设计要点

访问模式中主要有三个角色，在设计访问模式时要找到并区分这些角色。

1. 访问者（Visitor）：负责对数据节点进行访问和操作。
2. 元素（Element）：即要被操作的数据对象，一般种类是固定不变的。
3. 对象结构（ObjectStructure）：数据结构的管理类，也是数据对象的一个容器，可遍历容器内的所有元素。

### 22.4.2 优缺点

1. 优点
    + 将数据和操作（算法）分离，降低了耦合度。将有关元素对象的访问行为集中到一个访问者对象中，而不是分散在一个个的元素类中，类的职责更加清晰。
    + 增加新的访问操作很方便。使用访问模式，增加新的访问操作就意味着增加一个新的具体访问者类，实现简单，无须修改源代码，符合“开闭原则”。
    + 让用户能够在不修改现有元素类层次结构的情况下，定义作用于该层次结构的操作。
2. 缺点
    + 增加新的元素类很困难。在访问模式中，每增加一个新的元素类都意味着要在抽象访问者角色中增加一个新的抽象操作，并在每一个具体访问者类中增加相应的具体操作，这违背了“开闭原则”的要求。
    + 破坏数据对象的封装性。访问模式要求访问者对象能够访问并调用每一个元素的操作细节，这意味着元素对象有时候必须暴露一些自己的内部操作和内部状态，否则无法供访问者访问。

## 22.5 应用场景

1. 对象结构中包含的对象类型比较少，而且这些类需求比较固定，很少改变，但经常需要在此对象结构上定义新的操作。
2. 一个对象结构包含多个类型的对象，希望对这些对象实施一些依赖其具体类型的操作。在访问模式中针对每一种具体的类型都提供了一个访问操作，不同类型的对象可以有不同的访问操作。
3. 需要对一个对象结构中的对象进行很多不同的并且不相关的操作，需要避免让这些操作“污染”这些对象的类，也不希望在增加新操作时修改这些类。访问模式使得我们可以将相关的访问操作集中起来定义在访问者类中，对象结构可以被多个不同的访问者类所使用，将对象本身与对象的访问操作分离。

# 第二十三章 模板模式

## 23.1 核心思想

定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

## 23.2 UML类图

![模板模式UML类图](https://s2.loli.net/2022/03/26/mKkcvonwVs5rC9Z.jpg)

## 23.3 框架代码

```python
from abc import ABC,abstractmethod
import sys

class Template(ABC):
    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    def templateMethod(self):
        self.stepOne()
        self.stepTwo()

class TemplateImplA(Template):
    def stepOne(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

    def stepTwo(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class TemplateImplB(Template):
    def stepOne(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

    def stepTwo(self):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

if __name__ == "__main__":
    a = TemplateImplA()
    a.templateMethod()
    print()
    b = TemplateImplB()
    b.templateMethod()
```



## 23.4 模型说明

### 23.4.1 设计要点

两个重要的组成部分：

1. 抽象模板类（Template）：把不变的行为、方法和属性移到父类中，去除子类中的重复代码来体现它的优势；
2. 模板类具体子类（TemplateImpl）：子类实现模板父类的某些细节，满足个性化的需求；

### 23.4.2 优缺点

1. 优点
    + 模板方法模式是通过把不变的行为挪到一个统一的父类，从而达到去除子类中重复代码的目的。
    + 子类实现模板父类的某些细节，有助于模板父类的扩展。
    + 通过一个父类调用子类实现的操作，通过子类扩展增加新的行为，符合“开放-封闭原则”。
2. 缺点
    + 每一个不同的实现都需要一个子类来实现，导致类的个数增加，使得系统更加庞大。

## 23.5 应用场景

1. 对一些复杂的算法进行分割，将其算法中固定不变的部分设计为模板方法和父类具体方法，而一些可以改变的细节由其子类来实现。即一次性实现一个算法的不变部分，并将可变的行为留给子类来实现。
2. 各子类中公共的行为应被提取出来并集中到一个公共父类中以避免代码重复。
3. 需要通过子类来决定父类算法中某个步骤是否执行，实现子类对父类的反向控制。

# 第二十四章 桥接模式

## 24.1 核心思想

将抽象和实现解耦，使得它们可以独立地变化。

抽象与它的实现分离，这并不是说，让抽象类与其派生类分离，因为这没有任何意义。实现指的是抽象类和它的派生类用来实现自己的对象。

实现系统可能有多角度分类，每一种分类都有可能变化，那么就把这种多角度分离出来让它们独立变化，减少它们之间的耦合。桥梁模式关注的是抽象和实现的分离，使得它们可以独立地发展。

## 24.2 UML类图

![桥接模式UML类图](https://s2.loli.net/2022/03/28/8UAKEx4i7eY5QHF.jpg)

## 24.3 框架代码

```python
from abc import ABC, abstractmethod
import sys

class Implementor(ABC):
    @abstractmethod
    def operationImpl(self):
        pass

class ImplementorImplA(Implementor):
    def operationImpl(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class ImplementorImplB(Implementor):
    def operationImpl(self):
        print(
            f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Abstraction(ABC):
    def __init__(self) -> None:
        self.implementor = None

    def setImplementor(self, implementor:Implementor):
        self.implementor = implementor

    @abstractmethod
    def operation(self):
        pass

class RefinedAbstraction(Abstraction):
    def operation(self):
        self.implementor.operationImpl()

if __name__ == "__main__":
    ra = RefinedAbstraction()
    ra.setImplementor(ImplementorImplA())
    ra.operation()
    ra.setImplementor(ImplementorImplB())
    ra.operation()
```



## 24.4 模型说明

### 24.4.1 设计要点

两个重要的角色

1. Abstraction（抽象化角色）：与Implementor组合关系，里面提供了与Implementor相关的功能扩展；
2. Implementor（实现化角色）：实现化角色，定义了属性和功能；

### 24.4.2 优缺点

1. 优点
    + 分离抽象接口及其实现部分。
    + 桥接模式有时类似于多继承方案，但是多继承方案违背了类的单一职责原则（即一个类只有一个变化的原因），复用性比较差，而且多继承结构中类的个数非常庞大，桥接模式是比多继承方案更好的解决方法。
    +  桥接模式提高了系统的可扩充性，在两个变化维度中任意扩展一个维度，都不需要修改原有系统。
    + 实现细节对客户隐藏，可以对用户隐藏实现细节。

2. 缺点
    + 桥接模式的引入会增加系统的理解与设计难度，由于聚合关联关系建立在抽象层，要求开发者针对抽象进行设计与编程。
    + 桥接模式要求正确识别出系统中两个独立变化的维度，因此其使用范围具有一定的局限性。

## 24.5 应用场景

1. 如果一个系统需要在构件的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的继承联系，通过桥接模式可以使它们在抽象层建立一个关联关系。
2. 抽象化角色和实现化角色可以以继承的方式独立扩展而互不影响，在程序运行时可以动态将一个抽象化子类的对象和一个实现化子类的对象进行组合，即系统需要对抽象化角色和实现化角色进行动态耦合。
3. 一个类存在两个独立变化的维度，且这两个维度都需要进行扩展。
4. 虽然在系统中使用继承是没有问题的，但是由于抽象化角色和具体化角色需要独立变化，设计要求需要独立管理这两者。
5. 对于那些不希望使用继承或因为多层次继承导致系统类的个数急剧增加的系统，桥接模式尤为适用。

# 第二十五章 解释器模式

## 25.1 核心思想

解释器模式用于描述如何使用面向对象语言构建一个简单的语言解释器。在某些情况下，为了更好地描述某些特定类型的问题，我们可以创建一种新的语言，这种语言拥有自己的表达式和结构，即文法规则，这些问题的实例将对应为该语言中的句子。如在金融业务中，经常需要定义一些模型运算来统计、分析大量的金融数据，从而窥探一些商业发展趋势。

定义一个语言，定义它的文法的一种表示；并定义一个解释器，该解释器使用该文法来解释语言中的句子。

解释器模式需要解决的是，如果一种特定类型的问题发生的频率足够高，那么可能就值得将该问题的各个实例表述为一个简单语言中的句子。这样就可以构建一个解释器，该解释器通过解释这些句子来解决该问题。比方说，我们常常会在字符串中搜索匹配的字符或判断一个字符串是否符合我们规定的格式，这种技术就是正则表达式。

## 25.2 UML类图

![解释器模式UML类图](https://s2.loli.net/2022/03/31/PLlHnaMszT8Ffmd.jpg)

## 25.3 框架代码

```python
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
```



## 25.4 模型说明

### 25.4.1 设计要点

所谓解释器模式就是给定一门语言，定义它的文法的一种表示，并定义一个解释器，该解释器使用该表示来解释语言中的句子。解释器模式的角色划分：

1. 抽象表达式角色（AbstractExpression）：该角色声明一个所有的具体表达式角色都需要实现的抽象接口，该接口主要是一个解释操作interpert()方法。
2. 终结符表达式角色（TerminalExpression）：该角色实现了抽象表达式角色所要求的接口，文法中的每一个终结符都有一个具体终结表达式与之对应。
3. 非终结符表达式角色（Nonterminal Expression）：该角色是一个具体角色，文法中的每一条规则都对应一个非终结符表达式类。
4. 环境角色（Context）：该角色提供解释器之外的一些全局信息。
5. 客户端角色（Client）：该角色创建一个抽象语法树，调用解释操作。

### 25.4.2 优缺点

1. 优点
    + 可扩展性比较好，灵活。
    + 增加了新的解释表达式的方式。
    + 易于实现简单文法。

2. 缺点
    + 需要建大量的类，因为每一种语法都要建一个非终结符的类。
    + 解释的时候采用递归调用方法，导致有时候函数的深度会很深，影响效率。

## 25.5 应用场景

1. 可以将一个需要解释执行的语言中的句子表示为一个抽象语法树。
2. 一些重复出现的问题可以用一种简单的语言来进行表达。
3. 一个简单语法需要解释的场景。

# 第二十六章 过滤器模式

## 26.1 核心思想

过滤器模式就是根据某种规则，从一组对象中，过滤掉一些不符合要求的对象的过程。

## 26.2 UML类图

![过滤器模式UML类图](https://s2.loli.net/2022/04/05/lU8KkHTW4jNP6AD.jpg)

## 26.3 框架代码

```python
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
```



## 26.4 模型说明

### 26.4.1 设计要点

过滤器模式中主要有三个角色，在设计过滤器模式时要找到并区分这些角色。

1. 过滤的目标（Target）：即要被过滤的对象，通常是一个对象数组（对象列表）。
2. 过滤器（Filter）：负责过滤不需要的对象，一般一个规则对应一个类。
3. 过滤器链（FilterChain）：即过滤器的集合，负责管理和维护过滤器，用这个对象进行过滤时，它包含的每一个子过滤器都会进行一次过滤。这个类并不总是必要的，但如果有多个过滤器，有这个类将会带来极大的方便。

### 26.4.2 优缺点

1. 优点

    + 将对象的过滤、校验逻辑抽离出来，降低系统的复杂度。

    + 过滤规则可实现重复利用。

2. 缺点

    + 性能较低，每个过滤器对每一个元素都会进行遍历，如果有$n$个元素，$m$个过滤器，则复杂度度为$O(mn)$。

## 26.5 应用场景

1. 敏感词过滤、舆情监测。
2. 需要对对象列表(或数据列表)进行检验、审查或预处理的场景。
3. 对网络接口的请求和响应进行拦截，例如对每个请求和响应记录日志，以便日后分析。

# 第二十七章 对象池技术

## 27.1 核心思想

对象池是一个集合，里面包含了我们需要的已经过初始化且可以使用的对象。我们称这些对象都被池化了，也就是被对象池所管理，想要使用这样的对象，从池子里取一个就行，但是用完得归还。可以将对象池理解为单例模式的延展一多例模式。对象实例是有限的，要用可以，但用完必须归还，这样其他人才能再使用。

## 27.2 UML类图

![对象池UML类图](https://s2.loli.net/2022/04/05/QxmufIGVH1Jpg2o.jpg)

## 27.3 框架代码

```python
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
```



## 27.4 模型说明

### 27.4.1 设计要点

对象池机制有两个核心对象和三个关键动作对象（Object）

1. 两个核心对象
    + 要进行池化的对象：通常是一些创建和销毁时会非常耗时，或对象本身非常占内存的对象。
    + 对象池(Object Pool)：对象的集合，其实就是对象的管理器，管理对象的借用、归还。
2. 三个关键动作对象
    + 借用对象（borrow object）：从对象池中获取对象。
    +  使用对象（using object）：即使用对象进行业务逻辑的处理。
    + 归还对象（return、 give back）：将对象归还对象池，归还后这个对象的引用不能再用于其他对象，除
        非重新获取对象。

### 27.4.2 优缺点

1. 优点
    + 对象池机制通过借用、归还的思想，实现了对象的重复利用，能有效地节约内存，提升程序性能。
2. 缺点
    + 借用和归还必须成对出现，用完必须归还，不然这个对象将一直处于被占用状态。
    + 对已归还的对象的引用，不能再进行任何其他的操作，否则将产生不可预料的结果。

## 27.5 应用场景

对象池机制特别适用于那些初始化和销段的代价高且需要经常被实例化的对象，如大对象、需占用I/O的对象
等，这些对象在创建和销毁时会非常耗时，以及对象本身非常占内存的对象。

如果是简单的对象，对象的创建和销毁都非常迅速，也“不吃”内存；但有些对象，把它进行池化的时间比自己构建还多，这样就不划算了。因为对象池的管理本身也是需要占用资源的，如对象的创建、借用、归还这些都是需要消耗资源的。我们经常听到的（数据库）连接池、线程池用到的都是对象池机制的思想。

# 第二十八章 回调机制

## 28.1 核心思想

把函数作为参数，传递给另一个函数，延迟到另一个函数的某个时刻执行的过程叫回调。假设我们有一个函数`callback(args)`这个函数可以作为参数传递给另一个函数`otherFun(fun，args)`，如`otherFun(callback, [1, 2, 3])`，那么`callback`叫回调函数，`otherFun`叫高阶函数，也叫包含（调用）函数。

回调函数属于函数式编程，也就是面向过程编程。在面向对象编程中，如何实现这种机制呢?特别是那些不支持函数作为参数来传递的语言（如Java），可以使用策略模式实现回调机制。

## 28.2 UML类图

![回调模式UML类图](https://s2.loli.net/2022/04/05/iJVlkNoxI6gDqpz.jpg)

## 28.3 框架代码

```python
from abc import ABC,abstractmethod
import sys

class Strategy(ABC):
    @abstractmethod
    def alogrithm(self, *args, **kwargs):
        pass

class StrategyImplA(Strategy):
    def alogrithm(self, *args, **kwargs):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class StrategyImplB(Strategy):
    def alogrithm(self, *args, **kwargs):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} is running...")

class Context:
    def interface(self, strategy:Strategy, *args, **kwargs):
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} before callback...")
        strategy.alogrithm(*args, **kwargs)
        print(f"{self.__class__.__name__}/{sys._getframe().f_code.co_name} after callback...")

if __name__ == "__main__":
    c = Context()
    c.interface(StrategyImplA())
    print("*"*50)
    c.interface(StrategyImplB())
```



## 28.4 模型说明

### 28.4.1 设计要点

在设计回调机制的程序时要注意以下几点：

1. 在支持函数式编程的语言中，可以使用回调函数实现。作为参数传递的函数称为回调函数，接收回调函数（参数）的函数称为高阶函数或包含函数。
2. 在只支持面向对象编程的语言中，可以使用策略模式来实现回调机制。

### 28.4.2 优缺点

1. 优点
    + 避免重复代码。
    + 增强代码的可维护性。
    + 有更多定制的功能。
2. 缺点

+ 可能出现“回调地狱”的问题，即多重的回调函数调用。如回调函数A被高阶函数B调用，同时B本身又是一个回调函数，被函数C调用。我们应尽量避免这种多重调用的情况，否则代码的可读性很差，程序将很难维护。

## 28.5 应用场景

1. 在第三方库和框架中；
2. 异步执行（例如读文件、发送HTTP请求）；
3. 在需要更多通用功能的地方，更好地实现抽象（可处理各种类型的函数）；

# 第二十九章 MVC模式

## 29.1 MVC模式

MVC模式是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：模型（Model） 、视图（View）和控制器（Controller）。模型负责数据的持久化（也就是存储）；视图负责数据的输入和显示，直接和用户交互的一层，如大家看到的网站的页面内容、在表单上输入的数据；控制器负责具体的业务逻辑，根据用户的请求内容操作相应的模型和视图。

<img src="https://s2.loli.net/2022/04/05/ltpBS7iqf1AYx4r.jpg" alt="MVC示意图" style="zoom: 33%;" />

1. User直接与View进行交互；
2. View传递指令到Controller；
3. Controller完成业务逻辑后，要求Model更新数据和状态；
4. Model将新的数据发送到View，用户得到反馈；

## 29.2 MVP模式

MVP是MVC的一个变种，很多框架都自称遵循MVC模式，但是实际上它们却实现的是MVP模式；在MVP中使用Presenter对视图和模型进行解耦，视图和模型独立发展，互不干扰，沟通都通过Presenter进行。

<img src="https://s2.loli.net/2022/04/05/bRtg6qy2jP1vEmU.jpg" alt="MVP示意图" style="zoom:33%;" />

1. Presenter相当于MVC中的Controller，负责业务逻辑的处理；
2. Model和View不能直接通信，只能通过Presenter间接地通信；
3. Presenter与Model、Presenter与View是双向通信；
4. Presenter协调和控制Model与View的工作；

## 29.3 MVVM模式

MVVM（Model-View-ViewModel）最早由微软提出，ViewModel指“Model of View”，即视图的模型，它将View的状态和行为抽象化，让我们可以将UI和业务逻辑分开。

![MVVM示意图](https://s2.loli.net/2022/04/05/jq5LCiMSRcNabk9.jpg)

在MVP中，Presenter负责协调和控制Model与View的工作，保证Model和View的数据实时同步和更新，但这个操作需要程序员写代码手动控制。而MVVM中ViewModel把View和Model的同步逻辑自动化了，以前Presenter负责的View和Model同步不再需要手动地进行操作，而是交给框架所提供的数据绑定功能来负责，只需要告诉它View显示的数据对应的是Model的哪部分即可。

<img src="https://s2.loli.net/2022/04/05/72AroTmCehQs4cy.jpg" alt="MVVM_双向数据绑定" style="zoom: 67%;" />

双向数据绑定可以简单地理解为一个模板引擎，当视图改变时更新模型，当模型改变时更新视图，如下图所示。不同的框架实现双向数据绑定的技术有所不同，Vue采用数据劫持和发布订阅模式的方式。

## 29.4 模型说明

### 29.4.1 设计要点

MVC模式有三个关键的角色，在设计MVC模式时要找到并区分这些角色：

1. 模型（Model）：负责数据的存储和管理。
2. 视图（View）：负责数据的输入和显示，是直接和用户交互的一层。
3. 控制器（Controller）：负责具体的业务逻辑，根据用户的请求内容操作相应的模型和视图。

### 29.4.2 优缺点

1. 优点
    + 低耦合性。MVC模式将视图和模型分离，可以独立发展。
    + 高重用性和可适用性。对于某些应用，我们可能会有不同的端，如Web端、移动端、桌面端，但它们使用
        的用户数据是相同的，因此可以用同一套服务端代码，即M层和C层是相同的。
    + 快速开发， 快速部署。有很多现成的框架本身就是采用MVC模式进行设计的，如Java的Spring MVC、PHP
        的ThinkPHP，采用这些框架可以快速地进行开发。
    + 方便团队合作。将软件分成三层后，可以由不同的人员负责不同的模块。
2. 缺点
    + 增加了系统结构和实现的复杂性。对于简单的界面，严格遵循MVC会使模型、视图与控制器分离，增加很多代码。

## 29.5 应用场景

MVC的应用可谓随处可见，几乎可在各大成熟的框架中看到它的影子。MVC最核心的思想是软件分层，将软件分成模型层、视图层和控制层。

# 附录

## A. 创建型模式

关注的是对象的创建和初始化过程

1. 工厂方法
2. 抽象工厂
3. 单例模式
4. 构建模式
5. 原型模式

## B. 结构型模式

关注对象的内部结构设计

1. 适配模式
2. 桥接模式
3. 组合模式
4. 装饰模式
5. 外观模式
6. 享元模式
7. 代理模式

## C. 行为型模式

关注对象的特性和行为

1. 职责模式
2. 命令模式
3. 解释模式
4. 迭代模式
5. 中介模式
6. 备忘录模式
7. 监听模式
8. 状态模式
9. 策略模式
10. 模板模式
11. 访问模式
