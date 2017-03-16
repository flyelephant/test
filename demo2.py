import sys
import PySide
__author__ = 'fengjigang'
__metaclass__ = type
# def params(*param):
#     print param
# def params2(name,*param):
#     print name
#     print param
#
# params('ss','bb')
# params2('zhangsan','ss','bb')

# def hello_1(greeting,name):
#     print '%s,%s!' % (greeting,name)
# def hello_2(name,greeting):
#     print '%s,%s!' % (name,greeting)
#
# hello_1(greeting='hello',name='world')
# hello_1(name='world',greeting='hello')
# hello_2('hello','world')

# def params3(**param):
#     print param
# def params4(x,y,z=3,*param1,**param2):
#     print x,y,z
#     print param1
#     print param2
#
# params4(1,2,3,5,6,7,foo=1,header=2)

# x = 1
# scope = vars()
# scope['x'] += 1
# print x

# def combine(param):
#     print globals()['param'] + name
# def combine(param):
#     print param+ name
# name = 'kugou'
# global param;
# param = 'haha'
# combine('youku')
class Person:

    def __update(self):
        print 'update'
        pass
    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name
        self.__update()
    def greet(self):
        print 'Hello,world! I\'m %s' % self.name
def say():
    print 'say -----'
jim = Person()
jim.setName('jim')
jim.greet()

jim.greet = say
jim.greet()

sayHello = jim.greet


sayHello()

jim._Person__update()

def foo(x):return x*x
foo = lambda x: x*x

# print foo(3)

class MemberCounter:
    members = 0;
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
print m1.members

m2 = MemberCounter()
m2.init()
print m2.members

print hasattr(m2,'init')
print callable(getattr(m2,'init'))

class FooBar:
    def __init__(self,value = 32):
        self.value = value
f1 = FooBar(90)
print f1.value

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaaaaa'
            self.hungry = False
        else:
            print 'NO,thx'

class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super(SongBird,self).__init__()
        self.sound = 'wuwuwu'
    def song(self):
        print self.sound

song = SongBird()
song.song()
song.eat()
song.eat()

print PySide.__doc__