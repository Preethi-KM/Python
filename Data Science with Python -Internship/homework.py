# # # # secret = 7
# # # # guess = 0
# # # # while guess != secret:
# # # #     guess = int(input("Enter your guess: "))
# # # #     if guess < secret:
# # # #         print("Too low!")
# # # #     elif guess > secret:
# # # #         print("Too high!")
# # # #     else:
# # # #         print("Correct! ")






# # # secret = "python"
# # # guess = ""
# # # while guess != secret:
# # #     guess = input("Enter secret word: ")
# # #     if guess != secret:
# # #         print("Wrong! Try again.")
# # # print("You guessed it correctly ")








# # text = ""
# # while text != "exit":
# #     text = input("Type something (or 'exit' to stop): ")
# #     print("You typed:", text)






# password = "open123"
# attempts = 3

# while attempts > 0:
#     guess = input("Enter password: ")
#     if guess == password:
#         print("Access Granted ")
#         break
#     else:
#         attempts -= 1
#         print("Wrong password! Attempts left:", attempts)

# if attempts == 0:
#     print("Access Denied ")







# class BankAccount:
#     def deposit(self):
#         print("Money deposited")

#     def withdraw(self):
#         print("Money withdrawn")


# class SavingsAccount(BankAccount):
#     def add_interest(self):
#         print("Interest added to your savings")

# acc = SavingsAccount()
# acc.deposit()       
# acc.withdraw()       
# acc.add_interest() 




# Abtraction

# hiding the intern details and showing only the essential details

# from abc import ABC,abstractmethod

# class colleges(ABC):
#     @abstractmethod
#     def password(self,a):
#         a=int(input("Enter your password"))
# class B():
#     def deposite(self):
#         print("You deposited money")
# class C():
#     def withdraw(self):
#         print("You withdraw the money")
# c=B()
# c.deposite()
# k=colleges()
# k.password()




# from abc import ABC,abstractmethod


# inbuilt functions
# Abstract example
# combination of abstraction and encapsulation



# ABSTRACT

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass      # hidden details

# class Car(Vehicle):
#     def start(self):
#         print("Car engine starts with a key")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike engine starts with a self-start button")

# v1 = Car()
# v1.start()

# v2 = Bike()
# v2.start()







# COMBINATION OF ABSTRACT AND ABSTRACTION
# online payment system






# from abc import ABC, abstractmethod

# class Payment(ABC):
#     def _init_(self, amount):
#         self.__amount = amount   

#     def get_amount(self):
#         return self.__amount     

#     @abstractmethod
#     def make_payment(self):
#         pass                     

# class UpiPayment(Payment):
#     def make_payment(self):

#         print(f"Paid ₹{self.get_amount()} using UPI")

# class CardPayment(Payment):
#     def make_payment(self):
        
#         print(f"Paid ₹{self.get_amount()} using Card")


# p1 = UpiPayment(500)
# p1.make_payment()

# p2 = CardPayment(1200)
# p2.make_payment()

    




# decorator
