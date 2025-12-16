# # Variables and datatypes
# # Python is dynomically typed so no need to declare the varible type

# # a=10;
# # b=3.5;
# # c="preethi";
# # d=True;
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))



# # input and output in python

# # a=input("Enter your name:")
# # b=int(input("ENter your age:"))
# # print(f"Your name is {a} and your age is {b}")



# # Check number is positive or negative

# # x=-1;
# # if x>0:
# #     print("positive")
# # elif x==0:
# #     print("Zero")
# # else:
# #     print("Negative") 




# # for loop

# # for i in range(0,11):
# #     print(i)
 
 
    
# # for loop ouput in one line ==>end=""

# # for i in range(1,11):
# #     print(i,end=" ")




# # While loop

# # i=1
# # while i<11:
# #     print(i)
# #     i=i+1
 
 
    

# # In one line

# # i=1;
# # while i<11:
# #     print(i,end=" ")
# #     i=i+1




# # Function

# # def add(a,b):
# #     return a+b;
# # print(add(2,3))



# # Factorial using Function

# # def Fact(n):
# #     fact=1;
# #     for i in range(1,n+1):
# #         fact=fact*i;
# #     print(fact)
# # Fact(5)




# # Factorial using recursion(Function callimng itself)

# # def Fact(n):
# #     if n==0 or n==1:
# #         return 1
# #     else:
# #         return n*Fact(n-1)
# # print(Fact(5))




# #  fibonocci using loop
# # Range=5;
# # a,b=0,1
# # for _ in range(Range):
# #     print(a)
# #     a,b=b,a+b

# # a=5;
# # a,b=0,1
# # for _ in range(a):
# #     print(a)
# #     a,b=b,a+b
 

# #  Fibonocci using Recursion
# # def Fibo(n):
# #     if n<=1:
# #         return n
# #     else:
# #         return Fibo(n-1)+Fibo(n-2)
# # a=int(input("Enter any number"))
# # for i in range(a):
# #     print(Fibo(i))



# # Find the leap year
# # def Leap(year):
# #     if (year%400==0) or (year%4==0  and year%100!=0):
# #         print("This is leap year")
# #     else:
# #         print("This is not a leap year")
# # Leap(4000)



# # def Leap(year):
# #     if (Year%400==0) or (year%4==0 and year%100!==0):
# #         print("This is leap year")
# #     else:
# #         print("not")
# # Leap(2004)        

# # Finding the sum of digits of number
# # (KeyError:int object is not iterable (for i in a ==>Thi is only for string not integer))
# # (Wrong)

# # a=int(input("enter any number"))
# # sum=0;
# # for i in a:
# #     sum=sum+i;
# # print(sum)





# # (Right Way)
# # a=int(input("enter any number"))
# # sum=0;
# # for i in range(0,a+1):
# #     sum=sum+i;
# # print(sum)




# # Using while loop

# # a=int(input("Enter any number"))
# # sum=0;
# # i=0;
# # while i<=a:
# #     sum=sum+i
# #     i=i+1
# # print(sum)





# Check if a number is prime or not

# a=int(input("Enter any number"))
# if a>2:
#     for i in range(2,a):
#         if a%i==0:
#             print(" not  Prime");
#             break;
#     else:
#             print("prime")
# else:
#     print("not prime")



# a=5
# if a>2:
#     for i in range(2,a+1):
#         if i%2==0:
#             print("prime")
#             break;
#         else:
#             print("not prime")


# # Reverse a String(using slicing)
# # a="preethi";
# # print(a[::-1])




# # Reverse a string using (Without using slicing)
# # a="preethi"
# # rev=" ";
# # for i in a:
# #     rev=i+rev;
# # print(rev)



# # Reverse a number
# # num=12345;
# # num=str(num)er4
# # rev='';
# # for i in num:
# #     rev=i+rev
# # print(rev)



# # Check if a number is palindrome
# # a=121;
# # b=str(a)
# # if b==b[::-1]:
# #     print('This is palindrome')
# # else:
# #     print("Not palindrome")




# # Finding the largest of three numbers(split is a string method)
# # a,b,c=(input("Enter any 3 numbers seperated by space:")).split()
# # if a>=b and a>=c:
# #     print("a is larger");
# # elif b>=a and b>=c:
# #     print("b is larger")
# # else:
# #     print("c is larger")
    


# # program to check vowels and consonents in a string
# # a='preethi';
# # vowelss="aeiouAEIOU"
# # vowels=0;
# # consonents=0;
# # for i in a:
# #     if i in vowelss:
# #         vowels=vowels+1;
# #     else:
# #         consonents=consonents+1;
# # print("Number of vowels are:",vowels)
# # print("Number of consonents are:",consonents)       





# # Finding (GCD) greatest common divisor

# # a=int(input("Enter first number"));
# # b=int(input("Enter second  number"))
# # while b:
# #     a,b=b,a%b;
# # print("GCD is:",a)





# # Chect anagram

# # def Check(s1,s2):
# #     if sorted(s1)==sorted(s2):
# #         print("Anagram")
# #     else:
# #         print("Not Anagram")
# # Check('listen','silent')



# # LIST
# # Find the largest and smallest or Maximum and minimum  element in the list
# # list=[1,2,3,4,5]
# # print(max(list))
# # print(min(list))





# # Without using buit in function
# # list=[1,2,3,4,5]
# # maximum=list[0]
# # for i in list:
# #     if i>maximum:
# #         maximum=i;
# # print(maximum)




# # Finding minimum element(Without builtin)
# # a=[1,2,3,4,5]
# # minimum=a[0]
# # for i in a:
# #     if i<minimum:
# #         minimum=i
# # print("Minimum element is:",minimum)




# # Second largest element in an array
# # list=[1,2,3,5,8,6,5];
# # list.sort()
# # print("Second largest element is",list[-2])




# # Reverse an array
# # list=[1,2,3,4,6]
# # print(list[::-1])



# # Without slicing
# # a=([1,2,3,4,5])
# # rev=[]
# # for i in a:
# #     rev=[i]+rev;
# # print(rev)



# # Searching an element
# # list=[1,2,3,4,9,7]
# # key=9
# # if key in list:
# #         print("Found")
# # else:
# #     print("Not Found")



# # Sum and average of all elements in a list(With builtin functions)

# # list=[1,2,3,4,5]
# # print("sum:",sum(list))
# # print("Average",sum(list)/len(list))




# # Sum and average without builtin

# # list=[1,2,3,4,5]
# # sum=0;
# # count=0
# # for i in list:
# #     sum=sum+i;
# #     count=count+1;
# # print("sum is:",sum)
# # print("Average is:",sum/count)




# # Count the even and odd numbers in the list

# # list=[1,2,3,4,5,6]
# # even=0;
# # odd=0;
# # for i in list:
# #     if i%2==0:
# #         even=even+1;
# #     else:
# #         odd=odd+1
# # print("Even numbers are:",even)
# # print("Odd numbers are:",odd)




# # Sum of all elements at even index

# # list=[1,2,3,4,5,6]
# # sum=0
# # for i in range(0,len(list),2):
# #     sum=sum+i
# # print(sum)




# # Find the smallest and second smallest element in the list

# # l=[1,2,3,4,1,6,7,9]
# # new=list(set(l))
# # new.sort()
# # print("Smallest element is:",new[0])
# # print("Second smallest element is:",new[1])




# # Count positive ,Negative and zero elements in the list

# # list=[1,2,3,4,5,6,7,-1,-6,-5,0,0,0]
# # pos=neg=zero=0;
# # for i in list:
# #     if i>0:
# #         pos+=1;
# #     elif i==0:
# #         zero+=1;
# #     else:
# #         neg+=1
# # print(f"positive numbers:{pos}\n Negative numbers:{neg}\n zeros: {zero}")



# # Seperate even and odd numbers into 2 seperate list

# # list=[1,2,3,4,5,6]
# # even=[]
# # odd=[]
# # for i in list:
# #     if i%2==0:
# #         even.append(i)
# #     else:
# #         odd.append(i)
# # print(even,"\n",odd)



# # Find the frequency of each element in an array

# # a=[1,2,3,4,5,1,2,3,4]
# # for i in set(a):
# #     print(i,"ocuure",a.count(i),"times")




# # Find the missing number from the list

# # list=[1,2,3,5,6,7,8]
# # n=len(list)+1;
# # expected_sum=n*(n+1)//2;
# # actual_sum=sum(list)
# # missing=expected_sum-actual_sum;
# # print("Missing number is",missing)




# # List packing and unpacking

# # a=["preethi",81,"student"];
# # name,marks,doing=a
# # print(name)

# # Packing:collecting multiple values and stored in a single variable
# # Unpacking:Its a opposite of packing that is we extract indivial values form the packed structure





# # Swap the 2 numbers without using any 3rd variable

# # a,b=2,3;
# # print("Before swapping:",a,b);
# # a,b=b,a;
# # print("After swapping :",a,b)



# # Remove duplicates from th list

# # l=[1,2,3,4,5,1,2,3]
# # b=list(set(l))
# # print(b)




# # Sort the dictionary by Values in an ascending order

# # dic={"a":1,"c":4,"b":2}
# # b=dict(sorted(dic.items(),key=lambda x:x[1]))
# # print(b)  
    
 
# # Sort the dictionary by Values in an  descending order
# dic={"a":1,"c":4,"b":2}
# b=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
# print(b) 
 
    
# # Diffrence between sort() and and sorted()

# #     sort                                 sorted
# # ->sort() is a list method         sorted() is a buit-in function
# # ->returns None and it             It creates the new sorted list instead and it does not change the original 
# # changes original list                  
# # ->only for list                   Any iterable(list,tuple,dictionary,set,string)





# # Merging of 2 dictionarys
# # dic1={"a":1,"c":4,"b":2}
# # dic2={"x":9,"y":8,"z":7}
# # merged=dic1|dic2
# # print(merged)


# # or

# # dic1={"a":1,"c":4,"b":2}
# # dic2={"x":9,"y":8,"z":7}
# # merged={**dic1,**dic2}
# # print(merged)



# # Finding the maximum item in the dictionary




# # print:c (Maximum key)

# # dic={"a":1,"c":4,"b":2}
# # b=max(dic.keys())
# # print(b)




# # print:4(Maximum value)

# # dic={"a":1,"c":4,"b":2}
# # b=max(dic.values())
# # print(b)




# # print:('c:4')(Maximum item)

# # dic={"a":1,"c":4,"b":2}
# # b=max(dic.items())
# # print(b)



# # Finding the minimum value in a dictionary

# # dic={"a":1,"c":4,"b":2}
# # b=min(dic.items())
# # print(b)

# # Check whether the 2 dictionarys are equal(keys and values must same order is not matter)

# # False
# # dic1={"a":1,"c":4,"b":2}
# # dic2={"c":9,"b":8,"a":7}
# # print(dic1==dic2)

# # # True
# # dic1={"a":1,"c":4,"b":2}
# # dic2={"c":4,"b":2,"a":1}
# # print(dic1==dic2)





# # n=5;
# # a,b=0,1
# # for _ in range(n):
# #     print()



# class A(type):
#     def __init__(self,name):
#         self.name=name
#         print("Name is:",self.name)
# a=A("preethi")



# s="programming language is the best"
# print(len(s))


# Finding the max length of the word

# s = "programming language is the best"
# words = s.split()              
# longest = max(words, key=len)  
# print("Longest word:", longest)
# print("Length:", len(longest))



