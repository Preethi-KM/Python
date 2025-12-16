#Factorial of number
#a=int(input("Enter any number"));
# fact=1;
# for i in range(1,a+1):
#     fact=fact*i;
# print(fact)


# Factorial of number using function
# def Fact(n):
#     fact=1;
#     for i in range(1,n+1):
#         fact=fact*i;
#     print(fact);
# Fact(5)


# Checking palindreome without using sicing
# string='pop'
# rev='';
# for i  in string:
#     rev=i+rev;
# if rev==string:
#     print("This is palindrome");
# else:
#     print("This is not palindrome");
    
    
    
# Checking palindrome with using slicing   
# string="mam";
# if string==string[::-1]:
#     print("This is palindrome");
# else:
#     print("this is not a palindrome")


# Finding the largest of 3 numbers
# a,b,c=10,20,30;
# if a>=b and a>=c:
#     print("a is larger");
# elif  b>=a and b>=c:
#     print("b is larger")
# else:
#     print("c is larger")
    
    
# Finding the largest of 3 numbers in function with using built in function   
# def largest(a,b,c):
#     return max(a,b,c)
# print(largest(10,20,30))



# Reverse a string withou using any built in function
# string="preethi";
# rev='';
# for i in string:
#     rev=i+rev;
# print(rev);


# Reversing a string in function
# def Rever(string):
#     rev='';
#     for i in string:
#         rev=i+rev;
#     print(rev);
# Rever("preethi")


# Reversing a string using slicing
# string="preethi";
# b=string[::-1]
# print(b)



# Finding the vowelse and consonents using function
# def Find(string):
#     vow_count=0;
#     consonent_count=0;
#     vowels="aeiouAEIOU"
#     for i in string:
#         if i in vowels:
#             vow_count+=1;
#         else:
#             consonent_count+=1;
#     print("vowel counts are:",vow_count);
#     print("consonents counts are:",consonent_count)
# Find("preethi")




# Removing duplicates in an list
# list=[1,2,3,4,1,2,3,4]
# new_list=[]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)



# Removing duplicates with using sequences
# def Remove(duplicate):
#     return list(set(duplicate))
# print(Remove([1,2,3,1,2,3]))


# Finding the second largest element
# list=[1,2,3,42,3,567,9];
# list.sort()
# print(list[-2])


# Finding the second largest element using function
# def second(list):
#     list.sort()
#     print(list[-2])
# second([1,2,5,4,6,8])


# Sorting elements withot using any built in function sort()
# def Sorting(list):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#     return list
# print(Sorting([2,3,4,56,1,3,4]));




# Practicing the sorting elements without using any buitin function practice once again
# def Sorting(list):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i];
#     print(list);
# Sorting([1,2,9,5,4,3,7])




# def Common(lst1,lst2):
#     print(list(set(lst1) & set(lst2)))  
# Common([1,2,3],[41,1,2,3])
    
    
    
    
    
    
# #Fibonocci series    
# def Fibo(num):
#     a,b=0,1;
#     for _ in range(num):
#         print(a);
#         a,b=b,a+b;
# Fibo(7)
         

# dictionary={'a':2,'b':1,'c':3}
# dictionary.sorted()
# for key,value in dictionary.items():
#     print(value.sort())


#Checking prime or not   
# def Prime(num):
#     if num>1:
#         for i in range(2,num):
#             if num%2==0:
#                 print("This is not prime");
#                 break;
#             else:
#                 print("this is prime");
# Prime(6);


# # Checking prime or not
# def Checkin(num):
#     if num>1:
#         for i in range(2,num):
#             if num%2==0:
#                 print("This is not a prime")
#                 break;
#             else:
#                 print("This is prime")
# Checkin(3)



# # Check for angram string
# def Anagram(s1,s2):
#     if sorted(s1)==sorted(s2):
#         print("Thease are anagrams")
#     else:
#         print("these strings are not anagrams")
# Anagram("listen","silent");


# List comprahention
# list=[1,2,3,4,5];
# b=[x*x for x in list ]
# print(b)


# list=[1,2,3,4,5,6,7]
# b=[x for x in list if x%2==0]
# print(b)



# list=[1,2,3,4,5]
# b=["even" if x%2==0 else "odd" for x in list]
# print(b)



# function


# Finally good performance (Thank god )
