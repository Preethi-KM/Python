# # # # tup=(1,2,3,4,5,6);
# # # # new=list(tup);
# # # # new[0]=float(new[0])
# # # # new[1]=float(new[1])
# # # # new[3]=float(new[3])
# # # # tup=tuple(new);
# # # # print(tup);



# # # tup=(1,2,3.0,4,5,6.0);
# # # new=list(tup);
# # # new[1]=float(new[1])
# # # new[2]=int(new[2])
# # # new[5]=int(new[5])
# # # tup=tuple(new);
# # # print(tup)



# # # keeps element in a but not b
# # a={1,2,3,4,5};
# # b={6,7,8,9,6}
# # print(a-b);
# # print(a.difference(b))



# # # # keeps the elements in b but not a
# # a={1,2,3,4,5};
# # b={6,7,8,9,6}
# # print(b-a);
# # print(b.difference(a));




# # SymmetricDiffrence
# # Keeps the elements in either A or B but not both

# a={1,2,3};
# b={3,4,5};
# print(a^b);
# print(a.symmetric_difference(b));
