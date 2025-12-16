# class A:
#     def Marks(self):
#         self.__marks=0
#     def set_marks(self,m):
#         if 0<=m<=100:
#             self.__marks=m
#         else:
#             print("Enter marks within 0 and 100")
#     def get_marks(self):
#         return self.__marks
# a=A()
# a.set_marks(95)  
# print(a.get_marks())       
# a.__marks=34
# print(a.get_marks)




# class A:

#     def marks(self,m):
#         self.__m=m
#     def display(self):
#         return self.__m

# a=A()
# a.marks(90)
# print(a.display())

# a.__m=34

# print(a.display())




# compile time polymorphism

# class A:
#     def a(self,a):
#         self.a=a
#         return a
#     def a(self,b,c):
#         self.b=b
#         self.c=c
#         print(b,c)
# o1=A()
# o1.a(2)
# # o2.a(2,3)







# run time polymorphism

# class Animal:
#     def speak(self):
#         print("All animals speak")
# class Dog:
#     def speak(self):
#         print("Dog barks")
# class Cat:
#     def speak(self):
#         print("cat meows")
# a=Animal()
# b=Dog()
# c=Cat()
# a.speak()
# b.speak()
# c.speak()









# class Meth:
#     def addition(self,*args):
#         if len(args)==2:
#             print(args[0]+args[1])
#         elif len(args)==3:
#             print(args[0]+args[1]+args[2])
# a=Meth()
# a.addition(2,4)   
# a.addition(5,4,6)   
# a.addition(4,5,6,8)



# class Demo:
#     def a(self,*args):
#         return sum(args)
# d=Demo()
# # print(d.a(2,3))
# # print(d.a(4,5,6))




# class A:
#     def Marks(self,m):
#         self.__m=m
#     def display(self):
#         return self.__m
# o=A()
# o.Marks(99)
# print(o.display())
# o.m=77
# print(o.display())




# class A:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
# o=A()
# o.add(2,3)
    
    
    
    
    
    
    
    
    
    
# Why Encapsulation is Needed 


#  Encapsulation helps in
# • Data security
# • Prevention of accidental modification
# • Better maintainability of code





# Why Polymorphism is Needed

# Polymorphism helps in
# • Writing flexible code
# • Reducing complexity
# • Improving code reusability
# • Making programs easier to extend












# Syntax
# Try:
    # Code that may raise an Error
# except Someerror:
    # What to do if error happens
# else:
    # Run if no error
# finally
    # Always Run




# Ex1

# try:
#     a=int(input("Enter first number="))
#     b=int(input("Enter second number="))
#     print(a/b)
# except:
#     print("Error")
# finally:
#     print("Executed")
 
 
 
 
    
# If you want to know which error
  

# try:
    # a=int(input("Enter first number="))
    # b=int(input("Enter second number="))
#     print(a/b)
# except Exception as e:
#     print(f"Error:{e}")
# finally:
#     print("Executed")
 
 
 
 
 
# Exception:This is the common base class for all exceptions


# try:
#     a=int(input("Enter first number="))
#     b=int(input("Enter second number="))
#     print(a/b)
# except Exception as e:
#     print(f"Error:{e}")
# else:
#     print("No Error found")
# finally:
#     print("Executed")
 
 



# When you want to catch specific error


# try:
#     a=int(input("Enter first number="))
#     b=int(input("Enter second number="))
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divisible by zero")
# except ValueError:
#     print("Please Enter valid number")
# except Exception as e:
#     print(f"Error:{e}")
# else:
#     print("No Error found")
# finally:
#     print("Executed")





# Most common Errors
# 1.ZeroDivisionError
# try:
#     a=int(input("Enter first number="))
#     b=int(input("Enter second number="))
#     print(a/b)
# except Exception as e:
#     print(f"Error:{e}")
# finally:
#     print("Executed")



# 2>ValueError
# try:
#     a=int(input("Enter first number="))
#     b=int(input("Enter second number="))
#     print(a/b)
# except ValueError:
#     print("Plase enter valid number")
# finally:
#     print("Executed")



# 3>TypeError
# Raises when you use the wrong datatype in an operation

# try:
#     result="Hello"+5
# except TypeError:
#     print("You can't add string and number")
# finally:
#     print("Executed")




# Index Error

# raises when we try to access invalid index in a list 
# try:
#     fruits=["apple","mango","banana"]
#     print(fruits[1])
# except IndexError:
#     print("That index does not exist")
    


# Key Error
# Raises when a dictionary key does not exist

# try:
#     data={
#         "name1":"Varshini",
#         "name2":"Preeti"
#     }
#     print(data["name1"])
# except KeyError:
#     print("That key is not in a dictionary")


# NameError
# When we try to acces a variable without defining

# try:
#     print(xyz)
# except NameError:
#     print("That variable is not defined")




# Attribute Error

# # Raises when an invalid function or variable is used in an object


# try:
#     name="preethi"
#     name.append("KM")
# except AttributeError:
#     print("That function does not work on string")




# FileNotFoundError

# try:
#     f=open("pre.txt","r")
#     a=f.read()
#     print(a)
# except FileNotFoundError:
#     print("This file is not found")