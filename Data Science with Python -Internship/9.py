# OOps
# class,object

# INHERITANCE
# DEF=>child class aquiring the properties from the parent class
# or==>Derived class aquiring the properties fron base class

# class class_name():
#     statements;or pass
# variable_name=className()



# Types
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


# independent =>function
# whithever dependent to any class that is method
# class A():
#     def fun(self):  
#         print("hello")
# obj=A()
# obj.fun()



# class A():
#     def fun():  
#         print("hello")
#     fun()
# obj=A()
# This is ok  but if we want to acces through objec then we have to mention the self keyword 
# Without self we get an error
# Becase object is a instant of class




# class A():
#     def fun(self):  
#         print("hello")
#     def fun1(self):
#         print("hi")
    
# obj=A()
# obj.fun()
# obj.fun1()





# class A():
#     def fun(self):  
#         print("hello")
# class B(A):
#     def fun1(self):
#         print("preethi")
# obj=B()
# obj.fun()
# obj.fun1()




# Lini by line execution
# class A():
#     def fun(self):  
#         print("hello")
# class B(A):
#     def fun1(self):
#         print("preethi")
# obj=B()
# obj.fun1()
# obj.fun()




# Multiple inheritance
# class A():
#     def fun(self):  
#         print("hello")
# class B():
#     def fun1(self):
#         print("preethi")
# class C(A,B):
#     def fun2(self):
#         print("Hi")
# obj=C()
# obj.fun()
# obj.fun1()
# obj.fun2()






# Multilevel inheritance
# class A():
#     def fun1(self):
#         print("parent")
# class B(A):
#     def fun2(self):
#         print("Raju")
# class C(B):
#     def fun3(self):
#         print("Hemanth")
# object=C()
# object.fun1();
# object.fun2();
# object.fun3();





# Hierarchical Inheritance
# class A():
#     def fun1(self):
#         print("Hello");
# class B(A):
#     def fun2(self):
#         print("Hiii")
# class C(A):
#     def fun3(self):
#         print("Mom")
# obj=C()
# obj2=B()
# obj.fun3()
# obj.fun1()
# obj2.fun2()
  
  
  
  
  
  
# Hibrid Inheritance

# class Grandpa():
#     def fun1(self):
#         print("Hii")
# class Father(Grandpa):
#     def fun2(self):
#         print("Good morning")
# class Child(Father,Grandpa):
#     def fun3(self):
#         print("I know Everything")
# obj=Child()
# obj.fun1()
# obj.fun2()
# obj.fun3()



# CONSTRUCTOR(__init__)===>It is a special method whenver we create an object to the class then  it call automatically without calling anything
# class A():
#     def __init__(self):
#         print("Good")
#     def fun(self):
#         print("Bad")
# obj=A();
# If we want to acces fun then we need to call it but constructor no need to call






# Class and instance variable







class A():
    def __init__(self):
        print("Good")
class B():
    def __init__(self):
        print("Very Good")
    def fun(self,a):
        self.a=a;
        print(self.a)
obj=A();
obj2=B();
obj2.fun(2)