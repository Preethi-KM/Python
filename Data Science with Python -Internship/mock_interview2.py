# # for i in range(10):
# #     print(i,end=" ")


# # for i in "preethi":
# #     print(i)


# # sum=0
# # for i in range(1,11):
# #     sum=sum+i
# # print(sum)    


# # sum=0
# # for i in range(1,11):
# #     sum=sum+i
# # print(sum)


# # n=int(input("enter any number"))
# # fact=1;
# # for i in  range(1,n+1):
# #     fact=fact*i
# # print(fact)




# # def Factorial(num):
# #     fact=1
# #     for i in range(1,num+1):
# #         fact=fact*i
# #     print(fact)
# # Factorial(5)



# # def Factorial(num):
# #     fact=1
# #     for i in range(1,num+1):
# #         fact=fact*i
# #     print(fact)
# # Factorial(5)



# # for i in range(2,21,2):
# #     print(i,end=" ")


# # for i in range(21):
# #     if i%2==0:
# #         print(i,end=" ")
    
    
    
    
# # list=[1,2,3,4,5,6,7,8]
# # count=0
# # for i in list:
# #     if i%2!=0:
# #         count+=1
# # print(count)




# # s="preethi"
# # print(s[::-1])




# # s="preethi"
# # rev=' '
# # for i in s:
# #     rev=i+rev
# # print(rev)




# # s="preethi"
# # count=0
# # vowels="aeiouAEIOU"
# # for i in "preethi":
# #     if i in vowels:
# #         count+=1
# # print(count)



# # a=int(input("Enter any number"))
# # for i in range(0,a+1):
# #     print('*'*i)    






# # a=4;
# # for i in range(1,a+1):
# #     print("*"*i)    




# # a=5;
# # for i in range(a,0,-1):
# #     print("*"*i)




# # a=5
# # for i in range(a,0,-1):
# #     print("*"*i)




# # a=5
# # for i in range(1,a+1):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()






# # num=5
# # for i in range(1,num+1):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()



# # num=5
# # count=1
# # for i in range(1,num+1):
# #     for j in range(i):
# #         print(count, end=" ")
# #         count+=1
# #     print()



# # n=5
# # for i in range(1,n+1):
# #     print(" "*(n-i)+"* "*i )






# # n=5
# # for i in range(1,n+1):
# #     print(" "*(n-i)+"* "*i)






# # n=5
# # for i in range(n,0,-1):
# #     print(" "*(n-i)+"* " *i)



# # n=5
# # for i in range(1,n+1):
# #     print(" "*(n-i)+"* "*i)
# # for i in range(n,0,-1):
# #     print(" "*(n-i)+"* "*i)





# # s="pop"
# # if s==s[::-1]:
# #     print("palindrome")
# # else:
# #     print("Not")





# # s="pop"
# # rev=""
# # for i in s:
# #     rev=i+rev
# # if rev==s:
# #     print("palindrome")
# # else:
# #     print("not")




# # num=2
# # for i in range(1,21):
# #     print(num,"X",i,"=",i*num-)
    
    
    
# # num=2;
# # i=1
# # while i<=10:
# #     print(num,"X",i,"=",i*num)
# # #     i+=1




# # class Car:
# #     def __init__(self,brand):
# #       =  self.brandnd=brand
# #     def show_brand(self):
# #         return self.brand
# # c=Car("BMW")
# # # a=c.show_brand()
# # print(c.brand)
# # print(c.brand)





# # class car:
# #     def __init__(self,brand):
# #         self.__brand=brand
# #     def display(self):
# #         print("The brand is",self.__brand)
# # c=car("BMW")
# # print(c.__brand)
# # c.display()



# # Encapsulation
# # Making public variable to private ans allowing acces on;y to method?

# # class car:
# #     def __init__(self,brand):
# #         self.__brand=brand
# #     def show(self):
# #         return self.__brand
# # c=car("BMW")
# # a=c.show()
# # print(a)



# # # Inheritance
# # derived class inherite the properties from the base class

# # Single level inheritance
# # multi level inheritance
# # Mutiple inheritance
# # Hierarchical inheritance
# # Hybrid inheritance

# # Single level inheritance

# # class A:
# #     def showA(self):
# #         print("this is parent class")
# # class B(A):
# #     def showB(self):
# #         print("this is child class")

# # b=B()
# # b.showA()
# # b.showB()
# # 


# # multiple inheritance
# # derived class inherit the properties from the 2 or more base classesclass 


# class parent1:
#     def showA(self):
#         print("dad knows bike ride")
# class parent2:
#     def showB(self):
#         print("mother knows cocking")
# class child(parent1,parent2):
#     def showc(self):
#         print("Child knows bothe bike ride as well as cocking")
        
        
# c=child()
# c.showA()
# c.showB()
# c.showc()



# def creame(func):
#     def preethi():
#         print("Waite untill adding creame plase")
#         func()
# #         print("yes you can eat now")
# #     return preethi
# # @creame
# # def Main():
# #     print("yeah creame added")
# # Main()




# f=open("preethi.txt","r")
# a=f.read()
# print(a)
# f.close()




# f=open("preethi.txt","r")
# a=f.read()
# print(a)
# f.close()




import re
text="preethi 7676783274"
match=re.search("\\d{3}",text)
print(match.group(.))