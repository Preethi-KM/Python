
# # # # # # # # # # # # # # remove(value)=>syntax
# # # # # # # # # # # # # list=[1,3,3,2,4];
# # # # # # # # # # # # # # list.remove(4)
# # # # # # # # # # # # # # print(list)

# # # # # # # # # # # # # list.pop(3)
# # # # # # # # # # # # # print(list)



# # # # # # # # # # # # # list.pop()
# # # # # # # # # # # # # print(list)


# # # # # # # # # # # # # index(value)
# # # # # # # # # # # # list=[10,20,[2,3,4],30,40];
# # # # # # # # # # # # # print(list.index(10))
# # # # # # # # # # # # print(list.index(3));



# # # # # # # # # # # # count(value)
# # # # # # # # # # # list=[1,2,2,3,2,4,1];
# # # # # # # # # # # print(list.count(1));


# # # # # # # # # # in python2 print is a statement,in python3 print is a function
# # # # # # # # # # python2=>range(slow,more memory consumption),python3=>xrange(fast,less memory)



# # # # # # # # # # # sort=>sort(reverse=True)
# # # # # # # # # list=[3,1,4,5];
# # # # # # # # # # list.sort()
# # # # # # # # # # print(list)


# # # # # # # # # # dec syntax=>sort(reverse=True);
# # # # # # # # # list.sort(reverse=True);
# # # # # # # # # print(list)





# # # # # # # # # Finding maximum and minimum===>max(variable),min(variable)
# # # # # # # # # list=[1,2,3,4,5];
# # # # # # # # # print(max(list));
# # # # # # # # # print(min(list));


# # # # # # # # # Find the max and min without using inbuit function
# # # # # # # # list=[1,2,3,4,5,6,7];
# # # # # # # # max=list[0];
# # # # # # # # for i in range(1,len(list)):
# # # # # # # #     if list[i]<max:
# # # # # # # #         max=list[i];
# # # # # # # # print(max)



# # # # # # # # # reverse
# # # # # # # # list=[1,2,3,4];
# # # # # # # # list.reverse()
# # # # # # # # print(list)


# # # # # # # list=[2.5,2,3,5]
# # # # # # # for i in list:
# # # # # # #     print(i)
# # # # # # #     if i==2:
# # # # # # #         list.append(6)




# # # # # # x=[2.5,2,3,5]
# # # # # # for i in range(5-len(x)):
# # # # # #     x.append(6)
# # # # # #     print(x)




# # # # # # extend(iterator)
# # # # # list=[1,2,3,4];
# # # # # list.extend("hello");
# # # # # print(list)


# # # # # # but in append
# # # # # list=[1,2,3,4];
# # # # # list.append("hello");
# # # # # print(list)



# # # # # list concatination
# # # # list=[1,2,3,4];
# # # # list1=[5,6,7,8];
# # # # con=list+list1;
# # # # print(con);





# # # # ?adding elements dynamically with for LookupError
# # # list=[];
# # # for i in range(5):
# # #     list.append(i)
# # # print(list)



# # # list=[];
# # # for i in range(5):
# # #     list.append(i)
# # #     print(list)


# # list=[];
# # for i in range(5):
# #     list.append("*")
# #     print(list)



# list=[];
# for i in range(0,10,2):
#     list.append(i)
#     print(list)



# dUnorderiction version
# <3.7 dic=>
# # >3.7 =orderd


# loop,list=====>exam