# a=int(input("Enter any number:"))
# if a>0:
#     print("Positive")
# elif a<0:
#     print("Neagtive")
# else:
#     print("It is zero")




# for i in range(10):
#     print(i,end=" ")



# num=int(input("Enter any number:"))

# while i<num:
#     if num%2==0:
#         print("even")
#         break
#     else:
#         print("odd")


          
# i+=1



# for i in  range(2,10,2):
#     print(i)



# num=1
# while num<=10:
#     if num%2==0:
#         print(num)
#     num=num+1  





# i=1;
# while i<=10:
#     if i%2==0:
#         print(i)
#     i=i+1


# i=2;
# while i<20:
#     print(i)
#     i+=2


# def Factorial(num):
#     fact=1;
#     for i in range(1,num+1):
#         fact=fact*i;
#     print(fact)
        
    
# Factorial(5)




# def  Factorial(num):
#         fact=1
#         for i in range(1,num+1):
#             fact=fact*i
#         print(fact) 
# Factorial(5)




# def Factorial(num):
#    if num==0 or num==1:
#        return 1
#    else:
#        return num*Factorial(num-1)
# print(Factorial(5))




# num=int(input("Enter any number"))
# fact=1;
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)




# n=5
# fact=1;
# i=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print(fact)
    

# s=input("Enter any string")
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not")


# a=int(input("first:"))
# b=int(input("second:"))
# c=int(input("third:"))
# if a>=b and a>=c:
#     print("a")
# elif b>=a and b>=c:
#     print(b)
# else:
#     print("c")




# s=input("Enter any string")
# rev=" "
# for i in s:
#     rev=i+rev
# print(rev)



# s=input("Enter any string")
# rev=" "
# i=len(s)-1
# while i>=0:
#     rev+=s[i]
#     i-=1
# print(rev)





# s=input("Enter any string")
# vower=0
# consonent=0
# v="aeiouAEIOU"
# for i in s:
#     if i in v:
#         vower=vower+1
#     else:
#         consonent=consonent+1
# print(vower)
# print(consonent)




l=[1,2,3,2,2,2]
r=list(set(l))
print(l)