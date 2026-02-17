# Print Hello world
# print("Hello world")


# Swap 2 numbers without using third variable

# a=10
# b=20
# a,b=b,a
# print("a is",a)
# print("b is",b)


# Check if the number is positive,Negative or zero

# a=int(input("Enter any number"))
# if a>0:
#     print("positive")
# elif a<0:
#     print("Negative")
# else:
#     print("Zero")


# Find the largest of 3 numbers

# a=int(input("Enter 1st number"))
# b=int(input("Enter 2nd number"))
# c=int(input("Enter 3rd number"))
# if a>=b and a>=c:
#     print("a is big")
# elif b>a and b>c:
#     print("b is big")
# else:
#     print("c is bigS")



# Find the factorial of number

# a=int(input("Enter any number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)




# Generate a fibonacci number

# n=10
# a,b=0,1
# for _ in range(2,n+1):
#     print(a)
#     a,b=b,a+b



# Check prime number

# a=int(input("Enter any number"))
# if a<=1:
#     print("Not prime")
# else:
#     for i in range(2,a):
#         if a%i==0:
#             print("Not prime")
#             break
#     else:
#         print("prime")




# Sum of sumbers

# a=10
# sum=0
# for i in range(0,a+1):
#     sum=sum+i
# print(sum)


#Reverse a string 

# s=input("Enter a string")
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)




# Reverse a string using slicing

# a=input("Enter a string")
# a=a[::-1]
# print(a)



# Check whetherv a string is palindrome or not

# a=input("Enter a string")
# rev=""
# for i in a:
#     rev=i+rev
# if a==rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# Reverse a number

# a=int(input("Enter a number"))
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# print(rev)
    
    
# Check whether the number is palindrome or not

# a=int(input("Enter a number"))
# temp=a
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# if rev==temp:
#     print("palindrome")
# else:
#     print("Not palindrome")



# ArmStrong number

# a=int(input("Enter any number"))
# temp=a
# sum=0
# while a>0:
#     d=a%10
#     sum=sum+d**3
#     a=a//10
# if temp==sum:
#     print("ArmStrong")
# else:
#     print("No")



#count the digits in a number 

# a=123456
# count=0
# while a>0:
#     count+=1
#     a//=10
# print(count)





for i in range(1,21):
    if i%3==0:
        continue
    print(i,end=" ")