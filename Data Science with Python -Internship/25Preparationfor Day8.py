# # # # # # # # # # # # def greet():
# # # # # # # # # # # #     print("Hello,World!")
# # # # # # # # # # # # greet()



# # # # # # # # # # # def greet(name):
# # # # # # # # # # #     print("Hello",name);
# # # # # # # # # # # greet("preethi")



# # # # # # # # # # def add(a,b):
# # # # # # # # # #     print(a+b);
# # # # # # # # # # add(2,3);




# # # # # # # # # a=int(input("Enter any number"))
# # # # # # # # # def Check(num):
# # # # # # # # #     if a%2==0:
# # # # # # # # #         return "even"
# # # # # # # # #     else:
# # # # # # # # #         return "odd"
# # # # # # # # # print(Check(a))




# # # # # # # # def Square(a):
# # # # # # # #     print(a*a);
# # # # # # # # Square(2)
# # # # # # # # Square(5)



# # # # # # # def Factorial(num):
# # # # # # #     fact=1;
# # # # # # #     for i in range(1,num+1):
# # # # # # #         fact=fact*i;
# # # # # # #     print(fact)
# # # # # # # Factorial(6)




# # # # # # def Factorial(num):
# # # # # #     fact=1;
# # # # # #     for i in range(1,num+1):
# # # # # #         fact=fact+i;
# # # # # #     print("factorial of ",num,"is",fact);
# # # # # # Factorial(5)




# # # # # # def Maximum(a,b,c):
# # # # # #     if a>=b and a>=c:
# # # # # #         return "a is bigger"
# # # # # #     elif b>=a and b>=c:
# # # # # #         return "b is bigger"
# # # # # #     else:
# # # # # #         return "c is bigger"
# # # # # # print(Maximum(2,3,4));



# # # # # # Simple interest (principle*rate*time)/100 or PRT/100

# # # # # def Simple(a,b,c):
# # # # #     return (a*b*c)/100;
# # # # # print(Simple(1,2,3))



# # # # # Area and Circumference of a circle
# # # # # pi *r**2,circumference 2*pi*r



# # # # import math;
# # # # def Area(r):
# # # #     area=math.pi*r**2;
# # # #     circumference=2*math.pi*r
# # # #     print("AREA:",area)
# # # #     print("CIRCUMFERENCE:",circumference);
# # # # Area(3)




# # # def greet(name,message="Good Morning"):
# # #     print("Hi....",name,message)
# # # greet("preethi","good Evening");
# # # greet("Raju")



# # def Text(string):
# #     count=0
# #     vowels="aeiouAEIOU"
# #     for i in string:
# #         if i in "aeiou":
# #             count=count+1;
# #     return count;
# # print(Text("preethi"))
        


# def Check(string):
#     count=0;
#     vowels="aeiouAEIOU"
#     for i in string:
#         if i in vowels:
#             count=count+1;
#     print(count)
# Check("preethi")



# def Rev(list):
#     new_list=[];
#     for i in range(len(list)-1,-1,-1):
#         new_list.append(list[i])
#     return new_list
# print(Rev([1,2,3,4,5]));


def REV(list):
    for i in list:
        list.sort();
    print(list[-2])
REV([2,3,14,5,7])
