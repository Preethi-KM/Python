# # # # list=[1,2,3,4,5,6,7];
# # # # evens=[x for x in list if x%2==0]
# # # # print(evens)


# # # # list=[1,2,3,4,5,6,7];
# # # # odd=[x for x in list if x%2!=0]
# # # # print(odd)


# # # # # how to create new list from the existing list(importent)
# # # # num=[1,2,3,4,5,6,7,8,9,10]
# # # # values_numbers=[2,3,9];
# # # # filter=[i for i in num if i not in values_numbers]
# # # # print(filter)


# # # # FUNCTIONS

# # # def function_name():
# # #     statement; pass
# # # # function();
# # # by using pass also we ca create empty function?




# # # def A():
# # #     print(2+3)    print will not strore any value it just print the value
# # # A()


# # # def A():
# # #     print(2+3)   
# # # a=A()
# # # print(a)



# # # def A():
# # #       return 2+3     it does not print just store the value  
# # # a=A()
# # # print(a)





# # # def A():
# # #       return 2+3      
# # # a=A()
# # # print(a)
# # # print(a+6)




# # # def A():
# # #       print( 2+3 )     
# # # a=A()
# # # print(a)
# # # print(a+6)  one is string and onother one is int concatination not possible(Type Error)


# # # def A():
# # #           print( 2+3 )     
# # # a=A()
# # # print(a)
# # # print(5+6) 



# # # print=>only print the value won't store the Value
# # # return=>only store the value it won't print the value



# # # packing and unpacking
# # # packing
# # # list=[1,2,3,4,5];
# # # print(list)



# # # unpacking
# # # list=[1,2,3,4,5]
# # # (a,b,c,d,e)=list
# # # print(a);
# # # print(b);
# # # print(c)
# # # print(d)
# # # print(e)



# # # unpacking in tuple
# # # tuple=(1,2,3,4,5)
# # # (a,b,c,d,e)=tuple
# # # print(a)


# # # def painter(msg):
# # #     print("msg:",msg)
# # # painter("hello")


# # # # msg=>parameter
# # # # hello=>arguments


# # # # def painter(a,b):
# # # #     print(a+b)
# # # # painter(2,3)






# # # def painter(a=0,b=5):  
# # #     print(a+b)
# # # painter(2,3)
# # # # python is a line by line execution so finally it replase 0 with 2 and 5 with 3





# # # def painter(a=0,b=5):  
# # #     print(a+b)
# # # painter()
# # # if we does not pass anythng then it prints the default values





# # # types of arguments

# # 1.positional argument
# # 2.Keyword argumemnt
# # 3.default argument




# # Remove duplicate ===>Try using set
# # def removeduplicate():
# #     given_str="abcddd"
# #     original_string=" ".join(dict.fromkeys(given_str))
# #     print(original_string)
# # removeduplicate()




# # def removeduplicate():
# #     given_str="abcddd"
# #     original_string="-".join(dict.fromkeys(given_str))
# #     print(original_string)
# # removeduplicate()




# # calling function multiple times
# def one(a,b):
#     print(a+b);
# one(2,3)
# one(4,5)
# one(6,2)



# # taking input from the user
# a=int(input("Enter a value"));
# b=int(input("Enter b value"))
# def one(a,b):
#     print(a+b);
# one(2,3)
# one(4,5)
# one(6,2)
# one(a,b)



# taking input from the user

# def one(a,b):
#     a=int(input("Enter a value"));
#     b=int(input("Enter b value"))
#     print(a+b);
# one(2,3)
# one(4,5)
# one(6,2)
# one(a,b)


# def one(a,b):
#     print(a+b);
# one(2,3)
# a=int(input("Enter a value"));
# b=int(input("Enter b value"))



# def one (a,b):
#     print(a+b)  erre :position 
# print(2)
# we can achive this using default parameters 



# .__doc__  We can acces the comments  __init__ (check it)

# def add(a,b):
#     return a+b
# ''' add 2 numbers'''
# print(add.__doc__)

# # arbitary arguments overcome the positional arguments
# def fun(*arg):
#     return arg[0]-arg[1]
# print(fun(2,3,4,5,6,7,8))



double=lambda x:x*x
print(double(2))