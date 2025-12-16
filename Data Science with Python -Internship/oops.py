
# def pree(age):
#     if age>18:
#         print("eligible")
#     else:
#         print("not eligible")
# a=int(input("Enter the age"))
# pree(a)


# function==>Independent
# method==>dependent


# class preethi():
#     print('Hello')
# preethi()



# class preethi():
#     def addition(self,a,b):
#         print(a+b)
# obj=preethi()
# obj.addition(2,3)


# Advantanges:
# 1.code reuse: It allows developrs to avoid writting the same code reoeatedly
# 2.Adding options:
    
    
# base class,derived clas


# class dad:
#     def phone(self):
#         print("This is dad's phone")
# class son(dad):
#     def laptop(self):
#         print("This is sons laptop")
# class daughter(dad,son):
#     def tshirt(self):
#         print("hello")
# obj=daughter()
# obj.phone()
# obj.laptop()
# obj.tshirt()



# class Addition:
#     def Add(self,a,b):
#         print(a+b)
# class Subtracti(Addition):
#     def Sub(self,x,y):
#         print(x-y)
# o=Subtracti()
# o.Add(3,4)
# o.Sub(7,5)



# class dad:
#     def Money(self):
#         print("dad's money")
# class son(dad):
#     def Riding(self):
#         print("Son knows riding and having money")
# class daughter(dad):
#     def Dancing(self):
#         print("she knows dancing and having money")
# o1=son()
# o2=daughter()
# o1.Money()
# o2.Money()
# o1.Riding()
# o2.Dancing()



# __init__ constructor


# class car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#         print("The brand is",self.brand)
#         print("The color is",self.color)
# a=car("BMW","Block")
# print(a.brand)
# print(a.color)




# class A:
#     def __init__(self):
#         print("A")
# class B:
#     def __init__(self):
#         print("B")
# class C(A,B):
#     def __init__(self):
#         print("C")
# o=C()

# here c only printing becase interpreter get confused that which inheritance that i nedd to call

# That's why we have super keyword

# class A:
#     def __init__(self):
#         print("A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")
# o=B()



# use inheritance bank account real world example



# encapsulation

# def addition(*args):
#     return sum(args)
# print(addition(1,2,3,4,5))




# def addition(a,b):
#     print(a+b)
# addition(2,3,4)




# *args


# def addition(*args):
#     return sum(args)
# print(addition(1,2,3,4,5,6,7))



# method overriding

# class dog:
#     def sound(self):
#         print("barking")
# class cat:
#     def sound(self):
#         print("meow")
    
# d=dog()
# d.sound()
# c=cat()
# c.sound()





# class student():
#     def __init__(self, variable_name, register_no):
#         self.variable_name = variable_name
#         self.register_no = register_no
#     def display(self):
#         print("Name:", self.variable_name)
#         print("Register No:", self.register_no)

# s = student("preethi", 23)
# s.display()





# class fruit():
#     def __init__(self, color):
#         self.color = color

# pas= fruit("red")
# print(pas.color)




# class teacher():
#     def __init__(self, name, resister_no):
#         self.name = name
#         self.resister_no = resister_no

#     def display(self):
#         print("Teacher name", self.name)
#         print("Teacher resister_no", self.resister_no)

# t1 = teacher("preethi", 45)
# t2=teacher("varshini",45)
# t1.display()
# t2.display()




# # method overloading
# class A():
#     def add(a,b,c=0):
#         print(a+b)
#         print(a+b+c)
# o1=A()
# o1.add(20,30)    
# same function works in diffrent ways

# print(10+20)
# print("hi"+ "hello")




# decorator

# adding additional features to the existing function

# def add_sprinkles(func):
#     def wrapper():
#         print("you are adding sprincles")
#         func()
#     return wrapper
# @add_sprinkles
# def get_ice_cream():
#     print("Here is your ice cream")
    

# get_ice_cream()





# def add_sprinkles(fun):
#     def wrapper(*args, **kwargs):
#         print("you add sprincles")
#         fun(*args,**kwargs)
#     return wrapper

# @add_sprinkles
# def get_ice_cream(flavor):
#     print(f"here is your{flavor} ice creame" )
    
# get_ice_cream("vennila")



# Tread
# def fun1():
#     for i in range(5):
#         print("hi")
# def fun2():
#     for i in range(5):
#         print("hello")
# fun1()
# fun2()



# for i in range(5):
#      print("hi")
# else:
#     print("done")
    
# if we use break,continue,any transfer statement then else block will not work


# def cream(func):
#     def  preethi():
#         print("Wait untill adding cream")
#         func()
# #         print('You can eat now')
# #     return preethi
# # @cream
# # def  ice():
# #     print("yeah cream  added")
# # ice()




# # def Decorator(func):
# #     def Voting():
# #         print("After 18 only you can eligible for voting ok")
# #         func()
# #         print("Yeah your 18 now ....You can vote")
# #     return Voting
# # @Decorator
# # def voting():
# #    print("waite still you are not 18")
# # voting()





# def Decorate(func):
#     def preethi(*args,**kwargs):
#         print("I am ready to take any number of arguments")
#         func(*args,*kwargs)
#     return preethi

# @Decorate
# def add(a,b):
#     print(a+b)
# add(2,3)
    
    
    
# class Greet():
#     def a(self):
#         print("Hello preethi")
# o=Greet()
# o.a()


# def greet():
#     print("heloo")
# greet()




# Exception is a run time error
# Systex error is a compile time error



# try:
#     a=int(input("a:"))
#     b=int(input("b:"))
#     # print(a/b)
# except Exception as e:
#     print("somthing:",e)





# try:
#     a=int(input("a:"))
#     b=int(input("b:"))
#     print(a+b)
# except ValueError:
#     print("This is error")
# finally:
#     print("Done")



# Tread:

# 1.kernel level thread
# 2.user level thread



import _thread
import time
def a(msg):
    count=0
    while count<5:
        time.sleep(4)
        print(msg)
def b(msg):
    count=0
    while count<5:
        count+=1
        time.sleep(2)
        print(msg)
try:
    _thread.start_new_thread(a,("Thread1",))
    _thread.start_new_thraed(b,("Thread",))
except:
    print("error to start thread")

while 1:
    pass






# pdf exstarction

# regular expressions
# GUI