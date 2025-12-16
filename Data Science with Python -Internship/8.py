# # # def func(*n):
# # #     print(n)
# # # func(1,2,3)



# # # def func(*n):
# # #     total=sum(n)
# # #     print("sum:",total)
# # # func(1,2,3)



# # # def my(*args):
# # #     for item in args:
# # #         print(item)
# # # my(10,20,30)




# # # def add(*numbers):
# # #     sum=0;
# # #     for i in numbers:
# # #         sum=sum+i;
# # #     print(sum)
# # # add(1,2,3,4)
# # # add(7,8)




# # # Be carefull where is the print statement
# # # def add(*numbers): 
# # #     sum=0;
# # #     for i in numbers:
# # #         sum=sum+i;
# # #         print(sum)
# # # add(7,8)





# # # def add(*numbers): 
# # #     sum=0;
# # #     for i in numbers:
# # #         sum=sum+i;
# # #     print(sum)
# # # add(7,8)
# # # add(4,6,9,7)
# # # add(4,6,7,2,4,6,9)




# # # def My(*kids):
# # #     print("THe youngestchild is:" + kids[1])
# # # My('email','preethi','raju');


# # # keyword  arguments * and arbitary argument **

# # # emails=["divya@gamil.com","preethi@gamil.com","surya@yahoo.com","mahesg@yahoo.com"]
# # # gmail_users=[i for i in emails if "@gmail.com" in i]
# # # print(gmail_users)


# # # lambda arguments:expression (only one expression it perform)
# # # lambda function
# # # lambda function is a small anonimous function it only perform one expression
# n number of arguments only one expreesion
# # sub=lambda x,y:x-y
# # print(sub(3,5))


# # sum=lambda x,y:x+y
# # print(sum(3,4))



# diff=lambda x,y:x-y
# print(diff(4,5))


# mul=lambda x,y:x*y;
# print(mul(3,3))



# MAP FUNCTION   map()

# nums=[1,2,3,4,5]
# square=list(map(lambda x:x**2,nums))
# print(square)



# nums=[1,2,3,4,5]
# square=set(map(lambda x:x**2,nums))
# print(square)




# nums=[1,2,3,4,5]
# square=tuple(map(lambda x:x**2,nums))
# print(square)



# nums=[1,2,3,4,5]
# square=list(filter(lambda x:x%2==0,nums))
# print(square)

# chaith=0 index,21 is 1 index so if we give 2 we get error
# student=[("chaithra",21),("kaif",19),("vanitha",20)]
# sorted_students=sorted(student,key=lambda x:x[1])
# print(sorted_students)



# pass by value or call by value   (drinking juce)
# pass by reference or pass by reference


# pass by value or pass by reference
# def change_number(x):
#     x=10
#     print("Inside The function",x)
# num=20; 
# change_number(num)
# print("Outside the function",num)



# call by reference or pass by reference
# def change_number(x):
#     x.append(4);
#     print("Insede the function",x)
# list=[1,2,3]
# change_number(list)
# print("outside the function",list)


# local and global varible
# global varible =>declare the variable out side the function we can accces it inside or outside the function




