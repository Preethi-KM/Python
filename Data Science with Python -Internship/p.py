# a=10
# b='preethi'
# c=True
# d=3.4
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# Checking numner is positive and negative
# a=10;
# if a>0 or a==0:
#     print("number is positive")
# else:
#     print("number is negative")
    
    
    
# def find(a):
#     if a==0:
#         print("zero neither positive nor negative")
    
#     elif a>0:
#         print(f"{a} is positive")
#     else:
#         print(f"{a} is negative")
# find(0)




# def fact (num):
#     if num==0 or num==1:
#         return 1;
#     else:
#         return num*fact(num-1)
# a=fact(5);
# print(a)



# def factorial(n):
#     fact=1;
#     for i in  range(1,n+1):
#         fact=fact*i;
#     print(fact);
# factorial(5)

    
    
    
# def factorial(n):
#     fact=1;
#     for i in range(1,n+1):
#         fact=fact*i;
#     print(fact);
# factorial(5)
                
                
                
# num=5
# a,b=0,1;
# for _ in range(num):
#     print(a,end="");
#     a,b=b,a+b;


# num=5;
# a,b=0,1;
# for _ in range(num+1):
#     print(a,end=" ")
#     a,b=b,a+b
    
    
def leap(year):
    if (year%400==0) or (year%4==0  and year %100!=0):
        print(f"{year} is leap year");
    else:
        print("This is not a leap year");
leap(2024);