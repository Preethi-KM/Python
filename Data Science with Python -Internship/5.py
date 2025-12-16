# # # # # # # # # # # # names=("d","a","s");
# # # # # # # # # # # # print(names)



# # # # # # # # # # # # person=("Arun",25,True);
# # # # # # # # # # # # person=list(person);
# # # # # # # # # # # # person[1]=26;
# # # # # # # # # # # # person=tuple(person);
# # # # # # # # # # # # print(person)




# # # # # # # # # # # # person=("Arun",25,True,2,1,11,23,(56,77),"good");
# # # # # # # # # # # # # person=list(person);
# # # # # # # # # # # # # person[7][0]=57;
# # # # # # # # # # # # # person=tuple(person);                                     
# # # # # # # # # # # # # print(person)



# # # # # # # # # # # # person=("Arun",25,True,2,1,11,23,(56,77),"good");
# # # # # # # # # # # # person=list(person);
# # # # # # # # # # # # print(person);
# # # # # # # # # # # # person[7]=list(person[7]);
# # # # # # # # # # # # print(person[7]);
# # # # # # # # # # # # person[7][0]=50;
# # # # # # # # # # # # person[7]=tuple(person[7]);
# # # # # # # # # # # # print(tuple(person))




# # # # # # # # # # # person=("Arun",25,True,2,1,11,23,(56,77),"good");
# # # # # # # # # # # person=list(person);
# # # # # # # # # # # person[7]=list(person)
# # # # # # # # # # # print(person);




# # # # # # # # # tuple=(1,"hello",3,4,5,6,6.0);
# # # # # # # # # # # tuple=list(tuple);
# # # # # # # # # # # tuple[1]="bye";
# # # # # # # # # print(tuple[::])
# # # # # # # # # # # tuple[6]=6;
# # # # # # # # # # # print(tuple);



# # # # # # # # # tuple=("Hello",)*3
# # # # # # # # # print(tuple);



# # # # # # # # # tuple=("Hello")*3
# # # # # # # # # print(tuple);




# # # # # # # # memebership check
# # # # # # # # fruit=("apple","banana","cherry");
# # # # # # # # print("apple" in fruit);
# # # # # # # # print("grape" not in fruit)
# # # # # # # # print("grape" in fruit)



# # # # # # # set1={""};
# # # # # # # print(type(set1))

# # # # # # # set=set();
# # # # # # # print(type(set))

# # # # # # # set1={};
# # # # # # # print(type(set1))



# # # # # # sett={1,2,3,4,5}
# # # # # # print(sett)

# # # # # for inserting single value
# # # # # sett={1,2,3,4,5}
# # # # # sett.add(6);
# # # # # print(sett)


# # # # for inserting multiple elementa
# # sett={1,2,3,4,5}
# # # # sett.update([6,7,8]);
# # # # print(sett)                                  verify
# # # sett.remove(9)
# # for i in sett:
# #     print(i)



# # pop remove the random element
sett={1,2,3,4,5};
# poped_element=sett.pop()
# print(sett)
# print(poped_element)

sett.clear();
print(sett);


