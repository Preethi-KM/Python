# # def Factorial(n):
# #     if n==0 or n==1:
# #         return 1
# #     else:
# #         return n*Factorial(n-1)
# # print(Factorial(5))
# # print(Factorial(3))


# # out
# # 5*Factorial(4)
#     # 4*Factorial(3)
#         # 3*Factorial(2)
#             # 2*Factorial(1)



# # Modules and packages

# def leap(year):
#     Leap=False;
#     if (year % 400==0) or (year %4==0 and year % 100!=0):
#         Leap=True;
#     return Leap;
# a=leap(4000) 
# print(a)

    
    
    
    
# a=int(input("Enter any year"))
# if(a%400==0)or(a%4==0 and a%100!=0):
#     print(f"{a}: is leap year");
# else:
#     print("This is not a leap year")  



# def Leap_year(year):
#     if (year%400==0)or (year %4==0 and year %100!=0):
#         print(f"{year}:This is a leap year")
#     else:
#         print(f"{year}:This is not a leap year")  
# Leap_year(4000)