class MyClass:
    '''
    1、使用类class关键字定义类；
    2、类名用驼峰的形式，首字母大写；
    3、定义完成后，就产生一个继承object的一个类对象，绑定名字MyClass上。
    '''

    '''A Example class'''
    #类的说明文档，MyClass.__doc__调用输出结果。

    x = 'abc'
    #类属性(变量)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    #self.age是实例变量，类不能访问。
    #__init__方法可以有，也可以没有，实例话的时候第一个调用的函数就是__init__
    #self方法不能有返回值。

    def show_age(self):
        return '{} is {}'.format(self.name, self.age)

    def foo(self):
        #定义类属性foo，也是方法。
        return 'My Class'

print(MyClass.x)    #可以调用，返回类属性(变量)的值；
print(MyClass.foo)  #可以调用，返回foo内存地址；
print(MyClass.__doc__)  #返回类的说明文档；
print(MyClass.__dict__)  #返回类的变量字典。

#说明：1、foo是method方法对象，不是普通的函数对象function，他必须至少有一个参数，切第一个参数必须是self（self可以换成其他的名字），这个位置就留给self
#2、self代指当前实例。

#类的实例化. 1、实例化后的实例是不用的实例，即使参数一样，实例化后的对象也不是一个，在内存中是两份存在。
#python实例化会首先调用__init__方法，这个地方的第一个参数必须留给self。

tom = MyClass('Tom', 30)
jerry = MyClass('Jerry', 2)

print(tom.name, jerry.age)
jerry.age += 1
print(jerry.age)
print(jerry.show_age())
jerry.xxx = 111
print(jerry.__dict__)

#########################################################################################################
#实例变量和类变量
class Person:
    age = 3
    def __init__(self, name):
        self.name = name

tom = Person('tom')
jerry = Person('jerry')
print(tom.age, jerry.age)
print(tom.name, jerry.name)
print(Person.age)
#print(Person.name)
# Person.age = 30
jerry.age =  20
print(jerry.__dict__)
print(tom.__dict__)
print(Person.__dict__)
print(tom.age, jerry.age, Person.age)
#1、类变量存放在类的dict中，实例变量存放在实例的dict中，类不能访问实例变量；
#2、实例变量可以访问类的变量，在实例变量查找，找到返回，找不到则返回：instance.__class__.var2class（类里搜索）
#3、jerry.age =  20 意思是在增加一个实例变量。

#特殊属性的含义：
class Person:
    age = 3
    def __init__(self, name):
        self.name = name


print('~~~~~~~~~~~~~~instance~~~~~~~~~~~~~~~~')
jerry = Person('jerry')
#print(jerry.__name__)  #实例没有__name__属性
print(jerry.__class__)  #打印实例所属的类
print(jerry.__dict__)   #实例字典
#print(jerry.__qualname__)

print('~~~~~~~~~~~~~~~class~~~~~~~~~~~~~~~')
print(Person.__name__)  #打印类名
print(Person.__class__) #打印类的类型
print(Person.__dict__)  #类的字典
print(Person.__qualname__)

#可以看出，类的属性保存在类的__dict__中，实例的属性保存在实例的__dict__中，如果实例访问类的属性，就需要借助__class__找到所属的类

class Person:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

tom = Person('Tom')
jerry = Person('Jerry',20)

Person.age = 30

print(Person.age, tom.age, jerry.age)   #可以访问当，各是各的age
print(Person.height, tom.height, jerry.height)  #实例没有height变量就去类变量中去获取。
jerry.height = 175                              #可以动态在外部增加实例的属性
print(Person.height, tom.height, jerry.height)

tom.height += 15
print(Person.height, tom.height, jerry.height)

Person.weight = 70  #动态增加类的属性，增加后实例均可以调用到。
print(Person.weight, tom.weight, jerry.weight)
print(tom.__dict__)
print(jerry.__dict__)
print(Person.__dict__)

print(tom.__dict__['height'])
print(tom.__dict__['weight'])  #tom__dict__中没有weight

#2中方法访问实例的变量：
#1、实例.变量名
#2、实例.__dict__['变量名']

#实例属性的查找顺序是指
# 实例用.来访问属性，会先自己的__dict__，如果没有，然后通过属性__class__找到自己的类，再去类的__dict__中查找。
##如果实例使用__dict__[变量名]访问变量，将不会按照上面的查找顺序找变量了。
#一般来说，类的变量名使用全大写的。


##使用装饰器装饰一个类：
def add_name(name):
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper

@add_name
class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showinfo(self):
        return self.name, self.age

#类方法和静态方法
class Person:

    @classmethod
    def class_method(cls):
        print('class = {0.__name__} ({0})'.format(cls))

Person.class_method()
print(Person.__dict__)
#1、类方法，在定义中使用@classmethod装饰器的方法
#2、必须只要有一个参数，且第一个参数留给了cls，cls指代调用者即类对象本身
#3、cls这是一个标识符，可以是任意的形参，为了易读性，请不要修改。
#4、cls可以操作类的属性，但是不能操作实例。

#静态方法
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        cls.HEIGHT = 180
        return 'class = {0.__name__} ({0})'.format(cls)

    @staticmethod
    def static_method():
        return Person.HEIGHT

p = Person('Jerry', 10)

print("~~~~~~~~~~class~~~~~~~~~~~")
Person.class_method()
print(Person.__dict__)
print(Person.static_method())

print("~~~~~~~~~~~~instance~~~~~~~~~~~~~~")
p.class_method()
print(p.static_method())
print(p.__dict__)

#总结：1、类可以调用除了绑定实例的方法，其他的属性均可以调用。
#2、实例可以调用类所有的变量及方法，除了非法的普通函数的式的定义，因为不合规，所以不用考虑。
#3、实例调用普通方法靠绑定实例来调用，调用静态方法、类方法，类变量及属性是通过找到类后再调用！！

#私有（Private）属性
class Person:

    def __init__(self, age):
        self.__age = age   #变量保存在实例的__dict__中，__age名字将会被修改为_Classname__age

    def show_age(self):
        # return self.__age  #在内部调用__age会默认调用_Classname__age
        return self._Person__age
p1 = Person(30)

print(p1.show_age())
p1.__age = 50
print(p1.show_age())
print(p1.__dict__)
print(p1.__dict__['__age'])

##########################################
print(p1.show_age())
print(p1.__dict__)
p1._Person__age = 50
print(p1.show_age())
print(p1.__dict__)
#通过改过的名字可以从外部直接修改
#保护变量、同公有变量一样都可以直接被外部访问，并修改，只是保护变量是python开发者共同遵守的一个协议规范，去看靠自觉。
#私有的方法也是同私有的属性一致。

#猴子补丁（Monkey Patch）
#通过模块导入方式实现方法的覆盖。

#属性装饰器
#方式一
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,v):
        self.__age = v

    @age.deleter
    def age(self):
        del self.__age

#方式二：
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def getage(self):
        return self.__age

    def setage(self,v):
        self.__age = v

    def delage(self):
        del self.__age

    age = property(getage, setage, delage, 'age property')
#属性装饰器一般对私有的变量在外部直接调用属性的方式来直接操作。

#对象销毁
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def __del__(self):
        print('delete {}'.format(self.name))
#__del__方法用于对象的销毁。
