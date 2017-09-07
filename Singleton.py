# -*-coding:utf-8-*-
# 1.使用__new__方法实现
class Singleton1(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

class TestClass()
    a = 1

# 使用装饰器
def Singleton2(cls,*args,**kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return _singleton

# 使用Python模板
from ... import ...

#共享属性

"""
所谓单例就是所有引用（实例、对象）拥有相同的的状态（属性）和行为（方法）
同一个类的所有实例天然拥有相同的行为（方法）
只需要保证一个类的所有实例具有相同的状态（属性）即可
"""

class Singleton3(object):
    _state = {}
    def __new__(cls,*args,**kwargs):
        obj = super(Singleton3,cls).__new__(cls,*args,**kwargs)
        obj.__dict__ = cls._state
        return obj